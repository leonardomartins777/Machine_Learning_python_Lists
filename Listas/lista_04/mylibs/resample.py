import numpy as np

def split_train_test(n_elem, perc_train, seed):
    a = [ i for i in range(n_elem)]
    np.random.seed(seed)
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


def split_k_fold(n_elem, n_splits=3, shuffle=True, seed=0):
    a = [ i for i in range(n_elem)]
    np.random.seed(seed)
    if shuffle == True:
        np.random.shuffle(a)
    n_test = int(round(n_elem * (1.0 / n_splits)))

    train = []
    test = []

    for i in range(n_splits):
        train_Aux = []
        test_Aux = []
        test_Aux = a[i*n_test:i*n_test + n_test]
        for x in a:
            if x not in test_Aux:
                train_Aux.append(x)



        
        train.append(train_Aux)
        test.append(test_Aux)

    return np.array(train),np.array(test)
