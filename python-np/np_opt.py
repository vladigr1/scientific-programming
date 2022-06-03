'''
 n-gram model - txt: XXX.... n=3 
 make table of ngram count array for each string
 cov preason - cov(x,y)/sqrt(var(x) * var(y))
'''
#%%
import numpy as np

str1 = "abcabcabc"
str2 = 'df dsf dsg dgd'
n = 4


def str_to_list_ng(st : str, n):
    # return [st[i : i+n] for i in range(len(st) - n + 1)]
    return [hash(st[i : i+n]) for i in range(len(st) - n + 1)]

def list_to_vec(L : np.array, UL : np.array):
    n1 = L.shape
    L1 = L.reshape(1,n1[0])
    n2 = UL.shape
    L2 = UL.reshape(n2[0],1)
    one_matrix = L1 == L2 # give 1 to similar
    return (one_matrix) @ np.ones([n1[0],1])

'''
cov preason - cov(x,y)/sqrt(var(x) * var(y))
cov(x,y) = E((x-E(x))* (y-E(y))) = 1/n sum((x_i - x_avg)*(y_i - y_avg))
'''
def pearson(v1, v2):
    n = len(v1)
    v1_av = v1.sum() / n
    v2_av = v2.sum() / n
    x = (v1 - v1_av).reshape([1,n])
    y = (v2 - v2_av).reshape([n,1])
    xy = x @ y
    xx = (x @ x.T)**0.5
    yy = (y @ y.T)**0.5
    p = xy[0][0] / (xx[0][0] * yy[0][0])
    return (1 - p)/2

l1 = str_to_list_ng(str1, n)
l2 = str_to_list_ng(str2, n)
L = l1 + l2
l1 = np.array(l1)
l2 = np.array(l2)
uni_ng = np.array(list(set(L)))
V1 = list_to_vec(l1, uni_ng)
V2 = list_to_vec(l2, uni_ng)
print(pearson(V1, V2))
# %%
