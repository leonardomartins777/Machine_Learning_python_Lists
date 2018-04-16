import numpy as np
import matplotlib
import matplotlib.pyplot as plt


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
        
class LogisticRegression (object):
    beta_ = 0
    

    def __init__(self):
        self.beta_ =  0.

    def fit(self,X, y):
        np.random.seed(3)
        num_pos = len(y)
        learning_rate = 0.0001
        iterations = 50000
        dataset = np.vstack((X, y))
        x = np.hstack((np.ones(num_pos*2).reshape(num_pos*2, 1), dataset))
        label = np.hstack((np.zeros(num_pos), np.ones(num_pos)))
        y = label.reshape(num_pos*2, 1)
        beta = np.zeros(x.shape[1]).reshape(x.shape[1], 1)
        for step in np.arange(iterations):
            x_beta = np.dot(x, beta)
            y_hat = 1 / (1 + np.exp(-x_beta))
            likelihood = np.sum(np.log(1 - y_hat)) + np.dot(y.T, x_beta)
            preds = np.round( y_hat )
            accuracy = np.sum(preds == y)*1.00/len(preds)
            gradient = np.dot(np.transpose(x), y - y_hat)
            beta = beta + learning_rate*gradient

        self.beta_ = beta
    
    def predict(self,X):
        x_beta = np.dot(x, beta)
        y_hat = 1 / (1 + np.exp(-x_beta))

        

