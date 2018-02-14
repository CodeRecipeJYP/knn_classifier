import pickle
import numpy as np
import os

dirname = "cifar-10-batches-py"
def load_CIFAR_batch(filename):
    """ load single batch of cifar """
    with open(filename, 'rb') as f:
        datadict = pickle.load(f, encoding="latin-1")
        X = datadict['data']
        Y = datadict['labels']
        X = X.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
        Y = np.array(Y)

        return X, Y


def loadBatch():
    index = 1
    filename = "data_batch_" + str(index)

    fullpath = os.path.join(dirname, filename)

    return load_CIFAR_batch(fullpath)

def loadTest():
    filename = "test_batch"

    fullpath = os.path.join(dirname, filename)

    return load_CIFAR_batch(fullpath)