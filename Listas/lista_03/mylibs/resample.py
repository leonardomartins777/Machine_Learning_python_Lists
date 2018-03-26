import numpy as np

def split_train_test(n_elem, perc_train, seed):
    a = [ i for i in range(n_elem)]
    np.random.seed(0)
    np.random.shuffle(a)
    tam = perc_train * n_elem
    train = []
    test = []
    count = 0
    for i in range(len(a)):
        if count < tam:
            train.append(a[i])
        else:
            test.append(a[i])
        count = count + 1
    return train,test
