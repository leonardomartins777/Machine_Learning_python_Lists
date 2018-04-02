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

    


