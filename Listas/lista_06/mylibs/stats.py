from math import sqrt

def mean(x):
    retorno = 0
    for i in x:
        retorno = retorno + i
    return retorno/len(x)

def stdev(x):
    retorno = 0
    media = mean(x)
    for i in x:
        retorno = retorno + ((i - media)**2)
    retorno = retorno / len(x)
    return sqrt(retorno)

def var(y):
    retorno = 0
    media = mean(y)
    for i in y:
        retorno = retorno + ((i - media)**2)
    retorno = retorno / len(y)
    return retorno
