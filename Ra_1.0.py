import pandas as pd
import csv

data_sample = []  # Sadece featureların bulunduğu data
data_core = []
data_info = []
data_relief = []
data_sym = []
features_sample = []  # Sıralanmamış toplam feature değerleri.
features_info = []
features_core = []
features_relief = []
features_sym = []
sorted_sample = []  # Puanlanmamış sadece büyükten küçüğe sıralanmış hali.
sorted_core = []
sorted_info = []
sorted_relief = []
sorted_sym = []
score_sample = []  # Puanlanmış büyükten küçüğe sıralanmış hali.
score_core = []
score_info = []
score_relief = []
score_sym = []
RaRF_sample = []  # çarpılmış değerler ve featurelar.
RaRF_core = []
RaRF_info = []
RaRF_relief = []
RaRF_sym = []
Ra = []
sortedRa=[]

def ReadCsv(filename, data, features):
    pd.read_csv(filename, sep=',')
    df = pd.read_csv(filename, sep=',')
    for row in df:
        data.append(row)
    for i in range((len(data) - 1)):
        Total = df[data[i]].sum()
        features.append(Total)
    data.pop()  # Son Feature Atıldı


def SortFeature(sort_it, data, features):
    A = list(zip(data, features))
    A = sorted(A, reverse=True, key=lambda tup: tup[1])

    for i in range(0, len(A)):
        sort_it.append(A[i])


def Scoring(data, score):
    j = []
    temp = []
    temp = data
    for i in range(len(data), 0, -1):
        j.append(i)
    G = list(zip(temp, j))
    for k in range(0, len(data)):
        score.append(G[k])


def RaRF(score, rarf):
    b = []
    c = []
    for i in range(0, len(score)):
        a = score[i][1] * score[i][0][1]
        c.append(a)
        b.append(score[i][0][0])
    d = list(zip(b, c))
    for j in range(0, len(score)):
        rarf.append(d[j])


def sumSortedRarf(rarf_core, rarf_info, rarf_relief, rarf_sym):
    sum = []
    core_info_sum = []
    for i in range(0, len(rarf_core)):
        for j in range(0, len(rarf_core)):
            if rarf_core[i][0] == rarf_info[j][0]:
                sum.append(rarf_core[i][1] + rarf_info[j][1])
                core_info_sum.append(rarf_core[i][0])
                break
            else:

                j += 1
    z = list(zip(core_info_sum, sum))  # core ve infogain 'in çin aynı feature değerleri toplandı.

    sum2 = []
    relief_sym_sum2 = []
    for k in range(0, len(rarf_relief)):
        for l in range(0, len(rarf_relief)):
            if rarf_relief[k][0] == rarf_sym[l][0]:
                sum2.append(rarf_relief[k][1] + rarf_sym[l][1])
                relief_sym_sum2.append(rarf_relief[k][0])
                break
            else:
                l += 1
    z2 = list(zip(relief_sym_sum2, sum2))
    sum3 = []
    featuress = []
    for m in range(0, len(z2)):
        for n in range(0, len(z)):
            if z2[m][0] == z[n][0]:
                sum3.append(z2[m][1] + z[n][1])
                featuress.append(z2[m][0])
                break
            else:
                n += 1
    z3 = list(zip(featuress, sum3))
    for res in range(0, len(z3)):
        Ra.append(z3[res])


def RaSort(ra):
    ra = sorted(ra, reverse=True, key=lambda tup: tup[1])
    for i in range(0, len(ra)):
        sortedRa.append(ra[i])


ReadCsv('sample_mini.csv', data_sample, features_sample)
ReadCsv('core_yuzde90.csv', data_core, features_core)
ReadCsv('info_yuzde90.csv', data_info, features_info)
ReadCsv('relief_yuzde90.csv', data_relief, features_relief)
ReadCsv('sym_yuzde90.csv', data_sym, features_sym)

# Correlation Attirbute
SortFeature(sorted_core, data_core, features_core)
Scoring(sorted_core, score_core)
RaRF(score_core, RaRF_core)

# InfoGain Attirbute
SortFeature(sorted_info, data_info, features_info)
Scoring(sorted_info, score_info)
RaRF(score_info, RaRF_info)
# Relief Attirbute
SortFeature(sorted_relief, data_relief, features_relief)
Scoring(sorted_relief, score_relief)
RaRF(score_relief, RaRF_relief)
# Symmetrical Uncert Attirbute
SortFeature(sorted_sym, data_sym, features_sym)
Scoring(sorted_sym, score_sym)
RaRF(score_sym, RaRF_sym)
#Sample
SortFeature(sorted_sample, data_sample, features_sample)
Scoring(sorted_sample, score_sample)
RaRF(score_sample, RaRF_sample)


sumSortedRarf(RaRF_core, RaRF_info, RaRF_relief, RaRF_sym)
RaSort(Ra)

with open('Ra90.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(sortedRa)
