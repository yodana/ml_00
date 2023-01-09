import numpy as np
import matplotlib.pyplot as plt

def predict_(x, theta):
    if (isinstance(x, np.ndarray) == True or isinstance(theta, np.ndarray) == True):
        x = np.squeeze(x)
        if (x.ndim == 1 and len(x) != 0 and theta.shape == (2,1)):
            x = np.c_[ np.ones(len(x)) , x]
            y = x.dot(theta)
            return y
    return None

def loss_elem_(y, y_hat):
    j = []
    if (isinstance(y_hat, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        y_hat = np.squeeze(y_hat)
        if (y.ndim == 1 and y_hat.ndim == 1 and len(y) == len(y_hat)):
            for i in range(0, len(y)):
                j.append((y_hat[i] - y[i])**2)
            return np.array(j)
    return None

def loss_(y, y_hat):
    j = 0
    if (isinstance(y_hat, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        y = np.squeeze(y)
        y_hat = np.squeeze(y_hat)
        if (y.ndim == 1 and y_hat.ndim == 1 and len(y) == len(y_hat)):
            for i in range(0, len(y)):
                j = j + ((y_hat[i] - y[i])**2)
            return float(j / (2*len(y)))
    return None

if __name__ == '__main__':
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    y_hat1 = predict_(x1, theta1)
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])
    # Example 1:
    print(loss_elem_(y1, y_hat1))
    print(loss_(y1, y_hat1))
    x2 = np.array([0, 15, -9, 7, 12, 3, -21]).reshape(-1, 1)
    theta2 = np.array([[0.], [1.]]).reshape(-1, 1)
    y_hat2 = predict_(x2, theta2)
    y2 = np.array([2, 14, -13, 5, 12, 4, -19]).reshape(-1, 1)
    # Example 3:
    print(loss_(y2, y_hat2))
    print(loss_(y2, y2))