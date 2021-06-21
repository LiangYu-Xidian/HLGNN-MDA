Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: E:\study\code\scholar\MDA-SEAL\Python\data\data.py ========
>>> disAttr = pd.read_csv("./data/disease_gene.csv",header = 0,index_col=0)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    disAttr = pd.read_csv("./data/disease_gene.csv",header = 0,index_col=0)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'./data/disease_gene.csv' does not exist
>>> disAttr = pd.read_csv("disease_gene.csv",header = 0,index_col=0)
>>> miRAttr = pd.read_csv("./data/miRNA_gene.csv",header = 0,index_col=0)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    miRAttr = pd.read_csv("./data/miRNA_gene.csv",header = 0,index_col=0)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 678, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 440, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 787, in __init__
    self._make_engine(self.engine)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 1014, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\io\parsers.py", line 1708, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas\_libs\parsers.pyx", line 384, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas\_libs\parsers.pyx", line 695, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: File b'./data/miRNA_gene.csv' does not exist
>>> miRAttr = pd.read_csv("miRNA_gene.csv",header = 0,index_col=0)
>>> dis
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dis
NameError: name 'dis' is not defined
>>> disAttr
          abortion, habitual              ...                waldenstrom macroglobulinemia
AARS                0.000560              ...                                     0.000676
AARS2               0.000567              ...                                     0.000580
ABCA1               0.000555              ...                                     0.000493
ABCB5               0.000563              ...                                     0.000659
ABCB7               0.000557              ...                                     0.000773
ABCD4               0.000560              ...                                     0.000527
ABCF1               0.000557              ...                                     0.000726
ABI2                0.000554              ...                                     0.000563
ABL1                0.000550              ...                                     0.000461
ACBD3               0.000552              ...                                     0.000509
ACLY                0.000561              ...                                     0.000565
ACP1                0.000555              ...                                     0.000489
ACSL3               0.000569              ...                                     0.000618
ACTA1               0.000550              ...                                     0.000530
ACTA2               0.000550              ...                                     0.000537
ACTB                0.000550              ...                                     0.000513
ACTC1               0.000551              ...                                     0.000556
ACTN1               0.000557              ...                                     0.000515
ACTN4               0.000549              ...                                     0.000497
ACTR1A              0.000559              ...                                     0.000590
ACVR1B              0.000551              ...                                     0.000555
ADA                 0.000555              ...                                     0.000533
ADAM10              0.000554              ...                                     0.000556
ADAM12              0.000554              ...                                     0.000467
ADAM9               0.000541              ...                                     0.000477
ADAMTS1             0.000542              ...                                     0.000552
ADAMTSL4            0.000554              ...                                     0.000592
ADAR                0.000551              ...                                     0.000617
ADD2                0.000560              ...                                     0.000500
ADIPOR2             0.000552              ...                                     0.000645
...                      ...              ...                                          ...
YAP1                0.000555              ...                                     0.000485
YBX1                0.000551              ...                                     0.000480
YRDC                0.000551              ...                                     0.000622
YTHDC1              0.000557              ...                                     0.000502
YWHAE               0.000551              ...                                     0.000483
YWHAQ               0.000553              ...                                     0.000476
YWHAZ               0.000552              ...                                     0.000480
YY1                 0.000558              ...                                     0.000516
YY1AP1              0.000553              ...                                     0.000537
ZBED1               0.000558              ...                                     0.000474
ZBTB45              0.000556              ...                                     0.000554
ZBTB6               0.000551              ...                                     0.000674
ZC3H11A             0.000559              ...                                     0.000587
ZC3H7B              0.000557              ...                                     0.000518
ZDHHC4              0.000557              ...                                     0.000530
ZEB1                0.000556              ...                                     0.000518
ZEB2                0.000557              ...                                     0.000477
ZFP36               0.000555              ...                                     0.000453
ZFP91               0.000554              ...                                     0.000704
ZFPM2               0.000726              ...                                     0.000531
ZHX1                0.000552              ...                                     0.000469
ZMYND8              0.000550              ...                                     0.000567
ZNF202              0.000555              ...                                     0.000555
ZNF354A             0.000568              ...                                     0.000564
ZNF384              0.000554              ...                                     0.000494
ZNF559              0.000560              ...                                     0.000738
ZNF622              0.000555              ...                                     0.000512
ZNF638              0.000556              ...                                     0.000525
ZNF804A             0.000567              ...                                     0.000557
ZZEF1               0.000555              ...                                     0.000591

[1789 rows x 204 columns]
>>> len(disAttr.columns)
204
>>> len(miRAttr.columns)
243
>>> pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = None)
       0                                   1
0      1                  Abortion, Habitual
1      2  Acquired Immunodeficiency Syndrome
2      3    ACTH-Secreting Pituitary Adenoma
3      4             Acute Coronary Syndrome
4      5                   Acute Lung Injury
5      6                      Adenocarcinoma
6      7                             Adenoma
7      8             Adenoviridae Infections
8      9            Adrenal Cortex Neoplasms
9     10              Adrenocortical Adenoma
10    11            Adrenocortical Carcinoma
11    12                               Aging
12    13               AIDS Dementia Complex
13    14                         Albuminuria
14    15                            Alopecia
15    16                   Alzheimer Disease
16    17                         Amyloidosis
17    18       Amyotrophic Lateral Sclerosis
18    19                 Anemia, Sickle Cell
19    20                    Angina, Unstable
20    21                              Anoxia
21    22           Antiphospholipid Syndrome
22    23                      Anus Neoplasms
23    24                   Anxiety Disorders
24    25          Aortic Aneurysm, Abdominal
25    26           Aortic Aneurysm, Thoracic
26    27          Aortic Valve Insufficiency
27    28               Aortic Valve Stenosis
28    29                Arrhythmias, Cardiac
29    30                           Arthritis
..   ...                                 ...
353  354              Scleroderma, Localized
354  355               Scleroderma, Systemic
355  356                              Sepsis
356  357                     Sezary Syndrome
357  358                       SIV Infection
358  359                  Sjogren's Syndrome
359  360                      Skin Neoplasms
360  361           Small Cell Lung Carcinoma
361  362                Spinal Cord Injuries
362  363                    Stomach Diseases
363  364                   Stomach Neoplasms
364  365                  Stomach Neoplasms 
365  366                              Stroke
366  367     Supranuclear Palsy, Progressive
367  368                            Synapses
368  369                Testicular Neoplasms
369  370                   Thyroid Neoplasms
370  371                    Tongue Neoplasms
371  372                   Tourette Syndrome
372  373                          Toxoplasma
373  374                       Toxoplasmosis
374  375                        Trophoblasts
375  376             Tuberculosis, Pulmonary
376  377           Urinary Bladder Neoplasms
377  378          Uterine Cervical Neoplasms
378  379              Vascular Calcification
379  380                   Vascular Diseases
380  381                            Vitiligo
381  382       Waldenstrom Macroglobulinemia
382  383                 Wounds and Injuries

[383 rows x 2 columns]
>>> pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = None,index_col = 0)
                                      1
0                                      
1                    Abortion, Habitual
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[383 rows x 1 columns]
>>> pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = 0,index_col = 0)
                     Abortion, Habitual
1                                      
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
31                 Arthritis, Psoriatic
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[382 rows x 1 columns]
>>> pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = 0,index_col = 0)
                     Abortion, Habitual
1                                      
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
31                 Arthritis, Psoriatic
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[382 rows x 1 columns]
>>> pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = None,index_col = 0)'
SyntaxError: EOL while scanning string literal
>>> pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = None,index_col = 0)
                                      1
0                                      
1                    Abortion, Habitual
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[383 rows x 1 columns]
>>> dieasea_index = pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = None,index_col = 0)
>>> disease_index= pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = None,index_col = 0)
>>> disease_index[0]
Traceback (most recent call last):
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 958, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 964, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    disease_index[0]
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\frame.py", line 2688, in __getitem__
    return self._getitem_column(key)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\frame.py", line 2695, in _getitem_column
    return self._get_item_cache(key)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\generic.py", line 2489, in _get_item_cache
    values = self._data.get(item)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\internals.py", line 4115, in get
    loc = self.items.get_loc(item)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 958, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 964, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 0
>>> disease_index
                                      1
0                                      
1                    Abortion, Habitual
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[383 rows x 1 columns]
>>> disease_index.iloc[0]
1    Abortion, Habitual
Name: 1, dtype: object
>>> dieasea_index.reset_index(drop=True, inplace=True)
>>> disease_index
                                      1
0                                      
1                    Abortion, Habitual
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[383 rows x 1 columns]
>>> disease_index.ix[0]

Warning (from warnings module):
  File "E:\study\code\scholar\MDA-SEAL\Python\data\data.py", line 1
    import scipy.sparse as ssp
DeprecationWarning: 
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

See the documentation here:
http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
Traceback (most recent call last):
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\indexes\base.py", line 3078, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 958, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 964, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 0

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    disease_index.ix[0]
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\indexing.py", line 122, in __getitem__
    return self._getitem_axis(key, axis=axis)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\indexing.py", line 1116, in _getitem_axis
    return self._get_label(key, axis=axis)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\indexing.py", line 140, in _get_label
    return self.obj._xs(label, axis=axis)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\generic.py", line 2987, in xs
    loc = self.index.get_loc(key)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 140, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 958, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 964, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 0
>>> disease_index.ix[1]
1    Abortion, Habitual
Name: 1, dtype: object
>>> disease_index.ix[2]
1    Acquired Immunodeficiency Syndrome
Name: 2, dtype: object
>>> disease_index.reset_index(drop=True)
                                      1
0                    Abortion, Habitual
1    Acquired Immunodeficiency Syndrome
2      ACTH-Secreting Pituitary Adenoma
3               Acute Coronary Syndrome
4                     Acute Lung Injury
5                        Adenocarcinoma
6                               Adenoma
7               Adenoviridae Infections
8              Adrenal Cortex Neoplasms
9                Adrenocortical Adenoma
10             Adrenocortical Carcinoma
11                                Aging
12                AIDS Dementia Complex
13                          Albuminuria
14                             Alopecia
15                    Alzheimer Disease
16                          Amyloidosis
17        Amyotrophic Lateral Sclerosis
18                  Anemia, Sickle Cell
19                     Angina, Unstable
20                               Anoxia
21            Antiphospholipid Syndrome
22                       Anus Neoplasms
23                    Anxiety Disorders
24           Aortic Aneurysm, Abdominal
25            Aortic Aneurysm, Thoracic
26           Aortic Valve Insufficiency
27                Aortic Valve Stenosis
28                 Arrhythmias, Cardiac
29                            Arthritis
..                                  ...
353              Scleroderma, Localized
354               Scleroderma, Systemic
355                              Sepsis
356                     Sezary Syndrome
357                       SIV Infection
358                  Sjogren's Syndrome
359                      Skin Neoplasms
360           Small Cell Lung Carcinoma
361                Spinal Cord Injuries
362                    Stomach Diseases
363                   Stomach Neoplasms
364                  Stomach Neoplasms 
365                              Stroke
366     Supranuclear Palsy, Progressive
367                            Synapses
368                Testicular Neoplasms
369                   Thyroid Neoplasms
370                    Tongue Neoplasms
371                   Tourette Syndrome
372                          Toxoplasma
373                       Toxoplasmosis
374                        Trophoblasts
375             Tuberculosis, Pulmonary
376           Urinary Bladder Neoplasms
377          Uterine Cervical Neoplasms
378              Vascular Calcification
379                   Vascular Diseases
380                            Vitiligo
381       Waldenstrom Macroglobulinemia
382                 Wounds and Injuries

[383 rows x 1 columns]
>>> disease_index
                                      1
0                                      
1                    Abortion, Habitual
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[383 rows x 1 columns]
>>> disease_index = disease_index.reset_index(drop=True)
>>> miRNA_index = pd.read_excel("./5430dataset/1.miRNA-disease associations/miRNA_index.xlsx",header = None,index_col = 0)
>>> miRNA_index
                1
0                
1    hsa-mir-125a
2    hsa-mir-196a
3    hsa-mir-499a
4     hsa-mir-198
5     hsa-mir-29a
6     hsa-mir-29b
7      hsa-let-7a
8     hsa-mir-141
9     hsa-mir-143
10    hsa-mir-145
11    hsa-mir-150
12    hsa-mir-15a
13     hsa-mir-16
14     hsa-mir-21
15      hsa-mir-1
16   hsa-mir-133a
17   hsa-mir-133b
18   hsa-mir-146a
19    hsa-mir-155
20   hsa-mir-208b
21   hsa-mir-103a
22   hsa-mir-106a
23    hsa-mir-10b
24    hsa-mir-126
25   hsa-mir-135a
26   hsa-mir-151a
27    hsa-mir-152
28     hsa-mir-17
29   hsa-mir-181b
30    hsa-mir-182
..            ...
466  hsa-mir-548a
467  hsa-mir-1256
468  hsa-mir-1296
469   hsa-mir-521
470   hsa-mir-616
471  hsa-mir-642b
472   hsa-mir-647
473  hsa-mir-1266
474  hsa-mir-1183
475  hsa-mir-1909
476  hsa-mir-1293
477  hsa-mir-1228
478  hsa-mir-449c
479  hsa-mir-518f
480   hsa-mir-524
481  hsa-mir-551a
482   hsa-mir-570
483   hsa-mir-577
484   hsa-mir-591
485   hsa-mir-595
486   hsa-mir-605
487   hsa-mir-610
488   hsa-mir-938
489   hsa-mir-189
490  hsa-mir-3179
491  hsa-mir-550b
492  hsa-mir-1227
493  hsa-mir-1229
494   hsa-mir-944
495  hsa-mir-518a

[495 rows x 1 columns]
>>> miRNA_index = miRNA_index.reset_index(drop = True)
>>> disAttr.reindex(columns = disease_index)
          (Abortion, Habitual,)           ...            (Wounds and Injuries,)
AARS                        NaN           ...                               NaN
AARS2                       NaN           ...                               NaN
ABCA1                       NaN           ...                               NaN
ABCB5                       NaN           ...                               NaN
ABCB7                       NaN           ...                               NaN
ABCD4                       NaN           ...                               NaN
ABCF1                       NaN           ...                               NaN
ABI2                        NaN           ...                               NaN
ABL1                        NaN           ...                               NaN
ACBD3                       NaN           ...                               NaN
ACLY                        NaN           ...                               NaN
ACP1                        NaN           ...                               NaN
ACSL3                       NaN           ...                               NaN
ACTA1                       NaN           ...                               NaN
ACTA2                       NaN           ...                               NaN
ACTB                        NaN           ...                               NaN
ACTC1                       NaN           ...                               NaN
ACTN1                       NaN           ...                               NaN
ACTN4                       NaN           ...                               NaN
ACTR1A                      NaN           ...                               NaN
ACVR1B                      NaN           ...                               NaN
ADA                         NaN           ...                               NaN
ADAM10                      NaN           ...                               NaN
ADAM12                      NaN           ...                               NaN
ADAM9                       NaN           ...                               NaN
ADAMTS1                     NaN           ...                               NaN
ADAMTSL4                    NaN           ...                               NaN
ADAR                        NaN           ...                               NaN
ADD2                        NaN           ...                               NaN
ADIPOR2                     NaN           ...                               NaN
...                         ...           ...                               ...
YAP1                        NaN           ...                               NaN
YBX1                        NaN           ...                               NaN
YRDC                        NaN           ...                               NaN
YTHDC1                      NaN           ...                               NaN
YWHAE                       NaN           ...                               NaN
YWHAQ                       NaN           ...                               NaN
YWHAZ                       NaN           ...                               NaN
YY1                         NaN           ...                               NaN
YY1AP1                      NaN           ...                               NaN
ZBED1                       NaN           ...                               NaN
ZBTB45                      NaN           ...                               NaN
ZBTB6                       NaN           ...                               NaN
ZC3H11A                     NaN           ...                               NaN
ZC3H7B                      NaN           ...                               NaN
ZDHHC4                      NaN           ...                               NaN
ZEB1                        NaN           ...                               NaN
ZEB2                        NaN           ...                               NaN
ZFP36                       NaN           ...                               NaN
ZFP91                       NaN           ...                               NaN
ZFPM2                       NaN           ...                               NaN
ZHX1                        NaN           ...                               NaN
ZMYND8                      NaN           ...                               NaN
ZNF202                      NaN           ...                               NaN
ZNF354A                     NaN           ...                               NaN
ZNF384                      NaN           ...                               NaN
ZNF559                      NaN           ...                               NaN
ZNF622                      NaN           ...                               NaN
ZNF638                      NaN           ...                               NaN
ZNF804A                     NaN           ...                               NaN
ZZEF1                       NaN           ...                               NaN

[1789 rows x 383 columns]
>>> disAttr
          abortion, habitual              ...                waldenstrom macroglobulinemia
AARS                0.000560              ...                                     0.000676
AARS2               0.000567              ...                                     0.000580
ABCA1               0.000555              ...                                     0.000493
ABCB5               0.000563              ...                                     0.000659
ABCB7               0.000557              ...                                     0.000773
ABCD4               0.000560              ...                                     0.000527
ABCF1               0.000557              ...                                     0.000726
ABI2                0.000554              ...                                     0.000563
ABL1                0.000550              ...                                     0.000461
ACBD3               0.000552              ...                                     0.000509
ACLY                0.000561              ...                                     0.000565
ACP1                0.000555              ...                                     0.000489
ACSL3               0.000569              ...                                     0.000618
ACTA1               0.000550              ...                                     0.000530
ACTA2               0.000550              ...                                     0.000537
ACTB                0.000550              ...                                     0.000513
ACTC1               0.000551              ...                                     0.000556
ACTN1               0.000557              ...                                     0.000515
ACTN4               0.000549              ...                                     0.000497
ACTR1A              0.000559              ...                                     0.000590
ACVR1B              0.000551              ...                                     0.000555
ADA                 0.000555              ...                                     0.000533
ADAM10              0.000554              ...                                     0.000556
ADAM12              0.000554              ...                                     0.000467
ADAM9               0.000541              ...                                     0.000477
ADAMTS1             0.000542              ...                                     0.000552
ADAMTSL4            0.000554              ...                                     0.000592
ADAR                0.000551              ...                                     0.000617
ADD2                0.000560              ...                                     0.000500
ADIPOR2             0.000552              ...                                     0.000645
...                      ...              ...                                          ...
YAP1                0.000555              ...                                     0.000485
YBX1                0.000551              ...                                     0.000480
YRDC                0.000551              ...                                     0.000622
YTHDC1              0.000557              ...                                     0.000502
YWHAE               0.000551              ...                                     0.000483
YWHAQ               0.000553              ...                                     0.000476
YWHAZ               0.000552              ...                                     0.000480
YY1                 0.000558              ...                                     0.000516
YY1AP1              0.000553              ...                                     0.000537
ZBED1               0.000558              ...                                     0.000474
ZBTB45              0.000556              ...                                     0.000554
ZBTB6               0.000551              ...                                     0.000674
ZC3H11A             0.000559              ...                                     0.000587
ZC3H7B              0.000557              ...                                     0.000518
ZDHHC4              0.000557              ...                                     0.000530
ZEB1                0.000556              ...                                     0.000518
ZEB2                0.000557              ...                                     0.000477
ZFP36               0.000555              ...                                     0.000453
ZFP91               0.000554              ...                                     0.000704
ZFPM2               0.000726              ...                                     0.000531
ZHX1                0.000552              ...                                     0.000469
ZMYND8              0.000550              ...                                     0.000567
ZNF202              0.000555              ...                                     0.000555
ZNF354A             0.000568              ...                                     0.000564
ZNF384              0.000554              ...                                     0.000494
ZNF559              0.000560              ...                                     0.000738
ZNF622              0.000555              ...                                     0.000512
ZNF638              0.000556              ...                                     0.000525
ZNF804A             0.000567              ...                                     0.000557
ZZEF1               0.000555              ...                                     0.000591

[1789 rows x 204 columns]
>>> disAttr.columns
Index(['abortion, habitual', 'acquired immunodeficiency syndrome',
       'acth-secreting pituitary adenoma', 'acute coronary syndrome',
       'acute lung injury', 'adenocarcinoma', 'adenoma',
       'adrenocortical carcinoma', 'albuminuria', 'alopecia',
       ...
       'skin neoplasms', 'stomach diseases', 'stomach neoplasms',
       'testicular neoplasms', 'tongue neoplasms', 'tuberculosis, pulmonary',
       'vascular calcification', 'vascular diseases', 'vitiligo',
       'waldenstrom macroglobulinemia'],
      dtype='object', length=204)
>>> disease_index
                                      1
0                    Abortion, Habitual
1    Acquired Immunodeficiency Syndrome
2      ACTH-Secreting Pituitary Adenoma
3               Acute Coronary Syndrome
4                     Acute Lung Injury
5                        Adenocarcinoma
6                               Adenoma
7               Adenoviridae Infections
8              Adrenal Cortex Neoplasms
9                Adrenocortical Adenoma
10             Adrenocortical Carcinoma
11                                Aging
12                AIDS Dementia Complex
13                          Albuminuria
14                             Alopecia
15                    Alzheimer Disease
16                          Amyloidosis
17        Amyotrophic Lateral Sclerosis
18                  Anemia, Sickle Cell
19                     Angina, Unstable
20                               Anoxia
21            Antiphospholipid Syndrome
22                       Anus Neoplasms
23                    Anxiety Disorders
24           Aortic Aneurysm, Abdominal
25            Aortic Aneurysm, Thoracic
26           Aortic Valve Insufficiency
27                Aortic Valve Stenosis
28                 Arrhythmias, Cardiac
29                            Arthritis
..                                  ...
353              Scleroderma, Localized
354               Scleroderma, Systemic
355                              Sepsis
356                     Sezary Syndrome
357                       SIV Infection
358                  Sjogren's Syndrome
359                      Skin Neoplasms
360           Small Cell Lung Carcinoma
361                Spinal Cord Injuries
362                    Stomach Diseases
363                   Stomach Neoplasms
364                  Stomach Neoplasms 
365                              Stroke
366     Supranuclear Palsy, Progressive
367                            Synapses
368                Testicular Neoplasms
369                   Thyroid Neoplasms
370                    Tongue Neoplasms
371                   Tourette Syndrome
372                          Toxoplasma
373                       Toxoplasmosis
374                        Trophoblasts
375             Tuberculosis, Pulmonary
376           Urinary Bladder Neoplasms
377          Uterine Cervical Neoplasms
378              Vascular Calcification
379                   Vascular Diseases
380                            Vitiligo
381       Waldenstrom Macroglobulinemia
382                 Wounds and Injuries

[383 rows x 1 columns]
>>> for i in disease_index:
	i

	
1
>>> for i in disease_index[1]:
	i

	
'Abortion, Habitual'
'Acquired Immunodeficiency Syndrome'
'ACTH-Secreting Pituitary Adenoma'
'Acute Coronary Syndrome'
'Acute Lung Injury'
'Adenocarcinoma'
'Adenoma'
'Adenoviridae Infections'
'Adrenal Cortex Neoplasms'
'Adrenocortical Adenoma'
'Adrenocortical Carcinoma'
'Aging'
'AIDS Dementia Complex'
'Albuminuria'
'Alopecia'
'Alzheimer Disease'
'Amyloidosis'
'Amyotrophic Lateral Sclerosis'
'Anemia, Sickle Cell'
'Angina, Unstable'
'Anoxia'
'Antiphospholipid Syndrome'
'Anus Neoplasms'
'Anxiety Disorders'
'Aortic Aneurysm, Abdominal'
'Aortic Aneurysm, Thoracic'
'Aortic Valve Insufficiency'
'Aortic Valve Stenosis'
'Arrhythmias, Cardiac'
'Arthritis'
'Arthritis, Psoriatic'
'Arthritis, Rheumatoid'
'Asthma'
'Astrocytoma'
'Atherosclerosis'
'Atrial Fibrillation'
'Atrophy'
'Autistic Disorder'
'Autoimmune Diseases'
'Azoospermia'
'Barrett Esophagus'
'Behcet Syndrome'
'Biliary Atresia'
'Biliary Tract Neoplasms'
'Bladder Neoplasms'
'Brain Injuries'
'Brain Injury'
'Brain Ischemia'
'Brain Neoplasms'
'Breast Neoplasms'
'Burkitt Lymphoma'
'Burns'
'Carcinoma'
'Carcinoma, Basal Cell'
'Carcinoma, Ductal, Breast'
'Carcinoma, Ehrlich Tumor'
'Carcinoma, Embryonal'
'Carcinoma, Endometrioid'
'Carcinoma, Hepatocellular'
'Carcinoma, Neuroendocrine'
'Carcinoma, Non-Small-Cell Lung'
'Carcinoma, Oral'
'Carcinoma, Renal Cell'
'Carcinoma, Small Cell'
'Carcinoma, Squamous Cell'
'Cardiomegaly'
'Cardiomyopathies'
'Cardiomyopathy, Dilated'
'Cardiomyopathy, Hypertrophic'
'Cardiovascular Diseases'
'Carotid Artery Diseases'
'Cataract'
'Central Nervous System Diseases'
'Cerebellar Neoplasms'
'Cerebral Hemorrhage'
'Cerebral Infarction'
'Cerebral Ischemia'
'Cervical Intraepithelial Neoplasia'
'Cervical Neoplasms'
'Child Development Disorders, Pervasive'
'Chlamydia Infections'
'Cholangiocarcinoma'
'Cholesteatoma'
'Chondrodysplasia Punctata'
'Chordoma'
'Choriocarcinoma'
'Cicatrix'
'Cocaine-Related Disorders'
'Colitis'
'Colitis, Ulcerative'
'Colon Neoplasms'
'Colonic Neoplasms'
'Colorectal Neoplasms'
'Colorectal Neoplasms, Hereditary Nonpolyposis'
'Coronary Artery Disease'
'Creutzfeldt-Jakob Syndrome'
'Crohn Disease'
'Cryptosporidium'
'Cystic Fibrosis'
'Cystitis, Interstitial'
'Dementia'
'Demyelinating Diseases'
'Dermatitis, Atopic'
'Diabetes Complications'
'Diabetes Mellitus'
'Diabetes Mellitus, Type 1'
'Diabetes Mellitus, Type 2'
'Diabetic Nephropathies'
'Diabetic Retinopathy'
'Digestive System Neoplasms'
'Distal Myopathies'
'Down Syndrome'
'Drug-Induced Liver Injury'
'Dyslipidemias'
'Dyspepsia'
'Eclampsia'
'Eczema'
'Encephalomyelitis, Autoimmune, Experimental'
'Endometrial Neoplasms'
'Endometriosis'
'Endomyocardial Fibrosis'
'Endothelium, Vascular'
'Eosinophilic Esophagitis'
'Ependymoma'
'Erythropoiesis'
'Esophageal Neoplasms'
'Esophagus'
'Eye Abnormalities'
'Fanconi Anemia''Fatty Liver'
'Fatty Liver, Alcoholic'
'Fatty Liver, Non-Alcoholic'
'Fibroblasts'
'Fibrosarcoma'
'Fibrosis'
'Focal Epithelial Hyperplasia'
'Fragile X Syndrome'
'Francisella'
'Frontotemporal Lobar Degeneration'
'Gastric Neoplasms'
'Gastritis, Atrophic'
'Gastrointestinal Neoplasms'
'Gerstmann-Straussler-Scheinker Disease'
'Giant Cell Tumors'
'Glioblastoma'
'Glioblastoma '
'Glioma'
'Glomerulonephritis'
'Glomerulonephritis, IGA'
'Gout'
'Graft vs Host Disease'
'Granulosa Cell Tumor'
'Graves Disease'
'Hamartoma Syndrome, Multiple'
'Hand, Foot and Mouth Disease'
'HBV Infection'
'HCMV Infection'
'HCV'
'Head and Neck Neoplasms'
'Hearing Loss'
'Heart Defects, Congenital'
'Heart Diseases'
'Heart Failure'
'Helplessness, Learned'
'Hemangioma'
'Hemangiosarcoma'
'Hematologic Neoplasms'
'Hepatitis'
'Hepatitis B'
'Hepatitis B, Chronic'
'Hepatitis C'
'Hepatitis C, Chronic'
'Hepatitis, Chronic'
'Hepatoblastoma'
'HEV'
'HIV'
'HIV Infection'
'HIV Infections'
'HIV-1'
'Hodgkin Disease'
'HPV Infection'
'Huntington Disease'
'Hyperglycemia'
'Hyperlipidemias'
'Hypertension'
'Hypertrophy'
'Hypertrophy, Left Ventricular'
'Hypopharyngeal Neoplasms'
'Hypoxia-Ischemia, Brain'
'Infertility, Male'
'Inflammation'
'Inflammatory Bowel Diseases'
'Influenza, Human'
'Intellectual Disability'
'Intervertebral Disk'
'Intracranial Aneurysm'
'Irritable Bowel Syndrome'
'Ischemia'
'Ischemic Preconditioning'
'Keloid'
'Keratoconus'
'Kidney Diseases'
Traceback (most recent call last):
  File "<pyshell#38>", line 2, in <module>
    i
KeyboardInterrupt
>>> for i in range(len(disease_index[1])):
	disease_index[1][i]

	
'Abortion, Habitual'
'Acquired Immunodeficiency Syndrome'
'ACTH-Secreting Pituitary Adenoma'
'Acute Coronary Syndrome'
'Acute Lung Injury'
'Adenocarcinoma'
'Adenoma'
'Adenoviridae Infections'
'Adrenal Cortex Neoplasms'
'Adrenocortical Adenoma'
'Adrenocortical Carcinoma'
'Aging'
'AIDS Dementia Complex'
'Albuminuria'
'Alopecia'
'Alzheimer Disease'
'Amyloidosis'
'Amyotrophic Lateral Sclerosis'
'Anemia, Sickle Cell'
'Angina, Unstable'
'Anoxia'
'Antiphospholipid Syndrome'
'Anus Neoplasms'
'Anxiety Disorders'
'Aortic Aneurysm, Abdominal'
'Aortic Aneurysm, Thoracic'
'Aortic Valve Insufficiency'
'Aortic Valve Stenosis'
'Arrhythmias, Cardiac'
'Arthritis'
'Arthritis, Psoriatic'
'Arthritis, Rheumatoid'
'Asthma'
'Astrocytoma'
'Atherosclerosis'
'Atrial Fibrillation'
'Atrophy'
'Autistic Disorder'
'Autoimmune Diseases'
'Azoospermia'
'Barrett Esophagus'
'Behcet Syndrome'
'Biliary Atresia'
'Biliary Tract Neoplasms'
'Bladder Neoplasms'
'Brain Injuries'
'Brain Injury'
'Brain Ischemia'
'Brain Neoplasms'
'Breast Neoplasms'
'Burkitt Lymphoma'
'Burns'
'Carcinoma'
'Carcinoma, Basal Cell'
'Carcinoma, Ductal, Breast'
'Carcinoma, Ehrlich Tumor'
'Carcinoma, Embryonal'
'Carcinoma, Endometrioid'
'Carcinoma, Hepatocellular'
'Carcinoma, Neuroendocrine'
'Carcinoma, Non-Small-Cell Lung'
'Carcinoma, Oral'
'Carcinoma, Renal Cell'
'Carcinoma, Small Cell'
'Carcinoma, Squamous Cell''Cardiomegaly'
'Cardiomyopathies'
'Cardiomyopathy, Dilated'
'Cardiomyopathy, Hypertrophic'
'Cardiovascular Diseases'
'Carotid Artery Diseases'
'Cataract'
'Central Nervous System Diseases'
'Cerebellar Neoplasms'
'Cerebral Hemorrhage'
'Cerebral Infarction'
'Cerebral Ischemia'
'Cervical Intraepithelial Neoplasia'
'Cervical Neoplasms'
'Child Development Disorders, Pervasive'
'Chlamydia Infections'
'Cholangiocarcinoma'
'Cholesteatoma'
'Chondrodysplasia Punctata'
'Chordoma'
'Choriocarcinoma'
'Cicatrix'
'Cocaine-Related Disorders'
'Colitis'
'Colitis, Ulcerative'
'Colon Neoplasms'
'Colonic Neoplasms'
'Colorectal Neoplasms'
'Colorectal Neoplasms, Hereditary Nonpolyposis'
'Coronary Artery Disease'
'Creutzfeldt-Jakob Syndrome'
'Crohn Disease'
'Cryptosporidium'
'Cystic Fibrosis'
'Cystitis, Interstitial'
'Dementia'
'Demyelinating Diseases'
'Dermatitis, Atopic'
'Diabetes Complications'
'Diabetes Mellitus'
'Diabetes Mellitus, Type 1'
'Diabetes Mellitus, Type 2'
'Diabetic Nephropathies'
'Diabetic Retinopathy'
'Digestive System Neoplasms'
'Distal Myopathies'
'Down Syndrome'
'Drug-Induced Liver Injury'
'Dyslipidemias'
'Dyspepsia'
'Eclampsia'
'Eczema'
'Encephalomyelitis, Autoimmune, Experimental'
'Endometrial Neoplasms'
'Endometriosis'
'Endomyocardial Fibrosis'
'Endothelium, Vascular'
'Eosinophilic Esophagitis'
'Ependymoma'
'Erythropoiesis'
'Esophageal Neoplasms'
'Esophagus'
'Eye Abnormalities'
'Fanconi Anemia'
'Fatty Liver'
'Fatty Liver, Alcoholic'
'Fatty Liver, Non-Alcoholic'
'Fibroblasts'
'Fibrosarcoma'
Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    disease_index[1][i]
KeyboardInterrupt
>>> for i in range(len(disease_index[1])):
	lower(disease_index[1][i])

	
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    lower(disease_index[1][i])
NameError: name 'lower' is not defined
>>> for i in range(len(disease_index[1])):
	disease_index[1][i].lower

	
<built-in method lower of str object at 0x00DB0560>
<built-in method lower of str object at 0x00DA46A0>
<built-in method lower of str object at 0x00DA4560>
<built-in method lower of str object at 0x00D5F9B0>
<built-in method lower of str object at 0x00D5F4D0>
<built-in method lower of str object at 0x00D768E0>
<built-in method lower of str object at 0x00D7F060>
<built-in method lower of str object at 0x00D5FBC0>
<built-in method lower of str object at 0x00D94058>
<built-in method lower of str object at 0x00D5FF50>
<built-in method lower of str object at 0x00D94090>
<built-in method lower of str object at 0x00D7FA20>
<built-in method lower of str object at 0x00D5F6E0>
<built-in method lower of str object at 0x00D76EF8>
<built-in method lower of str object at 0x00D76ED0>
<built-in method lower of str object at 0x00D5FD70>
<built-in method lower of str object at 0x00D76610>
<built-in method lower of str object at 0x00D940C8>
<built-in method lower of str object at 0x00D5FB60>
<built-in method lower of str object at 0x00D5FEC0>
<built-in method lower of str object at 0x00D7FE80>
<built-in method lower of str object at 0x00D94100>
<built-in method lower of str object at 0x00D766B0>
<built-in method lower of str object at 0x00D5F740>
<built-in method lower of str object at 0x00D94138>
<built-in method lower of str object at 0x00D94170>
<built-in method lower of str object at 0x00D941A8>
<built-in method lower of str object at 0x00D5F800>
<built-in method lower of str object at 0x00D5FAD0>
<built-in method lower of str object at 0x00DAA228>
<built-in method lower of str object at 0x00D5FF20>
<built-in method lower of str object at 0x00D41DD0>
<built-in method lower of str object at 0x00D7F940>
<built-in method lower of str object at 0x00DAAC28>
<built-in method lower of str object at 0x00D72ED0>
<built-in method lower of str object at 0x00D41A10>
<built-in method lower of str object at 0x00D7F840>
<built-in method lower of str object at 0x00D41EC0>
<built-in method lower of str object at 0x00D41860>
<built-in method lower of str object at 0x00D72548>
<built-in method lower of str object at 0x00D41350>
<built-in method lower of str object at 0x00D72570>
<built-in method lower of str object at 0x00D72598>
<built-in method lower of str object at 0x00D41D40>
<built-in method lower of str object at 0x00D41560>
<built-in method lower of str object at 0x00D725C0>
<built-in method lower of str object at 0x00D725E8>
<built-in method lower of str object at 0x00D72610>
<built-in method lower of str object at 0x00D72EA8>
<built-in method lower of str object at 0x00D411D0>
<built-in method lower of str object at 0x00D410B0>
<built-in method lower of str object at 0x00D7FE00>
<built-in method lower of str object at 0x00D72E80>
<built-in method lower of str object at 0x00D41620>
<built-in method lower of str object at 0x00D941E0>
<built-in method lower of str object at 0x00D94218>
<built-in method lower of str object at 0x00D82260>
<built-in method lower of str object at 0x00D82440>
<built-in method lower of str object at 0x00D94250>
<built-in method lower of str object at 0x00D94288>
<built-in method lower of str object at 0x00D942C0>
<built-in method lower of str object at 0x00D72638>
<built-in method lower of str object at 0x00D82140>
<built-in method lower of str object at 0x00D82E00>
<built-in method lower of str object at 0x00D942F8>
<built-in method lower of str object at 0x00D726B0>
<built-in method lower of str object at 0x00D82530>
<built-in method lower of str object at 0x00D823B0>
<built-in method lower of str object at 0x00D94330>
<built-in method lower of str object at 0x00D82800>
<built-in method lower of str object at 0x00D82830>
<built-in method lower of str object at 0x00DA94D0>
<built-in method lower of str object at 0x00D94368>
<built-in method lower of str object at 0x00D82620>
<built-in method lower of str object at 0x00D822F0>
<built-in method lower of str object at 0x00D9F290>
<built-in method lower of str object at 0x00D9F770>
<built-in method lower of str object at 0x00DA4720>
<built-in method lower of str object at 0x00D9F7D0>
<built-in method lower of str object at 0x00DA4760>
<built-in method lower of str object at 0x00D9F6E0>
<built-in method lower of str object at 0x00D9F6B0>
<built-in method lower of str object at 0x00DA9930>
<built-in method lower of str object at 0x00D943A0>
<built-in method lower of str object at 0x00DA95E8>
<built-in method lower of str object at 0x00DA9D40>
<built-in method lower of str object at 0x00DA9868>
<built-in method lower of str object at 0x00D943D8>
<built-in method lower of str object at 0x00DAD720>
<built-in method lower of str object at 0x00D9F860>
<built-in method lower of str object at 0x00DA9458>
<built-in method lower of str object at 0x00D9F3E0>
<built-in method lower of str object at 0x00D9FE30>
<built-in method lower of str object at 0x00CE6188>
<built-in method lower of str object at 0x00D6C590>
<built-in method lower of str object at 0x00D94410>
<built-in method lower of str object at 0x00DA9E58>
<built-in method lower of str object at 0x00DA9F20>
<built-in method lower of str object at 0x00DA9EF8>
<built-in method lower of str object at 0x00D6C980>
<built-in method lower of str object at 0x00DA99F8>
<built-in method lower of str object at 0x00D6CB30>
<built-in method lower of str object at 0x00D6C380>
<built-in method lower of str object at 0x00D6C650>
<built-in method lower of str object at 0x00D6C440>
<built-in method lower of str object at 0x00D94448>
<built-in method lower of str object at 0x00D94480><built-in method lower of str object at 0x00D6C950>
<built-in method lower of str object at 0x00D6C110>
<built-in method lower of str object at 0x00D944B8>
<built-in method lower of str object at 0x00D8C500>
<built-in method lower of str object at 0x00DA99D0>
<built-in method lower of str object at 0x00D944F0>
<built-in method lower of str object at 0x00DA9B10>
<built-in method lower of str object at 0x00DA9AC0>
<built-in method lower of str object at 0x00DA9A48>
<built-in method lower of str object at 0x00DADC20>
<built-in method lower of str object at 0x00CE6140>
<built-in method lower of str object at 0x00D8CB30>
<built-in method lower of str object at 0x00DA9DB8>
<built-in method lower of str object at 0x00D8CB90>
<built-in method lower of str object at 0x00D8C050>
<built-in method lower of str object at 0x00D94528>
<built-in method lower of str object at 0x00DA9980>
<built-in method lower of str object at 0x00DA9390>
<built-in method lower of str object at 0x00D8C770>
<built-in method lower of str object at 0x00DA9A20>
<built-in method lower of str object at 0x00D8C260>
<built-in method lower of str object at 0x00DA9ED0>
<built-in method lower of str object at 0x00DA9B60>
<built-in method lower of str object at 0x00D48C80>
<built-in method lower of str object at 0x00D94560>
<built-in method lower of str object at 0x00DA9A70>
<built-in method lower of str object at 0x00DA9520>
<built-in method lower of str object at 0x00DA9DE0>
<built-in method lower of str object at 0x00D94598>
<built-in method lower of str object at 0x00D48AA0>
<built-in method lower of str object at 0x00DA9638>
<built-in method lower of str object at 0x00DA47E0>
<built-in method lower of str object at 0x00D48650>
<built-in method lower of str object at 0x00D482F0>
<built-in method lower of str object at 0x00D945D0>
<built-in method lower of str object at 0x00DA4820>
<built-in method lower of str object at 0x00D489B0>
<built-in method lower of str object at 0x00DA9660>
<built-in method lower of str object at 0x00DA9818>
<built-in method lower of str object at 0x00DADFA0>
<built-in method lower of str object at 0x00D48920>
<built-in method lower of str object at 0x00D481A0>
<built-in method lower of str object at 0x00DADAA0>
<built-in method lower of str object at 0x00D48620>
<built-in method lower of str object at 0x00D48440>
<built-in method lower of str object at 0x00DA96B0>
<built-in method lower of str object at 0x00D94608>
<built-in method lower of str object at 0x00D94640>
<built-in method lower of str object at 0x00DA9F48>
<built-in method lower of str object at 0x00DA9F70>
<built-in method lower of str object at 0x00D98800>
<built-in method lower of str object at 0x00D49830>
<built-in method lower of str object at 0x00DA9F98>
<built-in method lower of str object at 0x00D94678>
<built-in method lower of str object at 0x00DA9FC0>
<built-in method lower of str object at 0x00DA95C0>
<built-in method lower of str object at 0x00D494D0>
<built-in method lower of str object at 0x00DA9D90>
<built-in method lower of str object at 0x00DA9908>
<built-in method lower of str object at 0x00D49F80>
<built-in method lower of str object at 0x00DA9CC8>
<built-in method lower of str object at 0x00DA92C8>
<built-in method lower of str object at 0x00D49AD0>
<built-in method lower of str object at 0x00DA92F0>
<built-in method lower of str object at 0x00D49500>
<built-in method lower of str object at 0x00D49350>
<built-in method lower of str object at 0x00DA93E0>
<built-in method lower of str object at 0x00D98300>
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    disease_index[1][i].lower
KeyboardInterrupt
>>> for i in range(len(disease_index[1])):
	disease_index[1][i].lower()

	
'abortion, habitual'
'acquired immunodeficiency syndrome'
'acth-secreting pituitary adenoma'
'acute coronary syndrome'
'acute lung injury'
'adenocarcinoma'
'adenoma'
'adenoviridae infections'
'adrenal cortex neoplasms'
'adrenocortical adenoma'
'adrenocortical carcinoma'
'aging'
'aids dementia complex'
'albuminuria'
'alopecia'
'alzheimer disease'
'amyloidosis'
'amyotrophic lateral sclerosis'
'anemia, sickle cell'
'angina, unstable'
'anoxia'
'antiphospholipid syndrome'
'anus neoplasms'
'anxiety disorders'
'aortic aneurysm, abdominal'
'aortic aneurysm, thoracic'
'aortic valve insufficiency'
'aortic valve stenosis'
'arrhythmias, cardiac'
'arthritis'
'arthritis, psoriatic'
'arthritis, rheumatoid'
'asthma'
'astrocytoma'
'atherosclerosis'
'atrial fibrillation'
'atrophy'
'autistic disorder'
'autoimmune diseases'
'azoospermia'
'barrett esophagus'
'behcet syndrome'
'biliary atresia'
'biliary tract neoplasms'
'bladder neoplasms'
'brain injuries'
'brain injury'
'brain ischemia'
'brain neoplasms'
'breast neoplasms'
'burkitt lymphoma'
'burns'
'carcinoma'
'carcinoma, basal cell'
'carcinoma, ductal, breast'
'carcinoma, ehrlich tumor'
'carcinoma, embryonal'
'carcinoma, endometrioid'
'carcinoma, hepatocellular'
'carcinoma, neuroendocrine'
'carcinoma, non-small-cell lung'

'carcinoma, renal cell'
'carcinoma, small cell'
'carcinoma, squamous cell'
'cardiomegaly'
'cardiomyopathies'
'cardiomyopathy, dilated'
'cardiomyopathy, hypertrophic'
'cardiovascular diseases'
'carotid artery diseases'
'cataract'
'central nervous system diseases'
'cerebellar neoplasms'
'cerebral hemorrhage'
'cerebral infarction'
'cerebral ischemia'
'cervical intraepithelial neoplasia'
'cervical neoplasms'
'child development disorders, pervasive'
'chlamydia infections'
'cholangiocarcinoma'
'cholesteatoma'
'chondrodysplasia punctata'
'chordoma'
'choriocarcinoma'
'cicatrix'
'cocaine-related disorders'
'colitis'
'colitis, ulcerative'
'colon neoplasms'
'colonic neoplasms'
'colorectal neoplasms'
'colorectal neoplasms, hereditary nonpolyposis'
'coronary artery disease'
'creutzfeldt-jakob syndrome'
'crohn disease'
'cryptosporidium'
'cystic fibrosis'
'cystitis, interstitial'
'dementia'
'demyelinating diseases'
'dermatitis, atopic'
'diabetes complications'
'diabetes mellitus'
'diabetes mellitus, type 1'
'diabetes mellitus, type 2'
'diabetic nephropathies'
'diabetic retinopathy'
'digestive system neoplasms'
'distal myopathies'
'down syndrome'Traceback (most recent call last):
  File "<pyshell#46>", line 2, in <module>
    disease_index[1][i].lower()
KeyboardInterrupt
>>> for i in range(len(disease_index[1])):
	disease_index[1][i] = disease_index[1][i].lower()

	
>>> disease_index
                                      1
0                    abortion, habitual
1    acquired immunodeficiency syndrome
2      acth-secreting pituitary adenoma
3               acute coronary syndrome
4                     acute lung injury
5                        adenocarcinoma
6                               adenoma
7               adenoviridae infections
8              adrenal cortex neoplasms
9                adrenocortical adenoma
10             adrenocortical carcinoma
11                                aging
12                aids dementia complex
13                          albuminuria
14                             alopecia
15                    alzheimer disease
16                          amyloidosis
17        amyotrophic lateral sclerosis
18                  anemia, sickle cell
19                     angina, unstable
20                               anoxia
21            antiphospholipid syndrome
22                       anus neoplasms
23                    anxiety disorders
24           aortic aneurysm, abdominal
25            aortic aneurysm, thoracic
26           aortic valve insufficiency
27                aortic valve stenosis
28                 arrhythmias, cardiac
29                            arthritis
..                                  ...
353              scleroderma, localized
354               scleroderma, systemic
355                              sepsis
356                     sezary syndrome
357                       siv infection
358                  sjogren's syndrome
359                      skin neoplasms
360           small cell lung carcinoma
361                spinal cord injuries
362                    stomach diseases
363                   stomach neoplasms
364                  stomach neoplasms 
365                              stroke
366     supranuclear palsy, progressive
367                            synapses
368                testicular neoplasms
369                   thyroid neoplasms
370                    tongue neoplasms
371                   tourette syndrome
372                          toxoplasma
373                       toxoplasmosis
374                        trophoblasts
375             tuberculosis, pulmonary
376           urinary bladder neoplasms
377          uterine cervical neoplasms
378              vascular calcification
379                   vascular diseases
380                            vitiligo
381       waldenstrom macroglobulinemia
382                 wounds and injuries

[383 rows x 1 columns]
>>> disAttr.reindex(columns = disease_index)
          (abortion, habitual,)           ...            (wounds and injuries,)
AARS                        NaN           ...                               NaN
AARS2                       NaN           ...                               NaN
ABCA1                       NaN           ...                               NaN
ABCB5                       NaN           ...                               NaN
ABCB7                       NaN           ...                               NaN
ABCD4                       NaN           ...                               NaN
ABCF1                       NaN           ...                               NaN
ABI2                        NaN           ...                               NaN
ABL1                        NaN           ...                               NaN
ACBD3                       NaN           ...                               NaN
ACLY                        NaN           ...                               NaN
ACP1                        NaN           ...                               NaN
ACSL3                       NaN           ...                               NaN
ACTA1                       NaN           ...                               NaN
ACTA2                       NaN           ...                               NaN
ACTB                        NaN           ...                               NaN
ACTC1                       NaN           ...                               NaN
ACTN1                       NaN           ...                               NaN
ACTN4                       NaN           ...                               NaN
ACTR1A                      NaN           ...                               NaN
ACVR1B                      NaN           ...                               NaN
ADA                         NaN           ...                               NaN
ADAM10                      NaN           ...                               NaN
ADAM12                      NaN           ...                               NaN
ADAM9                       NaN           ...                               NaN
ADAMTS1                     NaN           ...                               NaN
ADAMTSL4                    NaN           ...                               NaN
ADAR                        NaN           ...                               NaN
ADD2                        NaN           ...                               NaN
ADIPOR2                     NaN           ...                               NaN
...                         ...           ...                               ...
YAP1                        NaN           ...                               NaN
YBX1                        NaN           ...                               NaN
YRDC                        NaN           ...                               NaN
YTHDC1                      NaN           ...                               NaN
YWHAE                       NaN           ...                               NaN
YWHAQ                       NaN           ...                               NaN
YWHAZ                       NaN           ...                               NaN
YY1                         NaN           ...                               NaN
YY1AP1                      NaN           ...                               NaN
ZBED1                       NaN           ...                               NaN
ZBTB45                      NaN           ...                               NaN
ZBTB6                       NaN           ...                               NaN
ZC3H11A                     NaN           ...                               NaN
ZC3H7B                      NaN           ...                               NaN
ZDHHC4                      NaN           ...                               NaN
ZEB1                        NaN           ...                               NaN
ZEB2                        NaN           ...                               NaN
ZFP36                       NaN           ...                               NaN
ZFP91                       NaN           ...                               NaN
ZFPM2                       NaN           ...                               NaN
ZHX1                        NaN           ...                               NaN
ZMYND8                      NaN           ...                               NaN
ZNF202                      NaN           ...                               NaN
ZNF354A                     NaN           ...                               NaN
ZNF384                      NaN           ...                               NaN
ZNF559                      NaN           ...                               NaN
ZNF622                      NaN           ...                               NaN
ZNF638                      NaN           ...                               NaN
ZNF804A                     NaN           ...                               NaN
ZZEF1                       NaN           ...                               NaN

[1789 rows x 383 columns]
>>> disAttr.columns
Index(['abortion, habitual', 'acquired immunodeficiency syndrome',
       'acth-secreting pituitary adenoma', 'acute coronary syndrome',
       'acute lung injury', 'adenocarcinoma', 'adenoma',
       'adrenocortical carcinoma', 'albuminuria', 'alopecia',
       ...
       'skin neoplasms', 'stomach diseases', 'stomach neoplasms',
       'testicular neoplasms', 'tongue neoplasms', 'tuberculosis, pulmonary',
       'vascular calcification', 'vascular diseases', 'vitiligo',
       'waldenstrom macroglobulinemia'],
      dtype='object', length=204)
>>> for i in range(len(disease_index[1])):
	disease_index[1][i] = disease_index[1][i].lower()[:-1]

	
>>> disAttr.columns
Index(['abortion, habitual', 'acquired immunodeficiency syndrome',
       'acth-secreting pituitary adenoma', 'acute coronary syndrome',
       'acute lung injury', 'adenocarcinoma', 'adenoma',
       'adrenocortical carcinoma', 'albuminuria', 'alopecia',
       ...
       'skin neoplasms', 'stomach diseases', 'stomach neoplasms',
       'testicular neoplasms', 'tongue neoplasms', 'tuberculosis, pulmonary',
       'vascular calcification', 'vascular diseases', 'vitiligo',
       'waldenstrom macroglobulinemia'],
      dtype='object', length=204)
>>> disease_index
                                     1
0                    abortion, habitua
1    acquired immunodeficiency syndrom
2      acth-secreting pituitary adenom
3               acute coronary syndrom
4                     acute lung injur
5                        adenocarcinom
6                               adenom
7               adenoviridae infection
8              adrenal cortex neoplasm
9                adrenocortical adenom
10             adrenocortical carcinom
11                                agin
12                aids dementia comple
13                          albuminuri
14                             alopeci
15                    alzheimer diseas
16                          amyloidosi
17        amyotrophic lateral sclerosi
18                  anemia, sickle cel
19                     angina, unstabl
20                               anoxi
21            antiphospholipid syndrom
22                       anus neoplasm
23                    anxiety disorder
24           aortic aneurysm, abdomina
25            aortic aneurysm, thoraci
26           aortic valve insufficienc
27                aortic valve stenosi
28                 arrhythmias, cardia
29                            arthriti
..                                 ...
353              scleroderma, localize
354               scleroderma, systemi
355                              sepsi
356                     sezary syndrom
357                       siv infectio
358                  sjogren's syndrom
359                      skin neoplasm
360           small cell lung carcinom
361                spinal cord injurie
362                    stomach disease
363                   stomach neoplasm
364                  stomach neoplasms
365                              strok
366     supranuclear palsy, progressiv
367                            synapse
368                testicular neoplasm
369                   thyroid neoplasm
370                    tongue neoplasm
371                   tourette syndrom
372                          toxoplasm
373                       toxoplasmosi
374                        trophoblast
375             tuberculosis, pulmonar
376           urinary bladder neoplasm
377          uterine cervical neoplasm
378              vascular calcificatio
379                   vascular disease
380                            vitilig
381       waldenstrom macroglobulinemi
382                 wounds and injurie

[383 rows x 1 columns]
>>> disAttr.reindex(columns = disease_index)
          (abortion, habitua,)          ...            (wounds and injurie,)
AARS                       NaN          ...                              NaN
AARS2                      NaN          ...                              NaN
ABCA1                      NaN          ...                              NaN
ABCB5                      NaN          ...                              NaN
ABCB7                      NaN          ...                              NaN
ABCD4                      NaN          ...                              NaN
ABCF1                      NaN          ...                              NaN
ABI2                       NaN          ...                              NaN
ABL1                       NaN          ...                              NaN
ACBD3                      NaN          ...                              NaN
ACLY                       NaN          ...                              NaN
ACP1                       NaN          ...                              NaN
ACSL3                      NaN          ...                              NaN
ACTA1                      NaN          ...                              NaN
ACTA2                      NaN          ...                              NaN
ACTB                       NaN          ...                              NaN
ACTC1                      NaN          ...                              NaN
ACTN1                      NaN          ...                              NaN
ACTN4                      NaN          ...                              NaN
ACTR1A                     NaN          ...                              NaN
ACVR1B                     NaN          ...                              NaN
ADA                        NaN          ...                              NaN
ADAM10                     NaN          ...                              NaN
ADAM12                     NaN          ...                              NaN
ADAM9                      NaN          ...                              NaN
ADAMTS1                    NaN          ...                              NaN
ADAMTSL4                   NaN          ...                              NaN
ADAR                       NaN          ...                              NaN
ADD2                       NaN          ...                              NaN
ADIPOR2                    NaN          ...                              NaN
...                        ...          ...                              ...
YAP1                       NaN          ...                              NaN
YBX1                       NaN          ...                              NaN
YRDC                       NaN          ...                              NaN
YTHDC1                     NaN          ...                              NaN
YWHAE                      NaN          ...                              NaN
YWHAQ                      NaN          ...                              NaN
YWHAZ                      NaN          ...                              NaN
YY1                        NaN          ...                              NaN
YY1AP1                     NaN          ...                              NaN
ZBED1                      NaN          ...                              NaN
ZBTB45                     NaN          ...                              NaN
ZBTB6                      NaN          ...                              NaN
ZC3H11A                    NaN          ...                              NaN
ZC3H7B                     NaN          ...                              NaN
ZDHHC4                     NaN          ...                              NaN
ZEB1                       NaN          ...                              NaN
ZEB2                       NaN          ...                              NaN
ZFP36                      NaN          ...                              NaN
ZFP91                      NaN          ...                              NaN
ZFPM2                      NaN          ...                              NaN
ZHX1                       NaN          ...                              NaN
ZMYND8                     NaN          ...                              NaN
ZNF202                     NaN          ...                              NaN
ZNF354A                    NaN          ...                              NaN
ZNF384                     NaN          ...                              NaN
ZNF559                     NaN          ...                              NaN
ZNF622                     NaN          ...                              NaN
ZNF638                     NaN          ...                              NaN
ZNF804A                    NaN          ...                              NaN
ZZEF1                      NaN          ...                              NaN

[1789 rows x 383 columns]
>>> for i in range(len(disease_index[1])):
	disease_index[1][i] = disease_index[1][i].lower()[:-1]

	
>>> disease_index
                                    1
0                    abortion, habitu
1    acquired immunodeficiency syndro
2      acth-secreting pituitary adeno
3               acute coronary syndro
4                     acute lung inju
5                        adenocarcino
6                               adeno
7               adenoviridae infectio
8              adrenal cortex neoplas
9                adrenocortical adeno
10             adrenocortical carcino
11                                agi
12                aids dementia compl
13                          albuminur
14                             alopec
15                    alzheimer disea
16                          amyloidos
17        amyotrophic lateral scleros
18                  anemia, sickle ce
19                     angina, unstab
20                               anox
21            antiphospholipid syndro
22                       anus neoplas
23                    anxiety disorde
24           aortic aneurysm, abdomin
25            aortic aneurysm, thorac
26           aortic valve insufficien
27                aortic valve stenos
28                 arrhythmias, cardi
29                            arthrit
..                                ...
353              scleroderma, localiz
354               scleroderma, system
355                              seps
356                     sezary syndro
357                       siv infecti
358                  sjogren's syndro
359                      skin neoplas
360           small cell lung carcino
361                spinal cord injuri
362                    stomach diseas
363                   stomach neoplas
364                  stomach neoplasm
365                              stro
366     supranuclear palsy, progressi
367                            synaps
368                testicular neoplas
369                   thyroid neoplas
370                    tongue neoplas
371                   tourette syndro
372                          toxoplas
373                       toxoplasmos
374                        trophoblas
375             tuberculosis, pulmona
376           urinary bladder neoplas
377          uterine cervical neoplas
378              vascular calcificati
379                   vascular diseas
380                            vitili
381       waldenstrom macroglobulinem
382                 wounds and injuri

[383 rows x 1 columns]
>>> disease_index= pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = None,index_col = 0)
>>> dieasea_index.reset_index(drop=True, inplace=True)
>>> disease_index
                                      1
0                                      
1                    Abortion, Habitual
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[383 rows x 1 columns]
>>> disease_index = dieasea_index.reset_index(drop=True, inplace=True)
>>> disease_index
>>> disease_index= pd.read_excel("./5430dataset/1.miRNA-disease associations/disease_index.xlsx",header = None,index_col = 0)
>>> disease_index
                                      1
0                                      
1                    Abortion, Habitual
2    Acquired Immunodeficiency Syndrome
3      ACTH-Secreting Pituitary Adenoma
4               Acute Coronary Syndrome
5                     Acute Lung Injury
6                        Adenocarcinoma
7                               Adenoma
8               Adenoviridae Infections
9              Adrenal Cortex Neoplasms
10               Adrenocortical Adenoma
11             Adrenocortical Carcinoma
12                                Aging
13                AIDS Dementia Complex
14                          Albuminuria
15                             Alopecia
16                    Alzheimer Disease
17                          Amyloidosis
18        Amyotrophic Lateral Sclerosis
19                  Anemia, Sickle Cell
20                     Angina, Unstable
21                               Anoxia
22            Antiphospholipid Syndrome
23                       Anus Neoplasms
24                    Anxiety Disorders
25           Aortic Aneurysm, Abdominal
26            Aortic Aneurysm, Thoracic
27           Aortic Valve Insufficiency
28                Aortic Valve Stenosis
29                 Arrhythmias, Cardiac
30                            Arthritis
..                                  ...
354              Scleroderma, Localized
355               Scleroderma, Systemic
356                              Sepsis
357                     Sezary Syndrome
358                       SIV Infection
359                  Sjogren's Syndrome
360                      Skin Neoplasms
361           Small Cell Lung Carcinoma
362                Spinal Cord Injuries
363                    Stomach Diseases
364                   Stomach Neoplasms
365                  Stomach Neoplasms 
366                              Stroke
367     Supranuclear Palsy, Progressive
368                            Synapses
369                Testicular Neoplasms
370                   Thyroid Neoplasms
371                    Tongue Neoplasms
372                   Tourette Syndrome
373                          Toxoplasma
374                       Toxoplasmosis
375                        Trophoblasts
376             Tuberculosis, Pulmonary
377           Urinary Bladder Neoplasms
378          Uterine Cervical Neoplasms
379              Vascular Calcification
380                   Vascular Diseases
381                            Vitiligo
382       Waldenstrom Macroglobulinemia
383                 Wounds and Injuries

[383 rows x 1 columns]
>>> disease_index = dieasea_index.reset_index(drop=True)
>>> disease_index
                                      1
0                    Abortion, Habitual
1    Acquired Immunodeficiency Syndrome
2      ACTH-Secreting Pituitary Adenoma
3               Acute Coronary Syndrome
4                     Acute Lung Injury
5                        Adenocarcinoma
6                               Adenoma
7               Adenoviridae Infections
8              Adrenal Cortex Neoplasms
9                Adrenocortical Adenoma
10             Adrenocortical Carcinoma
11                                Aging
12                AIDS Dementia Complex
13                          Albuminuria
14                             Alopecia
15                    Alzheimer Disease
16                          Amyloidosis
17        Amyotrophic Lateral Sclerosis
18                  Anemia, Sickle Cell
19                     Angina, Unstable
20                               Anoxia
21            Antiphospholipid Syndrome
22                       Anus Neoplasms
23                    Anxiety Disorders
24           Aortic Aneurysm, Abdominal
25            Aortic Aneurysm, Thoracic
26           Aortic Valve Insufficiency
27                Aortic Valve Stenosis
28                 Arrhythmias, Cardiac
29                            Arthritis
..                                  ...
353              Scleroderma, Localized
354               Scleroderma, Systemic
355                              Sepsis
356                     Sezary Syndrome
357                       SIV Infection
358                  Sjogren's Syndrome
359                      Skin Neoplasms
360           Small Cell Lung Carcinoma
361                Spinal Cord Injuries
362                    Stomach Diseases
363                   Stomach Neoplasms
364                  Stomach Neoplasms 
365                              Stroke
366     Supranuclear Palsy, Progressive
367                            Synapses
368                Testicular Neoplasms
369                   Thyroid Neoplasms
370                    Tongue Neoplasms
371                   Tourette Syndrome
372                          Toxoplasma
373                       Toxoplasmosis
374                        Trophoblasts
375             Tuberculosis, Pulmonary
376           Urinary Bladder Neoplasms
377          Uterine Cervical Neoplasms
378              Vascular Calcification
379                   Vascular Diseases
380                            Vitiligo
381       Waldenstrom Macroglobulinemia
382                 Wounds and Injuries

[383 rows x 1 columns]
>>> for i in range(len(disease_index[1])):
	disease_index[1][i] = disease_index[1][i].lower()

	
>>> disease_index
                                      1
0                    abortion, habitual
1    acquired immunodeficiency syndrome
2      acth-secreting pituitary adenoma
3               acute coronary syndrome
4                     acute lung injury
5                        adenocarcinoma
6                               adenoma
7               adenoviridae infections
8              adrenal cortex neoplasms
9                adrenocortical adenoma
10             adrenocortical carcinoma
11                                aging
12                aids dementia complex
13                          albuminuria
14                             alopecia
15                    alzheimer disease
16                          amyloidosis
17        amyotrophic lateral sclerosis
18                  anemia, sickle cell
19                     angina, unstable
20                               anoxia
21            antiphospholipid syndrome
22                       anus neoplasms
23                    anxiety disorders
24           aortic aneurysm, abdominal
25            aortic aneurysm, thoracic
26           aortic valve insufficiency
27                aortic valve stenosis
28                 arrhythmias, cardiac
29                            arthritis
..                                  ...
353              scleroderma, localized
354               scleroderma, systemic
355                              sepsis
356                     sezary syndrome
357                       siv infection
358                  sjogren's syndrome
359                      skin neoplasms
360           small cell lung carcinoma
361                spinal cord injuries
362                    stomach diseases
363                   stomach neoplasms
364                  stomach neoplasms 
365                              stroke
366     supranuclear palsy, progressive
367                            synapses
368                testicular neoplasms
369                   thyroid neoplasms
370                    tongue neoplasms
371                   tourette syndrome
372                          toxoplasma
373                       toxoplasmosis
374                        trophoblasts
375             tuberculosis, pulmonary
376           urinary bladder neoplasms
377          uterine cervical neoplasms
378              vascular calcification
379                   vascular diseases
380                            vitiligo
381       waldenstrom macroglobulinemia
382                 wounds and injuries

[383 rows x 1 columns]
>>> disAttr.reindex(columns = disease_index)
          (abortion, habitual,)           ...            (wounds and injuries,)
AARS                        NaN           ...                               NaN
AARS2                       NaN           ...                               NaN
ABCA1                       NaN           ...                               NaN
ABCB5                       NaN           ...                               NaN
ABCB7                       NaN           ...                               NaN
ABCD4                       NaN           ...                               NaN
ABCF1                       NaN           ...                               NaN
ABI2                        NaN           ...                               NaN
ABL1                        NaN           ...                               NaN
ACBD3                       NaN           ...                               NaN
ACLY                        NaN           ...                               NaN
ACP1                        NaN           ...                               NaN
ACSL3                       NaN           ...                               NaN
ACTA1                       NaN           ...                               NaN
ACTA2                       NaN           ...                               NaN
ACTB                        NaN           ...                               NaN
ACTC1                       NaN           ...                               NaN
ACTN1                       NaN           ...                               NaN
ACTN4                       NaN           ...                               NaN
ACTR1A                      NaN           ...                               NaN
ACVR1B                      NaN           ...                               NaN
ADA                         NaN           ...                               NaN
ADAM10                      NaN           ...                               NaN
ADAM12                      NaN           ...                               NaN
ADAM9                       NaN           ...                               NaN
ADAMTS1                     NaN           ...                               NaN
ADAMTSL4                    NaN           ...                               NaN
ADAR                        NaN           ...                               NaN
ADD2                        NaN           ...                               NaN
ADIPOR2                     NaN           ...                               NaN
...                         ...           ...                               ...
YAP1                        NaN           ...                               NaN
YBX1                        NaN           ...                               NaN
YRDC                        NaN           ...                               NaN
YTHDC1                      NaN           ...                               NaN
YWHAE                       NaN           ...                               NaN
YWHAQ                       NaN           ...                               NaN
YWHAZ                       NaN           ...                               NaN
YY1                         NaN           ...                               NaN
YY1AP1                      NaN           ...                               NaN
ZBED1                       NaN           ...                               NaN
ZBTB45                      NaN           ...                               NaN
ZBTB6                       NaN           ...                               NaN
ZC3H11A                     NaN           ...                               NaN
ZC3H7B                      NaN           ...                               NaN
ZDHHC4                      NaN           ...                               NaN
ZEB1                        NaN           ...                               NaN
ZEB2                        NaN           ...                               NaN
ZFP36                       NaN           ...                               NaN
ZFP91                       NaN           ...                               NaN
ZFPM2                       NaN           ...                               NaN
ZHX1                        NaN           ...                               NaN
ZMYND8                      NaN           ...                               NaN
ZNF202                      NaN           ...                               NaN
ZNF354A                     NaN           ...                               NaN
ZNF384                      NaN           ...                               NaN
ZNF559                      NaN           ...                               NaN
ZNF622                      NaN           ...                               NaN
ZNF638                      NaN           ...                               NaN
ZNF804A                     NaN           ...                               NaN
ZZEF1                       NaN           ...                               NaN

[1789 rows x 383 columns]
>>> disAttr
          abortion, habitual              ...                waldenstrom macroglobulinemia
AARS                0.000560              ...                                     0.000676
AARS2               0.000567              ...                                     0.000580
ABCA1               0.000555              ...                                     0.000493
ABCB5               0.000563              ...                                     0.000659
ABCB7               0.000557              ...                                     0.000773
ABCD4               0.000560              ...                                     0.000527
ABCF1               0.000557              ...                                     0.000726
ABI2                0.000554              ...                                     0.000563
ABL1                0.000550              ...                                     0.000461
ACBD3               0.000552              ...                                     0.000509
ACLY                0.000561              ...                                     0.000565
ACP1                0.000555              ...                                     0.000489
ACSL3               0.000569              ...                                     0.000618
ACTA1               0.000550              ...                                     0.000530
ACTA2               0.000550              ...                                     0.000537
ACTB                0.000550              ...                                     0.000513
ACTC1               0.000551              ...                                     0.000556
ACTN1               0.000557              ...                                     0.000515
ACTN4               0.000549              ...                                     0.000497
ACTR1A              0.000559              ...                                     0.000590
ACVR1B              0.000551              ...                                     0.000555
ADA                 0.000555              ...                                     0.000533
ADAM10              0.000554              ...                                     0.000556
ADAM12              0.000554              ...                                     0.000467
ADAM9               0.000541              ...                                     0.000477
ADAMTS1             0.000542              ...                                     0.000552
ADAMTSL4            0.000554              ...                                     0.000592
ADAR                0.000551              ...                                     0.000617
ADD2                0.000560              ...                                     0.000500
ADIPOR2             0.000552              ...                                     0.000645
...                      ...              ...                                          ...
YAP1                0.000555              ...                                     0.000485
YBX1                0.000551              ...                                     0.000480
YRDC                0.000551              ...                                     0.000622
YTHDC1              0.000557              ...                                     0.000502
YWHAE               0.000551              ...                                     0.000483
YWHAQ               0.000553              ...                                     0.000476
YWHAZ               0.000552              ...                                     0.000480
YY1                 0.000558              ...                                     0.000516
YY1AP1              0.000553              ...                                     0.000537
ZBED1               0.000558              ...                                     0.000474
ZBTB45              0.000556              ...                                     0.000554
ZBTB6               0.000551              ...                                     0.000674
ZC3H11A             0.000559              ...                                     0.000587
ZC3H7B              0.000557              ...                                     0.000518
ZDHHC4              0.000557              ...                                     0.000530
ZEB1                0.000556              ...                                     0.000518
ZEB2                0.000557              ...                                     0.000477
ZFP36               0.000555              ...                                     0.000453
ZFP91               0.000554              ...                                     0.000704
ZFPM2               0.000726              ...                                     0.000531
ZHX1                0.000552              ...                                     0.000469
ZMYND8              0.000550              ...                                     0.000567
ZNF202              0.000555              ...                                     0.000555
ZNF354A             0.000568              ...                                     0.000564
ZNF384              0.000554              ...                                     0.000494
ZNF559              0.000560              ...                                     0.000738
ZNF622              0.000555              ...                                     0.000512
ZNF638              0.000556              ...                                     0.000525
ZNF804A             0.000567              ...                                     0.000557
ZZEF1               0.000555              ...                                     0.000591

[1789 rows x 204 columns]
>>> disAttr.reindex(columns = disease_index[1])
1         abortion, habitual         ...           wounds and injuries
AARS                0.000560         ...                           NaN
AARS2               0.000567         ...                           NaN
ABCA1               0.000555         ...                           NaN
ABCB5               0.000563         ...                           NaN
ABCB7               0.000557         ...                           NaN
ABCD4               0.000560         ...                           NaN
ABCF1               0.000557         ...                           NaN
ABI2                0.000554         ...                           NaN
ABL1                0.000550         ...                           NaN
ACBD3               0.000552         ...                           NaN
ACLY                0.000561         ...                           NaN
ACP1                0.000555         ...                           NaN
ACSL3               0.000569         ...                           NaN
ACTA1               0.000550         ...                           NaN
ACTA2               0.000550         ...                           NaN
ACTB                0.000550         ...                           NaN
ACTC1               0.000551         ...                           NaN
ACTN1               0.000557         ...                           NaN
ACTN4               0.000549         ...                           NaN
ACTR1A              0.000559         ...                           NaN
ACVR1B              0.000551         ...                           NaN
ADA                 0.000555         ...                           NaN
ADAM10              0.000554         ...                           NaN
ADAM12              0.000554         ...                           NaN
ADAM9               0.000541         ...                           NaN
ADAMTS1             0.000542         ...                           NaN
ADAMTSL4            0.000554         ...                           NaN
ADAR                0.000551         ...                           NaN
ADD2                0.000560         ...                           NaN
ADIPOR2             0.000552         ...                           NaN
...                      ...         ...                           ...
YAP1                0.000555         ...                           NaN
YBX1                0.000551         ...                           NaN
YRDC                0.000551         ...                           NaN
YTHDC1              0.000557         ...                           NaN
YWHAE               0.000551         ...                           NaN
YWHAQ               0.000553         ...                           NaN
YWHAZ               0.000552         ...                           NaN
YY1                 0.000558         ...                           NaN
YY1AP1              0.000553         ...                           NaN
ZBED1               0.000558         ...                           NaN
ZBTB45              0.000556         ...                           NaN
ZBTB6               0.000551         ...                           NaN
ZC3H11A             0.000559         ...                           NaN
ZC3H7B              0.000557         ...                           NaN
ZDHHC4              0.000557         ...                           NaN
ZEB1                0.000556         ...                           NaN
ZEB2                0.000557         ...                           NaN
ZFP36               0.000555         ...                           NaN
ZFP91               0.000554         ...                           NaN
ZFPM2               0.000726         ...                           NaN
ZHX1                0.000552         ...                           NaN
ZMYND8              0.000550         ...                           NaN
ZNF202              0.000555         ...                           NaN
ZNF354A             0.000568         ...                           NaN
ZNF384              0.000554         ...                           NaN
ZNF559              0.000560         ...                           NaN
ZNF622              0.000555         ...                           NaN
ZNF638              0.000556         ...                           NaN
ZNF804A             0.000567         ...                           NaN
ZZEF1               0.000555         ...                           NaN

[1789 rows x 383 columns]
>>> miRAttr
          hsa-let-7a  hsa-let-7b     ...       hsa-mir-99a  hsa-mir-99b
AARS        0.000427    0.000456     ...          0.000547     0.000494
AARS2       0.000427    0.000456     ...          0.000547     0.000494
ABCA1       0.000492    0.000500     ...          0.000550     0.000532
ABCB5       0.000554    0.000550     ...          0.000564     0.000571
ABCB7       0.000437    0.000455     ...          0.000537     0.000496
ABCD4       0.000427    0.000456     ...          0.000547     0.000494
ABCF1       0.000427    0.000456     ...          0.000547     0.000494
ABI2        0.000515    0.000513     ...          0.000563     0.000559
ABL1        0.000509    0.000499     ...          0.000549     0.000536
ACBD3       0.000894    0.000852     ...          0.000638     0.000815
ACLY        0.000568    0.000549     ...          0.000554     0.000573
ACP1        0.001338    0.001148     ...          0.000592     0.000636
ACSL3       0.000515    0.000513     ...          0.000563     0.000559
ACTA1       0.000554    0.000550     ...          0.000564     0.000571
ACTA2       0.000847    0.000662     ...          0.000560     0.000538
ACTB        0.000401    0.000431     ...          0.000535     0.000474
ACTC1       0.000437    0.000455     ...          0.000537     0.000496
ACTN1       0.000554    0.000550     ...          0.000564     0.000571
ACTN4       0.000437    0.000455     ...          0.000537     0.000496
ACTR1A      0.000644    0.000631     ...          0.000545     0.000543
ACVR1B      0.000533    0.000548     ...          0.000547     0.000536
ADA         0.000568    0.000549     ...          0.000554     0.000573
ADAM10      0.000568    0.000549     ...          0.000554     0.000573
ADAM12      0.000554    0.000550     ...          0.000564     0.000571
ADAM9       0.000507    0.000506     ...          0.000546     0.000525
ADAMTS1     0.000715    0.000701     ...          0.000561     0.000575
ADAMTSL4    0.000554    0.000550     ...          0.000564     0.000571
ADAR        0.000552    0.000548     ...          0.000564     0.000569
ADD2        0.000523    0.000530     ...          0.000548     0.000561
ADIPOR2     0.000471    0.000487     ...          0.000539     0.000507
...              ...         ...     ...               ...          ...
YAP1        0.000515    0.000513     ...          0.000563     0.000559
YBX1        0.000492    0.000517     ...          0.000548     0.000526
YRDC        0.000427    0.000456     ...          0.000547     0.000494
YTHDC1      0.000554    0.000550     ...          0.000564     0.000571
YWHAE       0.000427    0.000456     ...          0.000547     0.000494
YWHAQ       0.000554    0.000550     ...          0.000564     0.000571
YWHAZ       0.000594    0.000572     ...          0.000574     0.000603
YY1         0.000427    0.000456     ...          0.000547     0.000494
YY1AP1      0.000515    0.000513     ...          0.000563     0.000559
ZBED1       0.000515    0.000513     ...          0.000563     0.000559
ZBTB45      0.000427    0.000456     ...          0.000547     0.000494
ZBTB6       0.000554    0.000550     ...          0.000564     0.000571
ZC3H11A     0.000554    0.000550     ...          0.000564     0.000571
ZC3H7B      0.000442    0.000468     ...          0.000543     0.000499
ZDHHC4      0.000523    0.000530     ...          0.000548     0.000561
ZEB1        0.000693    0.000731     ...          0.000569     0.000895
ZEB2        0.000648    0.000682     ...          0.000561     0.000818
ZFP36       0.000651    0.000647     ...          0.000547     0.000537
ZFP91       0.000515    0.000513     ...          0.000563     0.000559
ZFPM2       0.000723    0.000772     ...          0.000566     0.000998
ZHX1        0.000507    0.000506     ...          0.000546     0.000525
ZMYND8      0.000475    0.000491     ...          0.000545     0.000517
ZNF202      0.000427    0.000456     ...          0.000547     0.000494
ZNF354A     0.000427    0.000456     ...          0.000547     0.000494
ZNF384      0.000554    0.000550     ...          0.000564     0.000571
ZNF559      0.000658    0.000640     ...          0.000545     0.000544
ZNF622      0.000554    0.000550     ...          0.000564     0.000571
ZNF638      0.000554    0.000550     ...          0.000564     0.000571
ZNF804A     0.000494    0.000518     ...          0.000548     0.000527
ZZEF1       0.000427    0.000456     ...          0.000547     0.000494

[1789 rows x 243 columns]
>>> miRNA_index
                1
0    hsa-mir-125a
1    hsa-mir-196a
2    hsa-mir-499a
3     hsa-mir-198
4     hsa-mir-29a
5     hsa-mir-29b
6      hsa-let-7a
7     hsa-mir-141
8     hsa-mir-143
9     hsa-mir-145
10    hsa-mir-150
11    hsa-mir-15a
12     hsa-mir-16
13     hsa-mir-21
14      hsa-mir-1
15   hsa-mir-133a
16   hsa-mir-133b
17   hsa-mir-146a
18    hsa-mir-155
19   hsa-mir-208b
20   hsa-mir-103a
21   hsa-mir-106a
22    hsa-mir-10b
23    hsa-mir-126
24   hsa-mir-135a
25   hsa-mir-151a
26    hsa-mir-152
27     hsa-mir-17
28   hsa-mir-181b
29    hsa-mir-182
..            ...
465  hsa-mir-548a
466  hsa-mir-1256
467  hsa-mir-1296
468   hsa-mir-521
469   hsa-mir-616
470  hsa-mir-642b
471   hsa-mir-647
472  hsa-mir-1266
473  hsa-mir-1183
474  hsa-mir-1909
475  hsa-mir-1293
476  hsa-mir-1228
477  hsa-mir-449c
478  hsa-mir-518f
479   hsa-mir-524
480  hsa-mir-551a
481   hsa-mir-570
482   hsa-mir-577
483   hsa-mir-591
484   hsa-mir-595
485   hsa-mir-605
486   hsa-mir-610
487   hsa-mir-938
488   hsa-mir-189
489  hsa-mir-3179
490  hsa-mir-550b
491  hsa-mir-1227
492  hsa-mir-1229
493   hsa-mir-944
494  hsa-mir-518a

[495 rows x 1 columns]
>>> miRAttr.reindex(columns = miRNA_index[1])
1         hsa-mir-125a  hsa-mir-196a      ...       hsa-mir-944  hsa-mir-518a
AARS          0.000449      0.000499      ...               NaN           NaN
AARS2         0.000449      0.000499      ...               NaN           NaN
ABCA1         0.000511      0.000539      ...               NaN           NaN
ABCB5         0.000578      0.000576      ...               NaN           NaN
ABCB7         0.000452      0.000504      ...               NaN           NaN
ABCD4         0.000449      0.000499      ...               NaN           NaN
ABCF1         0.000449      0.000499      ...               NaN           NaN
ABI2          0.000544      0.000563      ...               NaN           NaN
ABL1          0.000512      0.000597      ...               NaN           NaN
ACBD3         0.001010      0.000627      ...               NaN           NaN
ACLY          0.000582      0.000582      ...               NaN           NaN
ACP1          0.000700      0.000637      ...               NaN           NaN
ACSL3         0.000544      0.000563      ...               NaN           NaN
ACTA1         0.000578      0.000576      ...               NaN           NaN
ACTA2         0.000548      0.000560      ...               NaN           NaN
ACTB          0.000418      0.000481      ...               NaN           NaN
ACTC1         0.000452      0.000504      ...               NaN           NaN
ACTN1         0.000578      0.000576      ...               NaN           NaN
ACTN4         0.000452      0.000504      ...               NaN           NaN
ACTR1A        0.000557      0.000546      ...               NaN           NaN
ACVR1B        0.000581      0.000585      ...               NaN           NaN
ADA           0.000582      0.000582      ...               NaN           NaN
ADAM10        0.000582      0.000582      ...               NaN           NaN
ADAM12        0.000578      0.000576      ...               NaN           NaN
ADAM9         0.000508      0.000534      ...               NaN           NaN
ADAMTS1       0.001139      0.000575      ...               NaN           NaN
ADAMTSL4      0.000578      0.000576      ...               NaN           NaN
ADAR          0.000576      0.000574      ...               NaN           NaN
ADD2          0.000545      0.000583      ...               NaN           NaN
ADIPOR2       0.000481      0.000515      ...               NaN           NaN
...                ...           ...      ...               ...           ...
YAP1          0.000544      0.000563      ...               NaN           NaN
YBX1          0.000516      0.000538      ...               NaN           NaN
YRDC          0.000449      0.000499      ...               NaN           NaN
YTHDC1        0.000578      0.000576      ...               NaN           NaN
YWHAE         0.000449      0.000499      ...               NaN           NaN
YWHAQ         0.000578      0.000576      ...               NaN           NaN
YWHAZ         0.000625      0.000607      ...               NaN           NaN
YY1           0.000449      0.000499      ...               NaN           NaN
YY1AP1        0.000544      0.000563      ...               NaN           NaN
ZBED1         0.000544      0.000563      ...               NaN           NaN
ZBTB45        0.000449      0.000499      ...               NaN           NaN
ZBTB6         0.000578      0.000576      ...               NaN           NaN
ZC3H11A       0.000578      0.000576      ...               NaN           NaN
ZC3H7B        0.000461      0.000510      ...               NaN           NaN
ZDHHC4        0.000545      0.000583      ...               NaN           NaN
ZEB1          0.000665      0.000600      ...               NaN           NaN
ZEB2          0.000662      0.000594      ...               NaN           NaN
ZFP36         0.000596      0.000567      ...               NaN           NaN
ZFP91         0.000544      0.000563      ...               NaN           NaN
ZFPM2         0.000625      0.000594      ...               NaN           NaN
ZHX1          0.000508      0.000534      ...               NaN           NaN
ZMYND8        0.000492      0.000531      ...               NaN           NaN
ZNF202        0.000449      0.000499      ...               NaN           NaN
ZNF354A       0.000449      0.000499      ...               NaN           NaN
ZNF384        0.000578      0.000576      ...               NaN           NaN
ZNF559        0.000561      0.000547      ...               NaN           NaN
ZNF622        0.000578      0.000576      ...               NaN           NaN
ZNF638        0.000578      0.000576      ...               NaN           NaN
ZNF804A       0.000517      0.000539      ...               NaN           NaN
ZZEF1         0.000449      0.000499      ...               NaN           NaN

[1789 rows x 495 columns]
>>> disAttr.reindex(columns = disease_index[1]).fullna(0)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    disAttr.reindex(columns = disease_index[1]).fullna(0)
  File "D:\software\codesoftwware\python\lib\site-packages\pandas\core\generic.py", line 4376, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'fullna'
>>> Dattr = disAttr.reindex(columns = disease_index[1])
>>> Dattr
1         abortion, habitual         ...           wounds and injuries
AARS                0.000560         ...                           NaN
AARS2               0.000567         ...                           NaN
ABCA1               0.000555         ...                           NaN
ABCB5               0.000563         ...                           NaN
ABCB7               0.000557         ...                           NaN
ABCD4               0.000560         ...                           NaN
ABCF1               0.000557         ...                           NaN
ABI2                0.000554         ...                           NaN
ABL1                0.000550         ...                           NaN
ACBD3               0.000552         ...                           NaN
ACLY                0.000561         ...                           NaN
ACP1                0.000555         ...                           NaN
ACSL3               0.000569         ...                           NaN
ACTA1               0.000550         ...                           NaN
ACTA2               0.000550         ...                           NaN
ACTB                0.000550         ...                           NaN
ACTC1               0.000551         ...                           NaN
ACTN1               0.000557         ...                           NaN
ACTN4               0.000549         ...                           NaN
ACTR1A              0.000559         ...                           NaN
ACVR1B              0.000551         ...                           NaN
ADA                 0.000555         ...                           NaN
ADAM10              0.000554         ...                           NaN
ADAM12              0.000554         ...                           NaN
ADAM9               0.000541         ...                           NaN
ADAMTS1             0.000542         ...                           NaN
ADAMTSL4            0.000554         ...                           NaN
ADAR                0.000551         ...                           NaN
ADD2                0.000560         ...                           NaN
ADIPOR2             0.000552         ...                           NaN
...                      ...         ...                           ...
YAP1                0.000555         ...                           NaN
YBX1                0.000551         ...                           NaN
YRDC                0.000551         ...                           NaN
YTHDC1              0.000557         ...                           NaN
YWHAE               0.000551         ...                           NaN
YWHAQ               0.000553         ...                           NaN
YWHAZ               0.000552         ...                           NaN
YY1                 0.000558         ...                           NaN
YY1AP1              0.000553         ...                           NaN
ZBED1               0.000558         ...                           NaN
ZBTB45              0.000556         ...                           NaN
ZBTB6               0.000551         ...                           NaN
ZC3H11A             0.000559         ...                           NaN
ZC3H7B              0.000557         ...                           NaN
ZDHHC4              0.000557         ...                           NaN
ZEB1                0.000556         ...                           NaN
ZEB2                0.000557         ...                           NaN
ZFP36               0.000555         ...                           NaN
ZFP91               0.000554         ...                           NaN
ZFPM2               0.000726         ...                           NaN
ZHX1                0.000552         ...                           NaN
ZMYND8              0.000550         ...                           NaN
ZNF202              0.000555         ...                           NaN
ZNF354A             0.000568         ...                           NaN
ZNF384              0.000554         ...                           NaN
ZNF559              0.000560         ...                           NaN
ZNF622              0.000555         ...                           NaN
ZNF638              0.000556         ...                           NaN
ZNF804A             0.000567         ...                           NaN
ZZEF1               0.000555         ...                           NaN

[1789 rows x 383 columns]
>>> Dattr.info(verbose=True, null_counts=True)
<class 'pandas.core.frame.DataFrame'>
Index: 1789 entries, AARS to ZZEF1
Data columns (total 383 columns):
abortion, habitual                                  1789 non-null float64
acquired immunodeficiency syndrome                  1789 non-null float64
acth-secreting pituitary adenoma                    1789 non-null float64
acute coronary syndrome                             1789 non-null float64
acute lung injury                                   1789 non-null float64
adenocarcinoma                                      1789 non-null float64
adenoma                                             1789 non-null float64
adenoviridae infections                             0 non-null float64
adrenal cortex neoplasms                            0 non-null float64
adrenocortical adenoma                              0 non-null float64
adrenocortical carcinoma                            1789 non-null float64
aging                                               0 non-null float64
aids dementia complex                               0 non-null float64
albuminuria                                         1789 non-null float64
alopecia                                            1789 non-null float64
alzheimer disease                                   0 non-null float64
amyloidosis                                         1789 non-null float64
amyotrophic lateral sclerosis                       0 non-null float64
anemia, sickle cell                                 0 non-null float64
angina, unstable                                    1789 non-null float64
anoxia                                              0 non-null float64
antiphospholipid syndrome                           0 non-null float64
anus neoplasms                                      0 non-null float64
anxiety disorders                                   1789 non-null float64
aortic aneurysm, abdominal                          1789 non-null float64
aortic aneurysm, thoracic                           1789 non-null float64
aortic valve insufficiency                          1789 non-null float64
aortic valve stenosis                               1789 non-null float64
arrhythmias, cardiac                                0 non-null float64
arthritis                                           1789 non-null float64
arthritis, psoriatic                                1789 non-null float64
arthritis, rheumatoid                               0 non-null float64
asthma                                              1789 non-null float64
astrocytoma                                         1789 non-null float64
atherosclerosis                                     1789 non-null float64
atrial fibrillation                                 1789 non-null float64
atrophy                                             0 non-null float64
autistic disorder                                   1789 non-null float64
autoimmune diseases                                 1789 non-null float64
azoospermia                                         1789 non-null float64
barrett esophagus                                   1789 non-null float64
behcet syndrome                                     1789 non-null float64
biliary atresia                                     1789 non-null float64
biliary tract neoplasms                             0 non-null float64
bladder neoplasms                                   0 non-null float64
brain injuries                                      0 non-null float64
brain injury                                        0 non-null float64
brain ischemia                                      1789 non-null float64
brain neoplasms                                     1789 non-null float64
breast neoplasms                                    0 non-null float64
burkitt lymphoma                                    1789 non-null float64
burns                                               0 non-null float64
carcinoma                                           0 non-null float64
carcinoma, basal cell                               0 non-null float64
carcinoma, ductal, breast                           0 non-null float64
carcinoma, ehrlich tumor                            0 non-null float64
carcinoma, embryonal                                0 non-null float64
carcinoma, endometrioid                             1789 non-null float64
carcinoma, hepatocellular                           0 non-null float64
carcinoma, neuroendocrine                           0 non-null float64
carcinoma, non-small-cell lung                      0 non-null float64
carcinoma, oral                                     0 non-null float64
carcinoma, renal cell                               0 non-null float64
carcinoma, small cell                               1789 non-null float64
carcinoma, squamous cell                            0 non-null float64
cardiomegaly                                        1789 non-null float64
cardiomyopathies                                    1789 non-null float64
cardiomyopathy, dilated                             1789 non-null float64
cardiomyopathy, hypertrophic                        0 non-null float64
cardiovascular diseases                             1789 non-null float64
carotid artery diseases                             1789 non-null float64
cataract                                            1789 non-null float64
central nervous system diseases                     0 non-null float64
cerebellar neoplasms                                0 non-null float64
cerebral hemorrhage                                 1789 non-null float64
cerebral infarction                                 1789 non-null float64
cerebral ischemia                                   0 non-null float64
cervical intraepithelial neoplasia                  1789 non-null float64
cervical neoplasms                                  0 non-null float64
child development disorders, pervasive              1789 non-null float64
chlamydia infections                                1789 non-null float64
cholangiocarcinoma                                  1789 non-null float64
cholesteatoma                                       1789 non-null float64
chondrodysplasia punctata                           0 non-null float64
chordoma                                            1789 non-null float64
choriocarcinoma                                     0 non-null float64
cicatrix                                            0 non-null float64
cocaine-related disorders                           1789 non-null float64
colitis                                             1789 non-null float64
colitis, ulcerative                                 0 non-null float64
colon neoplasms                                     0 non-null float64
colonic neoplasms                                   1789 non-null float64
colorectal neoplasms                                1789 non-null float64
colorectal neoplasms, hereditary nonpolyposis       0 non-null float64
coronary artery disease                             1789 non-null float64
creutzfeldt-jakob syndrome                          0 non-null float64
crohn disease                                       1789 non-null float64
cryptosporidium                                     0 non-null float64
cystic fibrosis                                     1789 non-null float64
cystitis, interstitial                              0 non-null float64
dementia                                            1789 non-null float64
demyelinating diseases                              1789 non-null float64
dermatitis, atopic                                  1789 non-null float64
diabetes complications                              0 non-null float64
diabetes mellitus                                   1789 non-null float64
diabetes mellitus, type 1                           0 non-null float64
diabetes mellitus, type 2                           0 non-null float64
diabetic nephropathies                              0 non-null float64
diabetic retinopathy                                1789 non-null float64
digestive system neoplasms                          1789 non-null float64
distal myopathies                                   0 non-null float64
down syndrome                                       1789 non-null float64
drug-induced liver injury                           0 non-null float64
dyslipidemias                                       1789 non-null float64
dyspepsia                                           0 non-null float64
eclampsia                                           0 non-null float64
eczema                                              1789 non-null float64
encephalomyelitis, autoimmune, experimental         0 non-null float64
endometrial neoplasms                               1789 non-null float64
endometriosis                                       1789 non-null float64
endomyocardial fibrosis                             1789 non-null float64
endothelium, vascular                               0 non-null float64
eosinophilic esophagitis                            1789 non-null float64
ependymoma                                          1789 non-null float64
erythropoiesis                                      0 non-null float64
esophageal neoplasms                                1789 non-null float64
esophagus                                           0 non-null float64
eye abnormalities                                   0 non-null float64
fanconi anemia                                      1789 non-null float64
fatty liver                                         1789 non-null float64
fatty liver, alcoholic                              1789 non-null float64
fatty liver, non-alcoholic                          0 non-null float64
fibroblasts                                         0 non-null float64
fibrosarcoma                                        1789 non-null float64
fibrosis                                            1789 non-null float64
focal epithelial hyperplasia                        0 non-null float64
fragile x syndrome                                  1789 non-null float64
francisella                                         0 non-null float64
frontotemporal lobar degeneration                   1789 non-null float64
gastric neoplasms                                   0 non-null float64
gastritis, atrophic                                 1789 non-null float64
gastrointestinal neoplasms                          1789 non-null float64
gerstmann-straussler-scheinker disease              1789 non-null float64
giant cell tumors                                   0 non-null float64
glioblastoma                                        1789 non-null float64
glioblastoma                                        0 non-null float64
glioma                                              1789 non-null float64
glomerulonephritis                                  0 non-null float64
glomerulonephritis, iga                             0 non-null float64
gout                                                1789 non-null float64
graft vs host disease                               0 non-null float64
granulosa cell tumor                                0 non-null float64
graves disease                                      1789 non-null float64
hamartoma syndrome, multiple                        1789 non-null float64
hand, foot and mouth disease                        0 non-null float64
hbv infection                                       0 non-null float64
hcmv infection                                      0 non-null float64
hcv                                                 0 non-null float64
head and neck neoplasms                             1789 non-null float64
hearing loss                                        0 non-null float64
heart defects, congenital                           0 non-null float64
heart diseases                                      1789 non-null float64
heart failure                                       1789 non-null float64
helplessness, learned                               0 non-null float64
hemangioma                                          0 non-null float64
hemangiosarcoma                                     1789 non-null float64
hematologic neoplasms                               1789 non-null float64
hepatitis                                           0 non-null float64
hepatitis b                                         1789 non-null float64
hepatitis b, chronic                                0 non-null float64
hepatitis c                                         1789 non-null float64
hepatitis c, chronic                                0 non-null float64
hepatitis, chronic                                  1789 non-null float64
hepatoblastoma                                      1789 non-null float64
hev                                                 0 non-null float64
hiv                                                 0 non-null float64
hiv infection                                       0 non-null float64
hiv infections                                      1789 non-null float64
hiv-1                                               0 non-null float64
hodgkin disease                                     1789 non-null float64
hpv infection                                       0 non-null float64
huntington disease                                  1789 non-null float64
hyperglycemia                                       1789 non-null float64
hyperlipidemias                                     0 non-null float64
hypertension                                        0 non-null float64
hypertrophy                                         1789 non-null float64
hypertrophy, left ventricular                       0 non-null float64
hypopharyngeal neoplasms                            0 non-null float64
hypoxia-ischemia, brain                             1789 non-null float64
infertility, male                                   0 non-null float64
inflammation                                        1789 non-null float64
inflammatory bowel diseases                         1789 non-null float64
influenza, human                                    0 non-null float64
intellectual disability                             1789 non-null float64
intervertebral disk                                 0 non-null float64
intracranial aneurysm                               1789 non-null float64
irritable bowel syndrome                            1789 non-null float64
ischemia                                            1789 non-null float64
ischemic preconditioning                            0 non-null float64
keloid                                              1789 non-null float64
keratoconus                                         0 non-null float64
kidney diseases                                     1789 non-null float64
kidney failure, acute                               1789 non-null float64
kidney failure, chronic                             1789 non-null float64
kidney neoplasms                                    0 non-null float64
laryngeal neoplasms                                 0 non-null float64
leiomyoma                                           0 non-null float64
leiomyosarcoma                                      0 non-null float64
leprosy                                             1789 non-null float64
leukemia                                            1789 non-null float64
leukemia, acute                                     0 non-null float64
leukemia, b-cell                                    0 non-null float64
leukemia, biphenotypic, acute                       0 non-null float64
leukemia, lymphoblastic, acute                      0 non-null float64
leukemia, lymphoblastic, chronic                    0 non-null float64
leukemia, lymphocytic, chronic, b-cell              0 non-null float64
leukemia, myelogenous, chronic, bcr-abl positive    0 non-null float64
leukemia, myeloid                                   0 non-null float64
leukemia, myeloid, acute                            0 non-null float64
leukemia, myeloid, chronic-phase                    0 non-null float64
leukemia, promyelocytic, acute                      0 non-null float64
leukemia-lymphoma, adult t-cell                     0 non-null float64
leukoplakia, oral                                   0 non-null float64
lichen planus, oral                                 0 non-null float64
lipid metabolism disorders                          0 non-null float64
liposarcoma                                         1789 non-null float64
liver cirrhosis                                     1789 non-null float64
liver cirrhosis, biliary                            0 non-null float64
liver diseases                                      1789 non-null float64
liver diseases, alcoholic                           0 non-null float64
liver failure                                       1789 non-null float64
liver neoplasms                                     1789 non-null float64
long qt syndrome                                    1789 non-null float64
lung diseases                                       1789 non-null float64
lung diseases, interstitial                         1789 non-null float64
lung neoplasms                                      1789 non-null float64
lupus erythematosus, systemic                       1789 non-null float64
lupus nephritis                                     1789 non-null float64
lupus vulgaris                                      0 non-null float64
lymphoma                                            1789 non-null float64
lymphoma, b-cell                                    0 non-null float64
lymphoma, extranodal nk-t-cell                      1789 non-null float64
lymphoma, large b-cell, diffuse                     0 non-null float64
lymphoma, large-cell, anaplastic                    0 non-null float64
lymphoma, mantle-cell                               0 non-null float64
lymphoma, non-hodgkin                               1789 non-null float64
lymphoma, primary effusion                          0 non-null float64
lymphoma, t-cell                                    0 non-null float64
lymphoproliferative disorders                       1789 non-null float64
marek disease                                       0 non-null float64
mastocytosis, systemic                              1789 non-null float64
medulloblastoma                                     1789 non-null float64
melanoma                                            1789 non-null float64
meningioma                                          1789 non-null float64
mesothelioma                                        1789 non-null float64
metabolic diseases                                  1789 non-null float64
mouth neoplasms                                     1789 non-null float64
moyamoya disease                                    1789 non-null float64
multiple endocrine neoplasia type 1                 1789 non-null float64
multiple myeloma                                    1789 non-null float64
multiple sclerosis                                  1789 non-null float64
muscular disorders, atrophic                        0 non-null float64
muscular dystrophies                                0 non-null float64
muscular dystrophy, duchenne                        1789 non-null float64
muscular dystrophy, facioscapulohumeral             1789 non-null float64
musculoskeletal abnormalities                       0 non-null float64
myasthenia gravis                                   0 non-null float64
mycosis fungoides                                   1789 non-null float64
myelodysplastic syndromes                           0 non-null float64
myeloproliferative disorders                        0 non-null float64
myocardial infarction                               1789 non-null float64
myocardial ischemia                                 1789 non-null float64
myocardial reperfusion injury                       1789 non-null float64
myocarditis                                         1789 non-null float64
myocardium                                          0 non-null float64
myocytes, cardiac                                   0 non-null float64
myopia                                              1789 non-null float64
myositis ossificans                                 1789 non-null float64
myotonic dystrophy                                  1789 non-null float64
nasal polyps                                        1789 non-null float64
nasopharyngeal neoplasms                            1789 non-null float64
neoplasms                                           0 non-null float64
neoplasms, germ cell and embryonal                  1789 non-null float64
neoplasms, glandular and epithelial                 1789 non-null float64
neoplasms, squamous cell                            0 non-null float64
nephrosclerosis                                     1789 non-null float64
nerve sheath neoplasms                              0 non-null float64
nervous system diseases                             0 non-null float64
neurilemmoma                                        1789 non-null float64
neuroblastoma                                       1789 non-null float64
neurodegenerative diseases                          0 non-null float64
neurofibromatosis 2                                 1789 non-null float64
neuroma, acoustic                                   0 non-null float64
neutropenia                                         1789 non-null float64
nevus, pigmented                                    0 non-null float64
obesity                                             1789 non-null float64
odontogenic tumors                                  0 non-null float64
oligodendroglioma                                   1789 non-null float64
osteoarthritis                                      0 non-null float64
osteolysis                                          0 non-null float64
osteoporosis                                        1789 non-null float64
osteosarcoma                                        1789 non-null float64
osteosarcoma                                        0 non-null float64
ovarian neoplasms                                   0 non-null float64
ovary syndrome                                      0 non-null float64
pain                                                1789 non-null float64
pancreatic neoplasms                                0 non-null float64
panic disorder                                      1789 non-null float64
papilary thyroid carcinoma                          0 non-null float64
parkinson disease                                   1789 non-null float64
patau syndrome                                      0 non-null float64
pemphigus, benign familial                          0 non-null float64
periodontal diseases                                1789 non-null float64
periodontitis                                       1789 non-null float64
pheochromocytoma                                    1789 non-null float64
pituitary adenomas                                  0 non-null float64
pituitary neoplasms                                 1789 non-null float64
polycystic kidney diseases                          1789 non-null float64
polycythemia vera                                   1789 non-null float64
precursor b-cell lymphoblastic leukemia-lymphoma    1789 non-null float64
precursor cell lymphoblastic leukemia-lymphoma      0 non-null float64
precursor t-cell lymphoblastic leukemia-lymphoma    1789 non-null float64
pre-eclampsia                                       1789 non-null float64
pregnancy, ectopic                                  0 non-null float64
prion diseases                                      1789 non-null float64
prolactinoma                                        1789 non-null float64
prostate neoplasms                                  0 non-null float64
prostatic neoplasms                                 1789 non-null float64
prrsv infection                                     0 non-null float64
psoriasis                                           1789 non-null float64
psychotic disorders                                 1789 non-null float64
pulmonary disease, chronic obstructive              0 non-null float64
pulmonary embolism                                  1789 non-null float64
pulmonary fibrosis                                  1789 non-null float64
radiation injuries                                  0 non-null float64
rectal neoplasms                                    1789 non-null float64
renal insufficiency                                 1789 non-null float64
reperfusion injury                                  1789 non-null float64
retinal degeneration                                1789 non-null float64
retinal neovascularization                          1789 non-null float64
retinoblastoma                                      1789 non-null float64
rhabdomyosarcoma                                    1789 non-null float64
rhinitis, allergic, perennial                       1789 non-null float64
rna virus infections                                0 non-null float64
salivary gland neoplasms                            1789 non-null float64
sarcoma                                             1789 non-null float64
sarcoma, ewing                                      0 non-null float64
sarcoma, ewing's                                    0 non-null float64
sarcoma, kaposi                                     0 non-null float64
sarcoma, synovial                                   0 non-null float64
sars virus                                          0 non-null float64
schistosomiasis                                     0 non-null float64
schizophrenia                                       1789 non-null float64
scleroderma, localized                              0 non-null float64
scleroderma, systemic                               0 non-null float64
sepsis                                              1789 non-null float64
sezary syndrome                                     1789 non-null float64
siv infection                                       0 non-null float64
sjogren's syndrome                                  1789 non-null float64
skin neoplasms                                      1789 non-null float64
small cell lung carcinoma                           0 non-null float64
spinal cord injuries                                0 non-null float64
stomach diseases                                    1789 non-null float64
stomach neoplasms                                   1789 non-null float64
stomach neoplasms                                   0 non-null float64
stroke                                              0 non-null float64
supranuclear palsy, progressive                     0 non-null float64
synapses                                            0 non-null float64
testicular neoplasms                                1789 non-null float64
thyroid neoplasms                                   0 non-null float64
tongue neoplasms                                    1789 non-null float64
tourette syndrome                                   0 non-null float64
toxoplasma                                          0 non-null float64
toxoplasmosis                                       0 non-null float64
trophoblasts                                        0 non-null float64
tuberculosis, pulmonary                             1789 non-null float64
urinary bladder neoplasms                           0 non-null float64
uterine cervical neoplasms                          0 non-null float64
vascular calcification                              1789 non-null float64
vascular diseases                                   1789 non-null float64
vitiligo                                            1789 non-null float64
waldenstrom macroglobulinemia                       1789 non-null float64
wounds and injuries                                 0 non-null float64
dtypes: float64(383)
memory usage: 5.2+ MB
>>> Dattr.fillna(value = 0)
1         abortion, habitual         ...           wounds and injuries
AARS                0.000560         ...                           0.0
AARS2               0.000567         ...                           0.0
ABCA1               0.000555         ...                           0.0
ABCB5               0.000563         ...                           0.0
ABCB7               0.000557         ...                           0.0
ABCD4               0.000560         ...                           0.0
ABCF1               0.000557         ...                           0.0
ABI2                0.000554         ...                           0.0
ABL1                0.000550         ...                           0.0
ACBD3               0.000552         ...                           0.0
ACLY                0.000561         ...                           0.0
ACP1                0.000555         ...                           0.0
ACSL3               0.000569         ...                           0.0
ACTA1               0.000550         ...                           0.0
ACTA2               0.000550         ...                           0.0
ACTB                0.000550         ...                           0.0
ACTC1               0.000551         ...                           0.0
ACTN1               0.000557         ...                           0.0
ACTN4               0.000549         ...                           0.0
ACTR1A              0.000559         ...                           0.0
ACVR1B              0.000551         ...                           0.0
ADA                 0.000555         ...                           0.0
ADAM10              0.000554         ...                           0.0
ADAM12              0.000554         ...                           0.0
ADAM9               0.000541         ...                           0.0
ADAMTS1             0.000542         ...                           0.0
ADAMTSL4            0.000554         ...                           0.0
ADAR                0.000551         ...                           0.0
ADD2                0.000560         ...                           0.0
ADIPOR2             0.000552         ...                           0.0
...                      ...         ...                           ...
YAP1                0.000555         ...                           0.0
YBX1                0.000551         ...                           0.0
YRDC                0.000551         ...                           0.0
YTHDC1              0.000557         ...                           0.0
YWHAE               0.000551         ...                           0.0
YWHAQ               0.000553         ...                           0.0
YWHAZ               0.000552         ...                           0.0
YY1                 0.000558         ...                           0.0
YY1AP1              0.000553         ...                           0.0
ZBED1               0.000558         ...                           0.0
ZBTB45              0.000556         ...                           0.0
ZBTB6               0.000551         ...                           0.0
ZC3H11A             0.000559         ...                           0.0
ZC3H7B              0.000557         ...                           0.0
ZDHHC4              0.000557         ...                           0.0
ZEB1                0.000556         ...                           0.0
ZEB2                0.000557         ...                           0.0
ZFP36               0.000555         ...                           0.0
ZFP91               0.000554         ...                           0.0
ZFPM2               0.000726         ...                           0.0
ZHX1                0.000552         ...                           0.0
ZMYND8              0.000550         ...                           0.0
ZNF202              0.000555         ...                           0.0
ZNF354A             0.000568         ...                           0.0
ZNF384              0.000554         ...                           0.0
ZNF559              0.000560         ...                           0.0
ZNF622              0.000555         ...                           0.0
ZNF638              0.000556         ...                           0.0
ZNF804A             0.000567         ...                           0.0
ZZEF1               0.000555         ...                           0.0

[1789 rows x 383 columns]
>>> Mattr = miRAttr.reindex(columns = miRNA_index[1])
>>> Mattr,fillna(value = 0)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    Mattr,fillna(value = 0)
NameError: name 'fillna' is not defined
>>> Mattr.fillna(value = 0)
1         hsa-mir-125a  hsa-mir-196a      ...       hsa-mir-944  hsa-mir-518a
AARS          0.000449      0.000499      ...               0.0           0.0
AARS2         0.000449      0.000499      ...               0.0           0.0
ABCA1         0.000511      0.000539      ...               0.0           0.0
ABCB5         0.000578      0.000576      ...               0.0           0.0
ABCB7         0.000452      0.000504      ...               0.0           0.0
ABCD4         0.000449      0.000499      ...               0.0           0.0
ABCF1         0.000449      0.000499      ...               0.0           0.0
ABI2          0.000544      0.000563      ...               0.0           0.0
ABL1          0.000512      0.000597      ...               0.0           0.0
ACBD3         0.001010      0.000627      ...               0.0           0.0
ACLY          0.000582      0.000582      ...               0.0           0.0
ACP1          0.000700      0.000637      ...               0.0           0.0
ACSL3         0.000544      0.000563      ...               0.0           0.0
ACTA1         0.000578      0.000576      ...               0.0           0.0
ACTA2         0.000548      0.000560      ...               0.0           0.0
ACTB          0.000418      0.000481      ...               0.0           0.0
ACTC1         0.000452      0.000504      ...               0.0           0.0
ACTN1         0.000578      0.000576      ...               0.0           0.0
ACTN4         0.000452      0.000504      ...               0.0           0.0
ACTR1A        0.000557      0.000546      ...               0.0           0.0
ACVR1B        0.000581      0.000585      ...               0.0           0.0
ADA           0.000582      0.000582      ...               0.0           0.0
ADAM10        0.000582      0.000582      ...               0.0           0.0
ADAM12        0.000578      0.000576      ...               0.0           0.0
ADAM9         0.000508      0.000534      ...               0.0           0.0
ADAMTS1       0.001139      0.000575      ...               0.0           0.0
ADAMTSL4      0.000578      0.000576      ...               0.0           0.0
ADAR          0.000576      0.000574      ...               0.0           0.0
ADD2          0.000545      0.000583      ...               0.0           0.0
ADIPOR2       0.000481      0.000515      ...               0.0           0.0
...                ...           ...      ...               ...           ...
YAP1          0.000544      0.000563      ...               0.0           0.0
YBX1          0.000516      0.000538      ...               0.0           0.0
YRDC          0.000449      0.000499      ...               0.0           0.0
YTHDC1        0.000578      0.000576      ...               0.0           0.0
YWHAE         0.000449      0.000499      ...               0.0           0.0
YWHAQ         0.000578      0.000576      ...               0.0           0.0
YWHAZ         0.000625      0.000607      ...               0.0           0.0
YY1           0.000449      0.000499      ...               0.0           0.0
YY1AP1        0.000544      0.000563      ...               0.0           0.0
ZBED1         0.000544      0.000563      ...               0.0           0.0
ZBTB45        0.000449      0.000499      ...               0.0           0.0
ZBTB6         0.000578      0.000576      ...               0.0           0.0
ZC3H11A       0.000578      0.000576      ...               0.0           0.0
ZC3H7B        0.000461      0.000510      ...               0.0           0.0
ZDHHC4        0.000545      0.000583      ...               0.0           0.0
ZEB1          0.000665      0.000600      ...               0.0           0.0
ZEB2          0.000662      0.000594      ...               0.0           0.0
ZFP36         0.000596      0.000567      ...               0.0           0.0
ZFP91         0.000544      0.000563      ...               0.0           0.0
ZFPM2         0.000625      0.000594      ...               0.0           0.0
ZHX1          0.000508      0.000534      ...               0.0           0.0
ZMYND8        0.000492      0.000531      ...               0.0           0.0
ZNF202        0.000449      0.000499      ...               0.0           0.0
ZNF354A       0.000449      0.000499      ...               0.0           0.0
ZNF384        0.000578      0.000576      ...               0.0           0.0
ZNF559        0.000561      0.000547      ...               0.0           0.0
ZNF622        0.000578      0.000576      ...               0.0           0.0
ZNF638        0.000578      0.000576      ...               0.0           0.0
ZNF804A       0.000517      0.000539      ...               0.0           0.0
ZZEF1         0.000449      0.000499      ...               0.0           0.0

[1789 rows x 495 columns]
>>> Dattr.T
                                        AARS    ...        ZZEF1
1                                               ...             
abortion, habitual                  0.000560    ...     0.000555
acquired immunodeficiency syndrome  0.000775    ...     0.000568
acth-secreting pituitary adenoma    0.000768    ...     0.000584
acute coronary syndrome             0.000673    ...     0.000624
acute lung injury                   0.000840    ...     0.000585
adenocarcinoma                      0.000545    ...     0.000521
adenoma                             0.000812    ...     0.000654
adenoviridae infections                  NaN    ...          NaN
adrenal cortex neoplasms                 NaN    ...          NaN
adrenocortical adenoma                   NaN    ...          NaN
adrenocortical carcinoma            0.000574    ...     0.000549
aging                                    NaN    ...          NaN
aids dementia complex                    NaN    ...          NaN
albuminuria                         0.000766    ...     0.000609
alopecia                            0.000809    ...     0.000582
alzheimer disease                        NaN    ...          NaN
amyloidosis                         0.000699    ...     0.000671
amyotrophic lateral sclerosis            NaN    ...          NaN
anemia, sickle cell                      NaN    ...          NaN
angina, unstable                    0.000711    ...     0.000536
anoxia                                   NaN    ...          NaN
antiphospholipid syndrome                NaN    ...          NaN
anus neoplasms                           NaN    ...          NaN
anxiety disorders                   0.000757    ...     0.000650
aortic aneurysm, abdominal          0.000743    ...     0.000642
aortic aneurysm, thoracic           0.000667    ...     0.000631
aortic valve insufficiency          0.000860    ...     0.000642
aortic valve stenosis               0.000922    ...     0.000578
arrhythmias, cardiac                     NaN    ...          NaN
arthritis                           0.000871    ...     0.000614
...                                      ...    ...          ...
scleroderma, localized                   NaN    ...          NaN
scleroderma, systemic                    NaN    ...          NaN
sepsis                              0.000612    ...     0.000622
sezary syndrome                     0.000723    ...     0.000662
siv infection                            NaN    ...          NaN
sjogren's syndrome                  0.000715    ...     0.000641
skin neoplasms                      0.000754    ...     0.000620
small cell lung carcinoma                NaN    ...          NaN
spinal cord injuries                     NaN    ...          NaN
stomach diseases                    0.000785    ...     0.000622
stomach neoplasms                   0.000468    ...     0.000524
stomach neoplasms                        NaN    ...          NaN
stroke                                   NaN    ...          NaN
supranuclear palsy, progressive          NaN    ...          NaN
synapses                                 NaN    ...          NaN
testicular neoplasms                0.000778    ...     0.000633
thyroid neoplasms                        NaN    ...          NaN
tongue neoplasms                    0.000726    ...     0.000621
tourette syndrome                        NaN    ...          NaN
toxoplasma                               NaN    ...          NaN
toxoplasmosis                            NaN    ...          NaN
trophoblasts                             NaN    ...          NaN
tuberculosis, pulmonary             0.000510    ...     0.000521
urinary bladder neoplasms                NaN    ...          NaN
uterine cervical neoplasms               NaN    ...          NaN
vascular calcification              0.000530    ...     0.000558
vascular diseases                   0.000730    ...     0.000582
vitiligo                            0.000871    ...     0.000628
waldenstrom macroglobulinemia       0.000676    ...     0.000591
wounds and injuries                      NaN    ...          NaN

[383 rows x 1789 columns]
>>> Mattr = Mattr.fillna(value = 0)
>>> Dattr = Dattr.fillna(value = 0)
>>> Mattr
1         hsa-mir-125a  hsa-mir-196a      ...       hsa-mir-944  hsa-mir-518a
AARS          0.000449      0.000499      ...               0.0           0.0
AARS2         0.000449      0.000499      ...               0.0           0.0
ABCA1         0.000511      0.000539      ...               0.0           0.0
ABCB5         0.000578      0.000576      ...               0.0           0.0
ABCB7         0.000452      0.000504      ...               0.0           0.0
ABCD4         0.000449      0.000499      ...               0.0           0.0
ABCF1         0.000449      0.000499      ...               0.0           0.0
ABI2          0.000544      0.000563      ...               0.0           0.0
ABL1          0.000512      0.000597      ...               0.0           0.0
ACBD3         0.001010      0.000627      ...               0.0           0.0
ACLY          0.000582      0.000582      ...               0.0           0.0
ACP1          0.000700      0.000637      ...               0.0           0.0
ACSL3         0.000544      0.000563      ...               0.0           0.0
ACTA1         0.000578      0.000576      ...               0.0           0.0
ACTA2         0.000548      0.000560      ...               0.0           0.0
ACTB          0.000418      0.000481      ...               0.0           0.0
ACTC1         0.000452      0.000504      ...               0.0           0.0
ACTN1         0.000578      0.000576      ...               0.0           0.0
ACTN4         0.000452      0.000504      ...               0.0           0.0
ACTR1A        0.000557      0.000546      ...               0.0           0.0
ACVR1B        0.000581      0.000585      ...               0.0           0.0
ADA           0.000582      0.000582      ...               0.0           0.0
ADAM10        0.000582      0.000582      ...               0.0           0.0
ADAM12        0.000578      0.000576      ...               0.0           0.0
ADAM9         0.000508      0.000534      ...               0.0           0.0
ADAMTS1       0.001139      0.000575      ...               0.0           0.0
ADAMTSL4      0.000578      0.000576      ...               0.0           0.0
ADAR          0.000576      0.000574      ...               0.0           0.0
ADD2          0.000545      0.000583      ...               0.0           0.0
ADIPOR2       0.000481      0.000515      ...               0.0           0.0
...                ...           ...      ...               ...           ...
YAP1          0.000544      0.000563      ...               0.0           0.0
YBX1          0.000516      0.000538      ...               0.0           0.0
YRDC          0.000449      0.000499      ...               0.0           0.0
YTHDC1        0.000578      0.000576      ...               0.0           0.0
YWHAE         0.000449      0.000499      ...               0.0           0.0
YWHAQ         0.000578      0.000576      ...               0.0           0.0
YWHAZ         0.000625      0.000607      ...               0.0           0.0
YY1           0.000449      0.000499      ...               0.0           0.0
YY1AP1        0.000544      0.000563      ...               0.0           0.0
ZBED1         0.000544      0.000563      ...               0.0           0.0
ZBTB45        0.000449      0.000499      ...               0.0           0.0
ZBTB6         0.000578      0.000576      ...               0.0           0.0
ZC3H11A       0.000578      0.000576      ...               0.0           0.0
ZC3H7B        0.000461      0.000510      ...               0.0           0.0
ZDHHC4        0.000545      0.000583      ...               0.0           0.0
ZEB1          0.000665      0.000600      ...               0.0           0.0
ZEB2          0.000662      0.000594      ...               0.0           0.0
ZFP36         0.000596      0.000567      ...               0.0           0.0
ZFP91         0.000544      0.000563      ...               0.0           0.0
ZFPM2         0.000625      0.000594      ...               0.0           0.0
ZHX1          0.000508      0.000534      ...               0.0           0.0
ZMYND8        0.000492      0.000531      ...               0.0           0.0
ZNF202        0.000449      0.000499      ...               0.0           0.0
ZNF354A       0.000449      0.000499      ...               0.0           0.0
ZNF384        0.000578      0.000576      ...               0.0           0.0
ZNF559        0.000561      0.000547      ...               0.0           0.0
ZNF622        0.000578      0.000576      ...               0.0           0.0
ZNF638        0.000578      0.000576      ...               0.0           0.0
ZNF804A       0.000517      0.000539      ...               0.0           0.0
ZZEF1         0.000449      0.000499      ...               0.0           0.0

[1789 rows x 495 columns]
>>> Mattr = Mattr.T
>>> Mattr
                  AARS     AARS2    ...      ZNF804A     ZZEF1
1                                   ...                       
hsa-mir-125a  0.000449  0.000449    ...     0.000517  0.000449
hsa-mir-196a  0.000499  0.000499    ...     0.000539  0.000499
hsa-mir-499a  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-198   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-29a   0.000470  0.000470    ...     0.000582  0.000470
hsa-mir-29b   0.000457  0.000457    ...     0.000564  0.000457
hsa-let-7a    0.000427  0.000427    ...     0.000494  0.000427
hsa-mir-141   0.000478  0.000478    ...     0.000519  0.000478
hsa-mir-143   0.000489  0.000489    ...     0.000525  0.000489
hsa-mir-145   0.000426  0.000426    ...     0.000505  0.000426
hsa-mir-150   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-15a   0.000496  0.000496    ...     0.000531  0.000496
hsa-mir-16    0.000471  0.000471    ...     0.000526  0.000471
hsa-mir-21    0.000463  0.000463    ...     0.000530  0.000463
hsa-mir-1     0.000492  0.000492    ...     0.000628  0.000492
hsa-mir-133a  0.000472  0.000472    ...     0.000613  0.000472
hsa-mir-133b  0.000525  0.000525    ...     0.000548  0.000525
hsa-mir-146a  0.000518  0.000518    ...     0.000534  0.000518
hsa-mir-155   0.000440  0.000440    ...     0.000498  0.000440
hsa-mir-208b  0.000515  0.000515    ...     0.000602  0.000515
hsa-mir-103a  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-106a  0.000504  0.000504    ...     0.000541  0.000504
hsa-mir-10b   0.000465  0.000465    ...     0.000578  0.000465
hsa-mir-126   0.000428  0.000428    ...     0.000505  0.000428
hsa-mir-135a  0.000518  0.000518    ...     0.001118  0.000518
hsa-mir-151a  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-152   0.000574  0.000574    ...     0.000552  0.000574
hsa-mir-17    0.000411  0.000411    ...     0.000511  0.000411
hsa-mir-181b  0.000536  0.000536    ...     0.000547  0.000536
hsa-mir-182   0.000000  0.000000    ...     0.000000  0.000000
...                ...       ...    ...          ...       ...
hsa-mir-548a  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1256  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1296  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-521   0.000543  0.000543    ...     0.000554  0.000543
hsa-mir-616   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-642b  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-647   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1266  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1183  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1909  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1293  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1228  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-449c  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-518f  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-524   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-551a  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-570   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-577   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-591   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-595   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-605   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-610   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-938   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-189   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-3179  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-550b  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1227  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-1229  0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-944   0.000000  0.000000    ...     0.000000  0.000000
hsa-mir-518a  0.000000  0.000000    ...     0.000000  0.000000

[495 rows x 1789 columns]
>>> M = Mattr.values
>>> M
array([[0.00044908, 0.00044908, 0.00051142, ..., 0.00057816, 0.00051741,
        0.00044908],
       [0.0004988 , 0.0004988 , 0.0005386 , ..., 0.00057558, 0.00053888,
        0.0004988 ],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ],
       ...,
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ]])
>>> Dattr
1         abortion, habitual         ...           wounds and injuries
AARS                0.000560         ...                           0.0
AARS2               0.000567         ...                           0.0
ABCA1               0.000555         ...                           0.0
ABCB5               0.000563         ...                           0.0
ABCB7               0.000557         ...                           0.0
ABCD4               0.000560         ...                           0.0
ABCF1               0.000557         ...                           0.0
ABI2                0.000554         ...                           0.0
ABL1                0.000550         ...                           0.0
ACBD3               0.000552         ...                           0.0
ACLY                0.000561         ...                           0.0
ACP1                0.000555         ...                           0.0
ACSL3               0.000569         ...                           0.0
ACTA1               0.000550         ...                           0.0
ACTA2               0.000550         ...                           0.0
ACTB                0.000550         ...                           0.0
ACTC1               0.000551         ...                           0.0
ACTN1               0.000557         ...                           0.0
ACTN4               0.000549         ...                           0.0
ACTR1A              0.000559         ...                           0.0
ACVR1B              0.000551         ...                           0.0
ADA                 0.000555         ...                           0.0
ADAM10              0.000554         ...                           0.0
ADAM12              0.000554         ...                           0.0
ADAM9               0.000541         ...                           0.0
ADAMTS1             0.000542         ...                           0.0
ADAMTSL4            0.000554         ...                           0.0
ADAR                0.000551         ...                           0.0
ADD2                0.000560         ...                           0.0
ADIPOR2             0.000552         ...                           0.0
...                      ...         ...                           ...
YAP1                0.000555         ...                           0.0
YBX1                0.000551         ...                           0.0
YRDC                0.000551         ...                           0.0
YTHDC1              0.000557         ...                           0.0
YWHAE               0.000551         ...                           0.0
YWHAQ               0.000553         ...                           0.0
YWHAZ               0.000552         ...                           0.0
YY1                 0.000558         ...                           0.0
YY1AP1              0.000553         ...                           0.0
ZBED1               0.000558         ...                           0.0
ZBTB45              0.000556         ...                           0.0
ZBTB6               0.000551         ...                           0.0
ZC3H11A             0.000559         ...                           0.0
ZC3H7B              0.000557         ...                           0.0
ZDHHC4              0.000557         ...                           0.0
ZEB1                0.000556         ...                           0.0
ZEB2                0.000557         ...                           0.0
ZFP36               0.000555         ...                           0.0
ZFP91               0.000554         ...                           0.0
ZFPM2               0.000726         ...                           0.0
ZHX1                0.000552         ...                           0.0
ZMYND8              0.000550         ...                           0.0
ZNF202              0.000555         ...                           0.0
ZNF354A             0.000568         ...                           0.0
ZNF384              0.000554         ...                           0.0
ZNF559              0.000560         ...                           0.0
ZNF622              0.000555         ...                           0.0
ZNF638              0.000556         ...                           0.0
ZNF804A             0.000567         ...                           0.0
ZZEF1               0.000555         ...                           0.0

[1789 rows x 383 columns]
>>> D = Dattr.T.values
>>> D
array([[0.00055985, 0.00056657, 0.00055523, ..., 0.00055614, 0.0005667 ,
        0.0005552 ],
       [0.00077523, 0.00054794, 0.00047251, ..., 0.00053476, 0.000528  ,
        0.00056794],
       [0.00076778, 0.00059159, 0.00047648, ..., 0.00051813, 0.00055517,
        0.00058397],
       ...,
       [0.00087072, 0.00057328, 0.00048473, ..., 0.00056215, 0.0005332 ,
        0.00062845],
       [0.00067584, 0.00058029, 0.00049289, ..., 0.00052492, 0.00055677,
        0.00059129],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ]])
>>> np.vstack(M,D)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    np.vstack(M,D)
TypeError: vstack() takes 1 positional argument but 2 were given
>>> M
array([[0.00044908, 0.00044908, 0.00051142, ..., 0.00057816, 0.00051741,
        0.00044908],
       [0.0004988 , 0.0004988 , 0.0005386 , ..., 0.00057558, 0.00053888,
        0.0004988 ],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ],
       ...,
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ]])
>>> M.shape
(495, 1789)
>>> D.shape
(383, 1789)
>>> np.vstack((M,D))
array([[0.00044908, 0.00044908, 0.00051142, ..., 0.00057816, 0.00051741,
        0.00044908],
       [0.0004988 , 0.0004988 , 0.0005386 , ..., 0.00057558, 0.00053888,
        0.0004988 ],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ],
       ...,
       [0.00087072, 0.00057328, 0.00048473, ..., 0.00056215, 0.0005332 ,
        0.00062845],
       [0.00067584, 0.00058029, 0.00049289, ..., 0.00052492, 0.00055677,
        0.00059129],
       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,
        0.        ]])
>>> Attr = np.vstack((M,D))
>>> At = ssp.csc_matrix(Attr)
>>> data = np.loadtxt("5430dataset/1.miRNA-disease associations/association.txt")
>>> data = ssp.csc_matrix(data)
>>> sio.savemat("./data/MD5430_simi_embedattr.mat",{'net':data,'group':embedding})
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    sio.savemat("./data/MD5430_simi_embedattr.mat",{'net':data,'group':embedding})
NameError: name 'embedding' is not defined
>>> sio.savemat("./data/MD5430_gene_Attribute.mat",{'net':data,'group':At})
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    sio.savemat("./data/MD5430_gene_Attribute.mat",{'net':data,'group':At})
  File "D:\software\codesoftwware\python\lib\site-packages\scipy\io\matlab\mio.py", line 270, in savemat
    file_stream = open(file_name, 'wb')
FileNotFoundError: [Errno 2] No such file or directory: './data/MD5430_gene_Attribute.mat'
>>> sio.savemat("/MD5430_gene_Attribute.mat",{'net':data,'group':At})
>>> sio.savemat("MD5430_gene_Attribute.mat",{'net':data,'group':At})
>>> disAttr = pd.read_csv("./data/disease_gene.csv",header = 0,index_col=0)

