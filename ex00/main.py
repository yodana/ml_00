from matrix import *

if __name__ == '__main__':
    m = Matrice([[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6]])
    print(m.matrice)
    m1 = Matrice([[0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6]])
    print(m1.matrice)
    add = m + m1
    print(add.matrice)
    radd = m1 + m
    print(add.matrice)
    v = Vector([[0], [1], [1, 2]])