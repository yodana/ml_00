import numpy as np
import matplotlib.pyplot as plt

def simple_predict(x, theta):
    if (isinstance(x, np.ndarray) == True or isinstance(theta, np.ndarray) == True):
        x = np.squeeze(x)
        theta = np.squeeze(theta)
        if (x.ndim == 1 and len(x) != 0 and theta.shape == (2,)):
            theta0 = theta[0]
            theta1 = theta[1]
            y = theta0 + theta1 * x
            return y
    return None

def loss_(y, y_hat):
    j = 0
    if (isinstance(y_hat, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        y = np.squeeze(y)
        y_hat = np.squeeze(y_hat)
        if (y.ndim == 1 and y_hat.ndim == 1 and len(y) == len(y_hat)):
            m = y_hat - y
            j = m.dot(m)
            return float(j / (2*len(y)))
    return None

def plot_with_loss(x, y, theta):
    if (isinstance(x, np.ndarray) == True or isinstance(theta, np.ndarray) == True or isinstance(y, np.ndarray) == True):
        theta = np.squeeze(theta)
        if (x.ndim == 1 and y.ndim == 1 and theta.shape == (2,)):
            plt.scatter(x, y)
            p = simple_predict(x, theta)
            print("p = ", p)
            plt.scatter(x, p)
            for i in range(0, len(x)):
                plt.plot([x[i], x[i]],[y[i], p[i]], '--', color="red")
            plt.title('Cost = ' + str(2*loss_(p, y)))
            plt.plot(x, p, color="orange")
            plt.show()
            plt.close()

if __name__ == '__main__':
    x = np.arange(1,6)
    y = np.array([11.52434424, 10.62589482, 13.14755699, 18.60682298, 14.14329568])
    # Example 1:
    theta1= np.array([18,-1])
    plot_with_loss(x, y, theta1)
    theta2 = np.array([14, 0])
    plot_with_loss(x, y, theta2)
    theta3 = np.array([12, 0.8])
    plot_with_loss(x, y, theta3)