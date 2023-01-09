import numpy as np

def add_intercept(x):
    if (isinstance(x, np.ndarray) == True):
        if (len(x) != 0):
            x = np.c_[ np.ones(len(x)) , x]
            return x
    return None

if __name__ == '__main__':
    x = np.arange(1,6)
    print(add_intercept(x))
    # Example 2:
    y = np.arange(1,10).reshape((3,3))
    print(add_intercept(y))