from __future__ import print_function
import numpy as np
import random
from tqdm import tqdm
import os, sys, pdb, math
# import cPickle as cp
import _pickle as cp  # python3 compatability
import networkx as nx
import argparse
import scipy.io as sio
import scipy.sparse as ssp
from sklearn import metrics
from gensim.models import Word2Vec
import warnings
from multiprocessing.pool import Pool
from functools import  partial
warnings.simplefilter('ignore', ssp.SparseEfficiencyWarning)
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append('%s/../../pytorch_DGCNN' % cur_dir)
sys.path.append('%s/software/node2vec/src' % cur_dir)
from util import GNNGraph
import node2vec

def sample_neg(net, test_ratio=0.1, train_pos=None, test_pos=None, max_train_num=None,
               bi_network = False,first_kind_node_num=None):
    if bi_network:
        net1 = net.copy().toarray()
        net1[:,range(first_kind_node_num)] = 0
        net1[range(first_kind_node_num,net1.shape[0]),:] = 0
        net_triu = ssp.csr_matrix(net1)
    else:
        # get upper triangular matrix
        net_triu = ssp.triu(net, k=1)
    # sample positive links for train/test
    row, col, _ = ssp.find(net_triu)
    # sample positive links if not specified
    if train_pos is None or test_pos is None:
        perm = random.sample(range(len(row)), len(row))
        row, col = row[perm], col[perm]
        split = int(math.ceil(len(row) * (1 - test_ratio)))
        train_pos = (row[:split], col[:split])
        test_pos = (row[split:], col[split:])
    # if max_train_num is set, randomly sample train links
    if max_train_num is not None:
        perm = np.random.permutation(len(train_pos[0]))[:max_train_num]
        train_pos = (train_pos[0][perm], train_pos[1][perm])
    # sample negative links for train/test
    train_num, test_num = len(train_pos[0]), len(test_pos[0])
    neg = ([], [])
    n = net.shape[0]
    print('sampling negative links for train and test')
    while len(neg[0]) < train_num + test_num:
        if bi_network:
            i, j = random.randint(first_kind_node_num, n - 1), random.randint(0, first_kind_node_num-1)
            if net[i, j] == 0:
                neg[0].append(i)
                neg[1].append(j)
            else:
                continue
        else:
            i, j = random.randint(0, n - 1), random.randint(0, n - 1)
            if i < j and net[i, j] == 0:
                neg[0].append(i)
                neg[1].append(j)
            else:
                continue
    train_neg  = (neg[0][:train_num], neg[1][:train_num])
    test_neg = (neg[0][train_num:], neg[1][train_num:])
    return train_pos, train_neg, test_pos, test_neg

def sample_neg_for_cross_validation(net, pos=None, bi_network = False,first_kind_node_num=None):
    if bi_network:
        net1 = net.copy().toarray() # 此处有可优化的部分，不用toarray()应该也能赋。
        net1[:,range(first_kind_node_num)] = 0
        net1[range(first_kind_node_num,net1.shape[0]),:] = 0
        net_triu = ssp.csr_matrix(net1)
    else:
        # get upper triangular matrix
        net_triu = ssp.triu(net, k=1)
    # sample positive links for train/test
    row, col, _ = ssp.find(net_triu)
    # sample positive links if not specified
    # sample positive links if not specified
    if pos is None:
        perm = random.sample(range(len(row)), len(row))
        pos = (row[perm], col[perm])
    # sample negative links
    pos_num= len(pos[0])
    neg = ([], [])
    n = net.shape[0]
    print('sampling negative links for train and test')
    while len(neg[0]) < pos_num:
        if bi_network:
            i, j = random.randint(0, first_kind_node_num-1) ,random.randint(first_kind_node_num, n - 1)
            if net[i, j] == 0:
                neg[0].append(i)
                neg[1].append(j)
            else:
                continue
        else:
            i, j = random.randint(0, n - 1), random.randint(0, n - 1)
            if i < j and net[i, j] == 0:
                neg[0].append(i)
                neg[1].append(j)
            else:
                continue
    return pos, neg
    
def links2subgraphs(A, train_pos, train_neg, test_pos, test_neg, h=1, max_nodes_per_hop=None, node_information=None):
    # automatically select h from {1, 2}
    if h == 'auto':
        # split train into val_train and val_test
        _, _, val_test_pos, val_test_neg = sample_neg(A, 0.1)
        val_A = A.copy()
        val_A[val_test_pos[0], val_test_pos[1]] = 0
        val_A[val_test_pos[1], val_test_pos[0]] = 0
        val_auc_CN = CN(val_A, val_test_pos, val_test_neg)
        val_auc_AA = AA(val_A, val_test_pos, val_test_neg)
        print('\033[91mValidation AUC of AA is {}, CN is {}\033[0m'.format(val_auc_AA, val_auc_CN))
        if val_auc_AA >= val_auc_CN:
            h = 2
            print('\033[91mChoose h=2\033[0m')
        else:
            h = 1
            print('\033[91mChoose h=1\033[0m')

    # extract enclosing subgraphs
    max_n_label = {'value': 0}
    def helper(A, links, g_label):
        g_list = []
        for i, j in tqdm(zip(links[0], links[1])):
            g, n_labels, n_features = subgraph_extraction_labeling((i, j), A, h, max_nodes_per_hop, node_information)
            max_n_label['value'] = max(max(n_labels), max_n_label['value'])
            g_list.append(GNNGraph(g, g_label, n_labels, n_features))
        return g_list
    def helper2(A,links,g_label):
        g_list = []
        Q = A**h
        for i, j in tqdm(zip(links[0], links[1])):
            g, n_labels, n_features = extract_subgraph((i, j), A, Q, node_information)
            max_n_label['value'] = max(max(n_labels), max_n_label['value'])
            g_list.append(GNNGraph(g, g_label, n_labels, n_features))
        return g_list
    def helper3(A,links,g_label):
        g_list = []
        pool = Pool(processes=10)
        with tqdm(total=len(links)) as pbar:
            for i,subgraph in tqdm(enumerate(pool.imap(partial(subgraph_extraction_labeling, A=A,h=h,max_nodes_per_hop=max_nodes_per_hop,node_information=node_information),
                                                       [(i,j) for i, j in zip(links[0], links[1])]))):
                pbar.update()
                max_n_label['value'] = max(max(subgraph[1]), max_n_label['value'])
                g_list.append(GNNGraph(subgraph[0], g_label, subgraph[1], subgraph[2]))

        return g_list
    print('Enclosing subgraph extraction begins...')
    train_graphs = helper3(A, train_pos, 1) + helper3(A, train_neg, 0)
    test_graphs = helper3(A, test_pos, 1) + helper3(A, test_neg, 0)
    print(max_n_label)
    return train_graphs, test_graphs, max_n_label['value']

def selfDefine_links2subgraphs(A, links, g_label=0, h=1, max_nodes_per_hop=None, node_information=None):
    # automatically select h from {1, 2}
    if h == 'auto':
        # split train into val_train and val_test
        _, _, val_test_pos, val_test_neg = sample_neg(A, 0.1)
        val_A = A.copy()
        val_A[val_test_pos[0], val_test_pos[1]] = 0
        val_A[val_test_pos[1], val_test_pos[0]] = 0
        val_auc_CN = CN(val_A, val_test_pos, val_test_neg)
        val_auc_AA = AA(val_A, val_test_pos, val_test_neg)
        print('\033[91mValidation AUC of AA is {}, CN is {}\033[0m'.format(val_auc_AA, val_auc_CN))
        if val_auc_AA >= val_auc_CN:
            h = 2
            print('\033[91mChoose h=2\033[0m')
        else:
            h = 1
            print('\033[91mChoose h=1\033[0m')

    # extract enclosing subgraphs
    max_n_label = {'value': 0}
    def helper(A, links, g_label):
        g_list = []
        for i, j in tqdm(zip(links[0], links[1])):
            g, n_labels, n_features,node_mask = subgraph_extraction_labeling((i, j), A, h, max_nodes_per_hop, node_information)
            max_n_label['value'] = max(max(n_labels), max_n_label['value'])
            g_list.append(GNNGraph(g, g_label, n_labels, n_features))
        return g_list

    def helper3(A,links,g_label):
        g_list = []
        pool = Pool(processes=10)
        with tqdm(total=len(links)) as pbar:
            for i,subgraph in tqdm(enumerate(pool.imap(partial(subgraph_extraction_labeling, A=A,h=h,max_nodes_per_hop=max_nodes_per_hop,node_information=node_information),
                                                       [(i,j) for i, j in zip(links[0], links[1])]))):
                pbar.update()
                max_n_label['value'] = max(max(subgraph[1]), max_n_label['value'])
                g_list.append(GNNGraph(subgraph[0], g_label, subgraph[1], subgraph[2]))

        return g_list
    print('Enclosing subgraph extraction begins...')
    graphs = helper3(A,links,g_label)
    print(max_n_label)
    return graphs, max_n_label['value']

def subgraph_extraction_labeling(ind, A, h=1, max_nodes_per_hop=None, node_information=None):
    # extract the h-hop enclosing subgraph around link 'ind'
    dist = 0
    nodes = set([ind[0], ind[1]])
    visited = set([ind[0], ind[1]])
    fringe = set([ind[0], ind[1]])
    nodes_dist = [0, 0]
    for dist in range(1, h+1):
        fringe = neighbors(fringe, A)
        fringe = fringe - visited
        visited = visited.union(fringe)
        if max_nodes_per_hop is not None:
            if max_nodes_per_hop < len(fringe):
                fringe = random.sample(fringe, max_nodes_per_hop)
        if len(fringe) == 0:
            break
        nodes = nodes.union(fringe)
        nodes_dist += [dist] * len(fringe)
    # move target nodes to top
    nodes.remove(ind[0])
    nodes.remove(ind[1])
    nodes = [ind[0], ind[1]] + list(nodes) 
    subgraph = A[nodes, :][:, nodes]
    # apply node-labeling
    labels = node_label(subgraph)
    # get node features
    features = None
    if node_information is not None:
        features = node_information[nodes]
    # construct nx graph
    g = nx.from_scipy_sparse_matrix(subgraph)
    # remove link between target nodes
    if g.has_edge(0, 1):
        g.remove_edge(0, 1)
    return g, labels.tolist(), features


def neighbors(fringe, A):
    # find all 1-hop neighbors of nodes in fringe from A
    res = set()
    for node in fringe:
        nei, _, _ = ssp.find(A[:, node])
        nei = set(nei)
        res = res.union(nei)
    return res


def node_label(subgraph):
    # an implementation of the proposed double-radius node labeling (DRNL)
    K = subgraph.shape[0]
    subgraph_wo0 = subgraph[1:, 1:]
    subgraph_wo1 = subgraph[[0]+list(range(2, K)), :][:, [0]+list(range(2, K))]
    dist_to_0 = ssp.csgraph.shortest_path(subgraph_wo0, directed=False, unweighted=True)
    dist_to_0 = dist_to_0[1:, 0]
    dist_to_1 = ssp.csgraph.shortest_path(subgraph_wo1, directed=False, unweighted=True)
    dist_to_1 = dist_to_1[1:, 0]
    d = (dist_to_0 + dist_to_1).astype(int)
    d_over_2, d_mod_2 = np.divmod(d, 2)
    labels = 1 + np.minimum(dist_to_0, dist_to_1).astype(int) + d_over_2 * (d_over_2 + d_mod_2 - 1)
    labels = np.concatenate((np.array([1, 1]), labels))
    labels[np.isinf(labels)] = 0
    labels[labels>1e6] = 0  # set inf labels to 0
    labels[labels<-1e6] = 0  # set -inf labels to 0
    return labels

def extract_subgraph(ind, A, Q, node_information=None):
    nodes = neighbors(ind,Q)
    nodes.remove(ind[0])
    nodes.remove(ind[1])
    nodes = [ind[0], ind[1]] + list(nodes)
    subgraph = A[nodes, :][:, nodes]
    # apply node-labeling
    labels = node_label(subgraph)
    # get node features
    features = None
    if node_information is not None:
        features = node_information[nodes]
    # construct nx graph
    g = nx.from_scipy_sparse_matrix(subgraph)
    # remove link between target nodes
    if g.has_edge(0, 1):
        g.remove_edge(0, 1)
    return g, labels.tolist(), features


def generate_node2vec_embeddings(A, emd_size=128, negative_injection=False, train_neg=None):
    if negative_injection:
        row, col = train_neg
        A = A.copy()
        A[row, col] = 1  # inject negative train
        A[col, row] = 1  # inject negative train
    nx_G = nx.from_scipy_sparse_matrix(A)
    G = node2vec.Graph(nx_G, is_directed=False, p=1, q=1)
    G.preprocess_transition_probs()
    walks = G.simulate_walks(num_walks=10, walk_length=80)
    walks = [list(map(str, walk)) for walk in walks]
    model = Word2Vec(walks, size=emd_size, window=10, min_count=0, sg=1, 
            workers=8, iter=1)
    wv = model.wv
    embeddings = np.zeros([A.shape[0], emd_size], dtype='float32')
    sum_embeddings = 0
    empty_list = []
    for i in range(A.shape[0]):
        if str(i) in wv:
            embeddings[i] = wv.word_vec(str(i))
            sum_embeddings += embeddings[i]
        else:
            empty_list.append(i)
    mean_embedding = sum_embeddings / (A.shape[0] - len(empty_list))
    embeddings[empty_list] = mean_embedding
    return embeddings


def AA(A, test_pos, test_neg):
    # Adamic-Adar score
    A_ = A / np.log(A.sum(axis=1))
    A_[np.isnan(A_)] = 0
    A_[np.isinf(A_)] = 0
    sim = A.dot(A_)
    return CalcAUC(sim, test_pos, test_neg)
    
        
def CN(A, test_pos, test_neg):
    # Common Neighbor score
    sim = A.dot(A)
    return CalcAUC(sim, test_pos, test_neg)


def CalcAUC(sim, test_pos, test_neg):
    pos_scores = np.asarray(sim[test_pos[0], test_pos[1]]).squeeze()
    neg_scores = np.asarray(sim[test_neg[0], test_neg[1]]).squeeze()
    scores = np.concatenate([pos_scores, neg_scores])
    labels = np.hstack([np.ones(len(pos_scores)), np.zeros(len(neg_scores))])
    fpr, tpr, _ = metrics.roc_curve(labels, scores, pos_label=1)
    auc = metrics.auc(fpr, tpr)
    return auc

