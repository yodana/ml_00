import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import math
def mse_(y, y_hat):
    j = 0
    if (isinstance(y_hat, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        y = np.squeeze(y)
        y_hat = np.squeeze(y_hat)
        if (y.ndim == 1 and y_hat.ndim == 1 and len(y) == len(y_hat)):
            m = y_hat - y
            j = m.dot(m)
            return float(j / (len(y)))
    return None

def rmse_(y, y_hat):
    j = 0
    if (isinstance(y_hat, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        y = np.squeeze(y)
        y_hat = np.squeeze(y_hat)
        if (y.ndim == 1 and y_hat.ndim == 1 and len(y) == len(y_hat)):
            m = y_hat - y
            j = m.dot(m)
            return float(math.sqrt(j / (len(y))))
    return None

def mae_(y, y_hat):
    j = 0
    if (isinstance(y_hat, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        y = np.squeeze(y)
        y_hat = np.squeeze(y_hat)
        if (y.ndim == 1 and y_hat.ndim == 1 and len(y) == len(y_hat)):
            j = y_hat - y
            j = np.sum(np.absolute(j), axis=0)
            return float(j / (len(y)))
    return None

def r2score_(y, y_hat):
    j = 0
    if (isinstance(y_hat, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        y = np.squeeze(y)
        y_hat = np.squeeze(y_hat)
        if (y.ndim == 1 and y_hat.ndim == 1 and len(y) == len(y_hat)):
            m = y_hat - y
            j = m.dot(m)
            m = y - np.mean(y)
            j2 = m.dot(m)
            return float(1 - (j / j2))
    return None

if __name__ == '__main__':
    x = np.array([0, 15, -9, 7, 12, 3, -21])
    y = np.array([2, 14, -13, 5, 12, 4, -19])
    # Mean squared error
    ## your implementation
    print(mse_(x,y))
    ## Output:
    print(mean_squared_error(x,y))
    print(rmse_(x,y))
    print(math.sqrt(mean_squared_error(x,y)))
    print(mae_(x,y))
    print(mean_absolute_error(x,y))
    print(r2score_(x,y))
    print(r2_score(x,y))