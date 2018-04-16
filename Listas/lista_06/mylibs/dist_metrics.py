import numpy as np



def minkowski_distance(X, row, p):
    X_ = (np.absolute(X - row)) ** p
    return np.sum(X_,axis=1) ** (1/p)



def euclidean_distance(X, row):
    return minkowski_distance(X,row,2)


def manhattan_distance(X, row):
    X_ = np.absolute(X - row)
    return np.sum(X_,axis=1)
    

def chebyshev_distance(X, row):
    X_ = np.maximum((np.absolute(X-row)),((np.absolute(X-row)**2)**1/5))

    return np.sum(X_,axis=1)