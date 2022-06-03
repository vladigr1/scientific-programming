'''
 n-gram model - txt: XXX.... n=3 
 make table of ngram count array for each string
 cov preason - cov(x,y)/sqrt(var(x) * var(y))
'''

str1 = "dsfdsf dsf"
str2 = 'df dsf dsg dgd'
n = 4


def str_to_list_ng(st : str, n):
    # return [st[i : i+n] for i in range(len(st) - n + 1)]
    return [hash(st[i : i+n]) for i in range(len(st) - n + 1)]

def list_to_vec(L : list, UL : list):
    return [L.count(x) for x in UL]

'''
cov preason - cov(x,y)/sqrt(var(x) * var(y))
cov(x,y) = E((x-E(x))* (y-E(y))) = 1/n sum((x_i - x_avg)*(y_i - y_avg))
'''
def pearson(v1, v2):
    n = len(v1)
    v1_av = sum(v1) / n
    v2_av = sum(v2) / n
    x = [ t - v1_av for t in v1]
    y = [ t - v2_av for t in v2]
    xy = sum([x[i]*y[i] for i in range(n)])
    xx = sum([ t**2 for t in x])**0.5
    yy = sum([ t**2 for t in y])**0.5
    p = xy / (xx * yy)
    return (1 - p)/2

l1 = str_to_list_ng(str1, n)
l2 = str_to_list_ng(str2, n)
L = l1 + l2
uni_ng = list(set(L))
V1 = list_to_vec(l1, uni_ng)
V2 = list_to_vec(l2, uni_ng)
