import numpy as np

def Nil ():
    return []
    
def Tree(root, L, R):
    return [root, L, R]

def root(t):
    return t[0]

def L(t):
    return t[1]

def R(t):
    return t[2]
    
def F(t): # ret_t  - The most heavy balanced almost positive subtree in t
           # is_pos - If t is almost positive then is_pos = True otherwise is_pos = False
           # is_bal - If t is balanced then is_bal = True otherwise is_bal = False 
           # n_pos  - The number of positive vertices in t
           # n_neg  - T he number of negative vertices in t
           # h      - The height of the t
           # w      - The weight of the t
           # w_ret  - The weight of the most heavy balanced almost positive subtree in t
    
    if t == Nil():
        return Nil(), True, True, 0, 0, 0, 0, 0
    
    l_ret_t, l_is_pos, l_is_bal, l_n_pos, l_n_neg, l_h, l_w, l_w_ret = F(L(t))
    r_ret_t, r_is_pos, r_is_bal, r_n_pos, r_n_neg, r_h, r_w, r_w_ret = F(R(t))
    
    n_pos = (l_n_pos + l_n_pos + 1) if root(t) >  0 else (l_n_pos + l_n_pos)
    n_neg = (l_n_neg + l_n_neg + 1) if root(t) <= 0 else (l_n_neg + l_n_neg)
    h = max(l_h, r_h) + 1
    is_pos = n_pos > n_neg 
    is_bal = abs(l_h - r_h) <= 1
    w = l_w + r_w + root(t)
    w_ret = max(l_w_ret, r_w_ret, w) if (is_bal and is_pos) else max(l_w_ret, r_w_ret)
    
    if is_bal and is_pos:
        ret_t = t if w > max(l_w_ret, r_w_ret) else l_ret_t if l_w_ret > r_w_ret else r_ret_t
    else:
        ret_t = l_ret_t if l_w_ret > r_w_ret else r_ret_t
        
    return (ret_t, is_pos, is_bal, n_pos, n_neg, h, w, w_ret)

def G(t): # max_w_level, w_levels
    if t == Nil():
        return 0, []
    
    l_max_w_level, l_w_levels = G(L(t))
    r_max_w_level, r_w_levels = G(R(t))
    
    m = len(l_w_levels)
    n = len(r_w_levels)
    k = min(m, n)
    
    if m > n:
        w_levels = [root(t)] + [l_w_levels[i] + r_w_levels[i] for i in range(k)] + l_w_levels[k :]
    else:
        w_levels = [root(t)] + [l_w_levels[i] + r_w_levels[i] for i in range(k)] + r_w_levels[k :]
    
    return max(w_levels), w_levels

def H(A):
    m, n = A.shape
    N = A - np.mean(A, 1).reshape(n, 1)
    P = np.dot(N, N.T)
    x = np.diag(P).reshape(n, 1)
    Q = np.dot(x, x.T)**0.5
    return P / Q