import numpy as np

def predict_(x, theta):
    if (isinstance(x, np.ndarray) == True or isinstance(theta, np.ndarray) == True):
        x = np.squeeze(x)
        if (x.ndim == 1 and len(x) != 0 and theta.shape == (2,1)):
            x = np.c_[ np.ones(len(x)) , x]
            y = x.dot(theta)
            return y
    return None

if __name__ == '__main__':
    x = np.arange(1,6)
    theta1 = np.array([[5], [0]])
    print(predict_(x, theta1))
    # Do you remember why y_hat contains only 5’s here?
    # Example 2:
    theta2 = np.array([[0], [1]])
    print(predict_(x, theta2))
    # Do you remember why y_hat == x here?
    # Example 3:
    theta3 = np.array([[5], [3]])
    print(predict_(x, theta3))
    # Example 4:
    theta4 = np.array([[-3], [1]])
    print(predict_(x, theta4))
    x = np.arange(0,1)
    print(predict_(x, theta4))