
#%%
def Nil():
    return []

def Tree(root, L, R):
    return [root,L, R]

def root(t):
    return t[0]

def L(t):
    return t[1]

def R(t):
    return t[2]
'''
 return tb, sum, pos_node
 tb - tree best
 sum - sum nodes
 pos_node - num_pos_node - num_neg_node
 cur_sum - 
 cur_pos_node - 
'''
def F(t):
    if t == Nil():
        return t,0,0,0,0

    tb_l, sum_l,pos_node_l,cur_sum_l,cur_pos_node_l = F(L(t))
    tb_r, sum_r,pos_node_r,cur_sum_r,cur_pos_node_r = F(R(t))
    
    cur_pos_root = 0
    if root(t) > 0:
        cur_pos_root = 1
    elif root(t) < 0:
        cur_pos_root = -1
    cur_pos_node = cur_pos_node_l + cur_pos_node_r + cur_pos_root
        
    cur_sum = cur_sum_r + cur_sum_l + root(t)

    if cur_pos_node > 0 and cur_sum > cur_sum_l and cur_sum > cur_sum_r:
        return t,cur_sum, cur_pos_node, cur_sum, cur_pos_node
    
    if sum_l > sum_r:
        return tb_l, sum_l, pos_node_l, cur_sum, cur_pos_node
    else :
        return tb_r, sum_r, pos_node_r, cur_sum, cur_pos_node 

t = [-6, [5, [-3, [], []], []], [-5, [], [-7, [3, [], []], [5, [] ,[]]]]]
print(t)
print(f'print F(t) {F(t)}')
#result in index 1
print(f'print F(t) only bt {F(t)[1]}')


def G(t):
    depths_sum = {}
    '''
    t - tree (node we pass)
    depth - depth of current node from root
    '''
    def helper_G(t,depth):
        if t == Nil():
            return
        
        if depths_sum.get(depth) == None:
            depths_sum[depth] = root(t)
        else:
            depths_sum[depth] += root(t)
        
        helper_G(L(t), depth+1)
        helper_G(R(t), depth+1)

    helper_G(t,0)
    return max(depths_sum.values())

print(f'print G(t) {G(t)}')
print(f'print G(t) {G(t)}')

import numpy as np
def H(t):
    def row(x,y):
        n = len(x)
        x_av = x.sum() / n
        y_av = y.sum() / n
        x_hat = (x - x_av).reshape([1,n])
        y_hat = (y - y_av).reshape([n,1])
        numerator = x_hat @ y_hat
        x_hat_ds_sq = (x_hat @ x_hat.T)
        y_hat_ds_sq = (y_hat.T @ y_hat)
        denominator = (x_hat_ds_sq * y_hat_ds_sq)**0.5
        return numerator/denominator

    m,n = t.shape
    D = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            D[i,j] = row(t[i,:],t[j,:])
    return D

from scipy.spatial.distance import pdist, squareform
n = 4
A = np.random.rand(n, n)
B = 1 - squareform(pdist(A, 'correlation'))
print('H(T):')
print(H(A), "\n")
print(B)
# %%
