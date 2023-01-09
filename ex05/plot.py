import numpy as np
import matplotlib.pyplot as plt

def simple_predict(x, theta):
    if (isinstance(x, np.ndarray) == True or isinstance(theta, np.ndarray) == True):
        x = np.squeeze(x)
        if (x.ndim == 1 and len(x) != 0 and theta.shape == (2,1)):
            theta0 = theta[0]
            theta1 = theta[1]
            y = theta0 + theta1 * x
            return y
    return None

def plot(x, y, theta):
    if (isinstance(x, np.ndarray) == True or isinstance(theta, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        if (x.ndim == 1 and y.ndim == 1 and theta.shape == (2,1)):
            plt.scatter(x, y)
            y = simple_predict(x, theta)
            plt.plot(x, y, color="orange")
            plt.show()

if __name__ == '__main__':
    x = np.arange(1,6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
    # Example 1:
    theta1 = np.array([[4.5],[-0.2]])
    plot(x, y, theta1)
    theta2 = np.array([[-1.5],[2]])
    plot(x, y, theta2)
    theta3 = np.array([[3],[0.3]])
    plot(x, y, theta3)