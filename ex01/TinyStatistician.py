import numpy as np
import math as math
class TinyStatistician():
    def mean(self, x):
        r = 0
        if (isinstance(x, list) == True or isinstance(x, np.ndarray) == True):
            if (len(x) != 0):
                for i in range(0, len(x)):
                    r = r + x[i]
                r = r / len(x)
                return r 
        return None

    def median(self, x):
        r = 0
        if (isinstance(x, list) == True or isinstance(x, np.ndarray) == True):
            x = sorted(x)
            if (len(x) != 0):
                if ((len(x) % 2) == 1):
                    return float(x[int((len(x) / 2))])
                else:
                    return float((x[int((len(x) / 2)) - 1] +  x[(int(len(x) / 2))]) / 2)
        return None
    
    def quartile(self, x):
        r = 0
        s = []
        if (isinstance(x, list) == True or isinstance(x, np.ndarray) == True):
            x = sorted(x)
            if (len(x) != 0):
                if ((len(x) % 2) == 1):
                    s.append(float(x[int((len(x) / 4))]))
                else:
                    s.append(float((x[int((len(x) / 4)) - 1] +  x[(int(len(x) / 4))]) / 2))
        if (isinstance(x, list) == True or isinstance(x, np.ndarray) == True):
            if (len(x) != 0):
                if ((len(x) % 2) == 1):
                   s.append(float(x[int((len(x) * 0.75))]))
                else:
                   s.append(float((x[int((len(x) * 0.75)) - 1] +  x[(int(len(x) * 0.75))]) / 2))
            return s
        return None
    
    def percentile(self, x, p):
        r = 0
        p = p / 100
        if ((isinstance(x, list) == True or isinstance(x, np.ndarray) == True) and (p >= 0 and p <= 1)):
            x = sorted(x)
            if (len(x) != 0):
                if (p == 1):
                    return float(x[int((len(x) * p)) - 1])
                if ((len(x) % 2) == 1):
                    return float(x[int((len(x) * p))])
                else:
                    return float((x[int((len(x) * p)) - 1] +  x[(int(len(x) * p))]) / 2)
        return None
    
    def var(self, x):
        ret = 0
        if ((isinstance(x, list) == True or isinstance(x, np.ndarray) == True)):
            x = sorted(x)
            mean = self.mean(x)
            if (len(x) != 0):
                for d in x:
                    ret = ret + (d - mean)**2
                return float(ret / len(x))
        return None

    def std(self, x):
        ret = 0
        if ((isinstance(x, list) == True or isinstance(x, np.ndarray) == True)):
            x = sorted(x)
            mean = self.mean(x)
            if (len(x) != 0):
                for d in x:
                    ret = ret + (d - mean)**2
                return float(math.sqrt(ret / len(x)))
        return None

if __name__ == '__main__':
    m = np.array([1, 2, 3.0])
    print(type(m))
    m = [1, 2, 3.0]
    print(type(m))
    a = [1, 42, 300, 10, 59]
    r = TinyStatistician().mean(a)
    print(r)
    a = []
    r = TinyStatistician().mean(a)
    print(r)
    a = np.array([1, 42, 300, 10, 59])
    r = TinyStatistician().mean(a)
    print(r)
    a = 1
    r = TinyStatistician().mean(a)
    print(r)
    a = [1, 42, 300, 10, 59]
    r = TinyStatistician().median(a)
    print(r)
    a = [1, 2, 3, 4]
    r = TinyStatistician().median(a)
    print(r)
    a = [1, 42, 300, 10, 59]
    r = TinyStatistician().quartile(a)
    print(r)
    a = [1, 2, 3, 4]
    r = TinyStatistician().quartile(a)
    print(r)
    a = [1, 42, 300, 10, 59]
    r = TinyStatistician().percentile(a, 100)
    print(r)
    a = [1, 2, 3, 4]
    r = TinyStatistician().percentile(a, 20)
    print(r)
    a = [1, 42, 300, 10, 59]
    r = TinyStatistician().var(a)
    print(r)
    a = [1, 2, 3, 4]
    r = TinyStatistician().var(a)
    print(r)
    a = [1, 42, 300, 10, 59]
    r = TinyStatistician().std(a)
    print(r)
    a = [1, 2, 3, 4]
    r = TinyStatistician().std(a)
    print(r)
     a = [1, 42, 300, 10, 59]
    r = TinyStatistician().std(a)
    print(r)
    a = [1, 2, 3, 4]
    r = TinyStatistician().std(a)
    print(r)