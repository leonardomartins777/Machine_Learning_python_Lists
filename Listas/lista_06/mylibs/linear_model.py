import numpy as np

class SimpleLinearRegression(object):
    b0 = 0.
    b1 = 0.

    def __init__(self):
        self.b0 = 0.
        self.b1 = 0.
    
    def fit(self,X, y):
        y_ = [ [i] for i in y ]
        self.b1 = np.sum((X - np.mean(X)) * (y_ - np.mean(y_))) / np.sum((X - np.mean(X)) ** 2) 
        
        self.b0 = np.mean(y_) - self.b1 * np.mean(X)
    
    def predict(self,X):
        retorno = []
        for x in range(len(X)):
            retorno.append(self.b0 + (self.b1 * X[x]))
        return np.array(retorno)
        
    