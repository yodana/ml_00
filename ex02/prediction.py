import numpy as np

def simple_predict(x, theta):
    if (isinstance(x, np.ndarray) == True or isinstance(theta, np.ndarray) == True):
        if (x.ndim == 1 and len(x) != 0 and theta.shape == (2,)):
            theta0 = theta[0]
            theta1 = theta[1]
            y = theta0 + theta1 * x
            return y
    return None

if __name__ == '__main__':
    a = np.arange(1, 6)
    theta1 = np.array([5, 0])
    print(simple_predict(a, theta1))
    theta2 = np.array([0, 1])
    # Output:
    print(simple_predict(a, theta2))
    theta3 = np.array([5, 3])
    print(simple_predict(a, theta3))
    theta4 = np.array([-3, 1])
    print(simple_predict(a, theta4))
    a = np.array([5])
    print(simple_predict(a, theta1))