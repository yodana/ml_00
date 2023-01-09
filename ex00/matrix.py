class Matrice(object):
    def __init__(self,  data):
        if isinstance(data, list):
            self.matrice = data
        elif isinstance(data, tuple):
            self.matrice = self.fill_zero(data)
        self.s = self.shape(self.matrice)
    
    def fill_zero(self, data):
        l = [[0]*data[1] for i in range(data[0])]
        return l

    def shape(self, m):
        try:
            s = [len(matrice) for matrice in m]
        except:
            print("Error: matrix shape not conform")
            exit(1)
        check = [all(element == s[0] for element in s)]
        if check[0]:
            if s == []:
                self.square = True
                return ("0x0")
            else:
                if s[0] == len(m):
                    self.square = True
                return str(len(m)) + "x" + str(s[0])
        else:
           print("Error: Matrice is not the same shape in columns")
           exit(1)
    
    def __add__(self, matrice):
        m = matrice.matrice
        print(self.s, matrice.s)
        if (self.s != matrice.s):
            print("Not the same shape")
            exit(1)
        r = [[round(self.matrice[j][i] + m[j][i], 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        if (isinstance(self, Vector)):
            return Vector(r)
        if (isinstance(self, Matrice)):
            return Matrice(r)
    
    def __radd__(self, matrice):
        m = matrice.matrice
        if (self.s != matrice.s):
            print("Not the same shape")
            exit(1)
        r = [[round(m[j][i] + self.matrice[j][i], 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        if (isinstance(self, Vector)):
            return Vector(r)
        if (isinstance(self, Matrice)):
            return Matrice(r)
    
    def __sub__(self, matrice):
        m = matrice.matrice
        if (self.s != matrice.s):
            print("Not the same shape")
            exit(1)
        r = [[round(self.matrice[j][i] - m[j][i], 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        if (isinstance(self, Vector)):
            return Vector(r)
        if (isinstance(self, Matrice)):
            return Matrice(r)

    def __rsub__(self, matrice):
        m = matrice.matrice
        if (self.s != matrice.s):
            print("Not the same shape")
            exit(1)
        r = [[round(m[j][i] - self.matrice[j][i], 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        if (isinstance(self, Vector)):
            return Vector(r)
        if (isinstance(self, Matrice)):
            return Matrice(r)
    
    def __truediv__(self, scalar):
        if (scalar == 0):
            print("Divide by 0 impossible")
            exit(1)
        r = [[round(self.matrice[j][i] / scalar, 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        if (isinstance(self, Vector)):
            return Vector(r)
        if (isinstance(self, Matrice)):
            return Matrice(r)

    def __rtruediv__(self, scalar):
        if (scalar == 0):
            print("Divide by 0 impossible")
            exit(1)
        r = [[round(self.matrice[j][i] / scalar, 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        if (isinstance(self, Vector)):
            return Vector(r)
        if (isinstance(self, Matrice)):
            return Matrice(r)
    
    def __mul__(self, scalar):
        if (isinstance(scalar, int) or isinstance(scalar, float)):
            r = [[round(self.matrice[j][i] * scalar, 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        else:
            if (self.s[2] != scalar.s[0]):
                print("Mul impossible")
                exit(0)
            mat = scalar.matrice
            r = []
            i = 0
            k = 0
            for c in self.matrice:
                empty = [0 for i in range(0, int(scalar.s[2]))]
                print(empty)
                for m in mat:
                    for n in m:
                        empty[i] = empty[i] + c[k]*n
                        i = i + 1
                    i = 0
                    k = k + 1
                r.append(empty)
                k = 0
        if (isinstance(self, Matrice)):
            return Matrice(r)

    def T(self):
        m = self.matrice
        t = [[0 for m in range(0,len(m))] for matrice in range(0, len(m[0]))]
        x = 0
        y_t = 0
        x_t = 0
        for l in m:
            for x in range(0, len(m[0])):
                t[y_t][x_t] = l[x]
                y_t = y_t + 1
            x_t = x_t + 1
            y_t = 0
        return Matrice(t)

class Vector(Matrice):
    def __init__(self, column):
        if (len(column) != 1):
            for i in range(0, len(column)):
                if len(column[i]) != 1:
                    print("Error: that's not the syntax of a Vector")
                    exit(1)
        self.matrice = column
        self.s = self.shape(column)

    def mul_vec(self, vec):
        new = []
        if len(vec.vector) != len(self.matrice):
            print("Error: not the same shape")
            exit(1)
        i = 0
        r = 0
        for m in self.matrice:
            for n in m:
                r = r + n*vec.vector[i]
                i = i + 1
            new.append(r)
            r = 0
            i = 0
        return Vector(new)   
    """
    def print(self):
        p = [[m for m in matrice] for matrice in self.matrice]
        print(p)
    

    def res(self):
        m = [val for matrice in self.matrice for val in matrice]
        return Vector(m)
    
    def sub(self, m):
        m = m.matrice
        if self.complex == 1:
            r = [[(round(self.matrice[j][i].real, 9) + round(self.matrice[j][i].imag, 9)*1j) - (round(m[j][i].real, 9) + (round(m[j][i].imag, 9)*1j)) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
            return Matrice(r)
        r = [[round(self.matrice[j][i] - m[j][i], 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        return Matrice(r)

    def scl(self, k):
        m = []
        r = []
        if self.complex == 1:
            for j in range(0, len(self.matrice)):
                for i in range(0, len(self.matrice[0])):
                    res = k*self.matrice[j][i]
                    m.append(res)
                r.append(m)
                m = []
            return(Matrice(r))
        r = [[round(k*self.matrice[j][i], 9) for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        return Matrice(r)
    
    def mul_vec(self, vec):
        new = []
        if len(vec.vector) != len(self.matrice):
            print("Error: not the same shapeize")
            exit(1)
        i = 0
        r = 0
        for m in self.matrice:
            for n in m:
                r = r + n*vec.vector[i]
                i = i + 1
            new.append(r)
            r = 0
            i = 0
        return Vector(new)

    def mul_mat(self, mat):
        mat = mat.matrice
        new = []
        i = 0
        k = 0
        for c in self.matrice:
            empty = [0 for i in range(0, len(self.matrice[0]))]
            for m in mat:
                for n in m:
                    empty[i] = empty[i] + c[k]*n
                    i = i + 1
                i = 0
                k = k + 1
            new.append(empty)
            k = 0
        return Matrice(new)
    
    def trace(self):
        i = 0
        r = 0
        if self.square:
            for m in self.matrice:
                r = r + m[i]
                i = i + 1
            return r
        else:
            print("Error: matrix is not square")
            exit(1)

    def gaussian(self):
        m = [[self.matrice[j][i] for i in range(0, len(self.matrice[0]))] for j in range(0, len(self.matrice))]
        l = len(m)
        r,y,j,p = -1, 0, 0, 0
        t_pivot = []
        if self.complex == 1:
            m_i = [[0 + 0j for m in range(0,len(m[0]))] for matrice in range(0, l)]
            for x in range(0, l):
                if y < len(m[0]):
                    m_i[x][y] = 1 + 0j
                y = y + 1
        else:
            m_i = [[0 for m in range(0,len(m[0]))] for matrice in range(0, l)]
            for x in range(0, l):
                if y < len(m[0]):
                    m_i[x][y] = 1
                y = y + 1
        y = 0
        for c in range(0, len(m[0])):
            pivot = 0
            pivot_r = 0
            for x in range(r+1, l):
                if self.complex == 1:
                    module = ((m[x][y].real * m[x][y].real + m[x][y].imag * m[x][y].imag)**0.5)
                    if module > pivot_r:
                        pivot = m[x][y]
                        pivot_r = module
                        k = j
                    j += 1
                else:
                    if abs(m[x][y]) > pivot:
                        pivot = m[x][y]
                        k = j
                    j += 1
            t_pivot.append(pivot)
            if pivot != 0:
                r = r+1
                m[k] = Vector(m[k]).scl(1/pivot).vector
                m_i[k] = Vector(m_i[k]).scl(1/pivot).vector
                if k != r:
                    p = p+1
                    save = m[k]
                    m[k] = m[r]
                    m[r] = save
                    save = m_i[k]
                    m_i[k] = m_i[r]
                    m_i[r] = save
                for i in range(0, l):
                    if i != r:
                        vec1, vec2 = Vector(m[i]), Vector(m[r])
                        coeff = m[i][y]
                        res = vec1.sub(vec2.scl(coeff))
                        m[i] = res.vector
                        vec1, vec2 = Vector(m_i[i]), Vector(m_i[r])
                        res = vec1.sub(vec2.scl(coeff))
                        m_i[i] = res.vector
            j = r+1
            y = y+1
        y = 0
        for x in range(0, l):
            if all(x == 0 for x in m[x]):
                m.append(m[x])
                del m[y]
            y = y + 1
        return m, m_i, t_pivot, p

    def row_echelon(self):
        ret = self.gaussian()
        return Matrice(ret[0])
    
    def determinant(self):
        m = self.matrice
        t_pivot = []
        p = 0
        if len(m) > 4:
            return 0
        if len(m) <= 2:
            if len(m) == 1:
                return m[0]
            else:
                return m[0][0] * m[1][1] - m[1][0] * m[0][1]
        if len(m) >= 3:
            ret = self.gaussian()
            p = ret[3]
            t_pivot = ret[2]
            res = 1
            if p % 2 == 0:
                neg = 1
            else:
                neg = -1
            for x in t_pivot:
                res = res * x
            res = res * neg
            if self.complex == 1:
                return (round(res.real, 1) + round(res.imag, 1) *1j)
            return round(res, 1)
    
    def inverse(self):
        ret = self.gaussian()
        m_i = ret[1]
        t_pivot = ret[2]
        res = 1
        for x in t_pivot:
            res = res * x
        if res != 0:
            return Matrice(m_i)
        else:
            print("Error: the matrix is singular")
            exit(1)

    def rank(self):
        l = len(self.matrice)
        rank = l
        ret = self.gaussian()
        m = ret[0]
        for x in range(0, l):
            if all(x == 0 for x in m[x]):
                rank = rank-1
        return rank
    
    def transpose(self):
        m = self.matrice
        t = [[0 for m in range(0,len(m))] for matrice in range(0, len(m[0]))]
        x = 0
        y_t = 0
        x_t = 0
        for l in m:
            for x in range(0, len(m[0])):
                t[y_t][x_t] = l[x]
                y_t = y_t + 1
            x_t = x_t + 1
            y_t = 0
        return Matrice(t)

def linear_combination(v, k):
    i = 0
    for vector in v:
        if i == 0:
            u = vector.scl(k[i])
        else:
            u = u.add(vector.scl(k[i]))
        i = i + 1
    return u

def lerp(v, u, t):
    if type(v) != type(u):
        print("Error: not the same type")
        exit(1)
    if t >= 0 and t <= 1:
        try:
            r = v.add(u.sub(v).scl(t))
        except:
            r = v + ((u - v) * t)
        return r
    else:
        print("Error: t not between 0 and 1")
        exit(1)

def angle_cos(u, v):
    c = u.dot(v) / (u.norm() * v.norm())
    if u.complex == 1 or v.complex == 1:
        return (round(c.real,9) + round(c.imag, 9)*1j)
    return round(c, 9)

def cross_product(u, v):
    u = u.vector
    v = v.vector
    return Vector([u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]])"""