import scipy.sparse as ssp
import scipy.io as sio
import numpy as np
import pandas as pd
import random
import math
def get_big_network(association,M=None,D=None):
    r, c = np.shape(association)
    if not M:
        M = np.zeros((r, r))
    if not D:
        D = np.zeros((c, c))
    return np.vstack((np.hstack((M, association)),np.hstack((association.T,D))))
if __name__ == '__main__':

    '''
        获取HMDD3.0的矩阵形式
    '''
    HMDD3 = pd.read_excel("alldata.xlsx",header = 0)[['mir','disease']].values
    miRNA_list = [] # 1208个
    for miR in HMDD3[:,0]:
        if miR not in miRNA_list:
            miRNA_list.append(miR)
    miRNA_list.sort()
    disease_list = []   # 894个
    for dise in HMDD3[:,1]:
        if dise not in disease_list:
            disease_list.append(dise)
    disease_list.sort()
    print(miRNA_list)
    np.savetxt("HMDD3_miRNA_list.txt", miRNA_list, fmt="%s")
    np.savetxt("HMDD3_disease_list.txt", disease_list, fmt="%s")
    print(disease_list)
    # res = pd.DataFrame(data= np.zeros((1208, 894)), index= miRNA_list, columns= disease_list)
    # for (miR, dise) in HMDD3:
    #     res.loc[miR][dise] = 1
    # np.savetxt("association.txt", res)

    # HMDD3 = np.loadtxt("association.txt", dtype=int)

    '''
        获取HMDD3.0的稀疏矩阵形式，并以mat格式保存
    '''
    # data = ssp.csc_matrix(HMDD3)
    # sio.savemat("HMDD3_association.mat", {'net': data})

    '''
        获得HMDD3.0中的为0的值
    '''
    # mir_n , dis_n = HMDD3.shape
    # HMDD3 = get_big_network(HMDD3)
    # neg_idx = []
    # for i in range(mir_n):
    #     for j in range(mir_n,HMDD3.shape[0]):
    #         if HMDD3[i][j] == 0:
    #             neg_idx.append([i,j])
    # neg_idx = np.array(neg_idx)
    # np.savetxt("./HMDD3.0_neg_idx.txt", neg_idx, fmt="%d")
    # print(neg_idx)