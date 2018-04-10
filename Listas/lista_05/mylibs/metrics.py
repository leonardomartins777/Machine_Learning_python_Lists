from math import sqrt
import numpy as np

def mse(y_true, y_pred):
    retorno = 0
    for x in range(len(y_true)):
        retorno = retorno + ((y_true[x] - y_pred[x]) ** 2)
    return (retorno / len(y_true))

def rmse(y_true, y_pred):
    return sqrt( mse(y_true, y_pred))

def mae(y_true, y_pred):
    retorno = 0
    for x in range(len(y_true)):
        retorno = retorno + (y_true[x] - y_pred[x])
    return (retorno / len(y_true))

    
def accuracy_score(y_true, y_pred, normalize=True):
    acc = 0
    for x in range(len(y_true)):
        if (y_true[x] == y_pred[x]):
            acc = acc + 1
    if normalize:
        acc = acc / len(y_true)
            
    return acc

def precision_score(y_true, y_pred):
    c_tam,c_idx = np.unique(y_true,return_index=True)
    PV = 0
    PF = 0
    for i in range(len(c_tam)):
        for x in range(len(y_true)):
            if (y_pred[x] == y_true[c_idx[i]]) and (y_true[x] == y_pred[x]):
                PV = PV + 1
            if (y_pred[x] == y_true[c_idx[i]]) and (y_true[x] != y_pred[x]):
                PF = PF +1
    PF = PF / len(c_tam)
    return ((PV) / (PV + PF))

def recall(y_true,y_pred):
    c_tam,c_idx = np.unique(y_true,return_index=True)
    PV = 0
    P = 0
    total = 0
    for i in range(len(c_tam)):
        for x in range(len(y_true)):
            if (y_pred[x] == y_true[c_idx[i]]) and (y_true[x] == y_pred[x]):
                PV = PV + 1
            P = P + 1
        total = total + (PV / P)
    return  total

def f1_measure(y_true,y_pred):
    return (2 * precision_score(y_true,y_pred) * recall(y_true,y_pred)) / ( precision_score(y_true,y_pred) + recall(y_true,y_pred)) 