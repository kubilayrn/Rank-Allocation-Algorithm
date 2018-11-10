import pandas as pd
import csv

  # Sadece featurelarýn bulunduðu data
data_vot2 = []
data_vot3 = []
data_vot4 = []

 # Sýralanmamýþ toplam feature deðerleri.
features_vot2 = []
features_vot3 = []
features_vot4 = []

  # Puanlanmamýþ sadece büyükten küçüðe sýralanmýþ hali.
sorted_vot2 = []
sorted_vot3 = []
sorted_vot4 = []

 # Puanlanmýþ büyükten küçüðe sýralanmýþ hali.
score_vot2 = []
score_vot3 = []
score_vot4 = []

 # çarpýlmýþ deðerler ve featurelar.
RaRF_vot2 = []
RaRF_vot3 = []
RaRF_vot4 = []

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
    data.pop()  # Son Feature Atýldý


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


def sumSortedRarf(rarf_vot2, rarf_vot3, rarf_vot4):
    sum = []
    vot2_vot3_sum = []
    for i in range(0, len(rarf_vot2)):
        for j in range(0, len(rarf_vot3)):

            if rarf_vot2[i][0] == rarf_vot3[j][0]:
                sum.append(rarf_vot2[i][1] + rarf_vot3[j][1])
                vot2_vot3_sum.append(rarf_vot2[i][0])
                continue
            else:
                j+1



    z = list(zip(vot2_vot3_sum, sum))  # vot2 ve vot3  için ayný feature deðerleri toplandý.

    print(len(data_vot2))
    print(len(data_vot3))
    print(len(data_vot4))
    sum2 = []
    vot2_vot4_sum = []
    for i in range(0, len(rarf_vot2)):
        for j in range(0, len(rarf_vot4)):
            if rarf_vot2[i][0] == rarf_vot4[j][0]:
                sum2.append(rarf_vot2[i][1] + rarf_vot4[j][1])
                vot2_vot4_sum.append(rarf_vot2[i][0])
                continue
        else:
            j+1


    z2 = list(zip(vot2_vot4_sum, sum2))  # vot3 ve vot4 için ayný feature deðerleri toplandý.

    sum3 = []
    featuress = []
    for m in range(0, len(z2)):
        for n in range(0, len(z)):
            if z2[m][0] == z[n][0]:
                sum3.append(z2[m][1] + z[n][1])
                featuress.append(z2[m][0])
                continue
            else:
                n+1
    z3 = list(zip(featuress, sum3))
    for res in range(0, len(z3)):
        Ra.append(z3[res])


def RaSort(ra):
    ra = sorted(ra, reverse=True, key=lambda tup: tup[1])
    for i in range(0, len(ra)):
        sortedRa.append(ra[i])



ReadCsv('Voting_2in4_AttrCount_751.csv', data_vot2, features_vot2)
ReadCsv('Voting_3in4_AttrCount_751.csv', data_vot3, features_vot3)
ReadCsv('Voting_4in4_AttrCount_751.csv', data_vot4, features_vot4)


# Vot2 Attirbute
SortFeature(sorted_vot2, data_vot2, features_vot2)
Scoring(sorted_vot2, score_vot2)
RaRF(score_vot2, RaRF_vot2)

# Vot3 Attirbute
SortFeature(sorted_vot3, data_vot3, features_vot3)
Scoring(sorted_vot3, score_vot3)
RaRF(score_vot3, RaRF_vot3)
# Relief Attirbute
SortFeature(sorted_vot4, data_vot4, features_vot4)
Scoring(sorted_vot4, score_vot4)
RaRF(score_vot4, RaRF_vot4)



sumSortedRarf(RaRF_vot2, RaRF_vot3, RaRF_vot4)
RaSort(Ra)
#Data oluþturma

listTest=[]
dfO = pd.read_csv("Original.csv", sep=',')
for i in range(0,len(sortedRa)):
    a=sortedRa[i][0]
    listTest.append(dfO[a])
listTest.append(dfO.feature7507)
#print(type(listTest[1]))
dicts = {}
key=[]
values=listTest
for i in range(0,len(sortedRa)):
    key.append(sortedRa[i][0])
key.append("feature7507")
for i in range(0,len(listTest)):
    dicts[key[i]] = values[i]


dfSon=pd.DataFrame.from_dict(dicts)
dfSon.to_csv("vot90.csv", sep=',',index=False)



with open('Ra90test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(sortedRa)

