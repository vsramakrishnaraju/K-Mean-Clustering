#!/usr/bin/env python
# coding: utf-8


#A skeleton for implementing Naive Bayes Classifier in Python.
## Author: Venkata 

import numpy as np
import random
import time
import math 
import pandas as pd

datafile = "twoEllipses.txt"

dataset = np.loadtxt(datafile)

randomset = dataset[np.random.randint(0,dataset.shape[0],3)]

print('start')

for i in range(2):
  
    d = dataset.shape[1]-1

    n = dataset.shape[0]
    
    nn = randomset.shape[0]

    #print(len(dataset), len(randomset))

    #print('dataset',dataset)

    #print(randomset)
    dist = []
    distance = []
    buffer = []
    euc_dist_each_test_data =[]


    for i in range(nn):
        for j in range(n):
            for k in range(d):
                euc_dist_each_test_data = np.sqrt(np.sum((randomset[i][k]-dataset[j][k])**2))
                buffer.append(euc_dist_each_test_data)
                euc_dist_each_test_data = []
            distance.append(buffer)
            buffer = []
        dist.append(distance)
        distance = []

    df1 = pd.DataFrame(dataset)
    # print(df1)
    df2 = pd.DataFrame(dist[0])
    df3 = pd.DataFrame(dist[1])
    df4 = pd.DataFrame(dist[2])

    result = pd.concat([df2, df3, df4], axis=1)

    result.columns = ['d1', 'd2', 'd3']

    #print('result',result)


    c1 = []
    c2 = []
    c3 = [] 
    for i in range(int(n)):
        # min(d1,d2,d3) if min is d1 add x, y to cl else if d2 is min add x, y to c2 else if d3 is min add x, y to c3 

        l = result.iat[i,0]
        m = result.iat[i,1]
        n = result.iat[i,2]
        #print(min(pdf))

    #     print('l',l)
    #     print('m',m)
    #     print('n',n)

        pdf = min(result.loc[i,:])

    #     print('min-set', pdf)

    #     print('df1', df1.loc[i])

        if pdf == l:
            c1.append(df1.loc[i])
        elif pdf == m:
            c2.append(df1.loc[i])
        else:
            c3.append(df1.loc[i])


#     print('c1_len',len(c1))
#     print('c2_len',len(c2))
#     print('c3_len',len(c3))

    centroid = []
    centroid1 = []
    centroid2 = []

    centroid_m = []

    x = []
    y = []

    for i in range(len(c1)):
        x.append(c1[i][0])
        y.append(c1[i][1])

    mean_x = np.sum(x)/len(c1)
    mean_y = np.sum(y)/len(c1)

#     print(mean_x)
#     print(mean_y)

    centroid.append(mean_x)
    centroid.append(mean_y)

    centroid_m.append(centroid)

    x1 = []
    y1 = []

    for i in range(len(c2)):
        x1.append(c2[i][0])
        y1.append(c2[i][1])

    mean_x1 = np.sum(x1)/len(c2)
    mean_y1 = np.sum(y1)/len(c2)

#     print(mean_x1)
#     print(mean_y1)

    centroid1.append(mean_x1)
    centroid1.append(mean_y1)

    centroid_m.append(centroid1)

    x2 = []
    y2 = []

    for i in range(len(c3)):
        x2.append(c3[i][0])
        y2.append(c3[i][1])

    mean_x2 = np.sum(x2)/len(c1)
    mean_y2 = np.sum(y2)/len(c1)

#     print(mean_x2)
#     print(mean_y2)

    centroid2.append(mean_x2)
    centroid2.append(mean_y2)

    centroid_m.append(centroid2)

#   print('centroid m', centroid_m)

    randomset = np.array(centroid_m)
    

print('final mean or centroid')
print(randomset)

print('Cluster_1 size',len(c1))
print('Cluster_2 size',len(c2))
print('Cluster_3 size',len(c3))

print('Cluster_1 points')

for d, c in zip(x, y):
    print(d, c)
    
print('Cluster_2 points')

for d, c in zip(x1, y1):
    print(d, c)

print('Cluster_3 points')

for d, c in zip(x2, y2):
    print(d, c)

print('end')




