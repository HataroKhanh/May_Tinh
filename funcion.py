from cmath import cos, acos, pi, sqrt
from sympy import symbols, Eq, solve  # Vã lắm mới dùng thư viện huhu
from re import split
from math import degrees


def cbrt(x):
    return x ** (1/3)


def math(a):
    if [char for char in a if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '%', '/', '^', '*', '(', ')']]:
        return round(eval(a), 5)
    else:
        return 'Vui Long Nhap Lai'


def sapxep(a):
    a = [float(i) for i in a]
    n = len(a)
    for i in range(n):
        for j in range(i+1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return ' '.join(str(i) for i in a)


def dungsai(a):
    bangchucai = split(r'([<=>]+)', a)
    l = [item for item in bangchucai if item]
    if len(l) > 2:
        lr = round(eval(l[0]), 5)
        ll = round(eval(l[2]), 5)
        result = None
        if l[1] == '<=':
            result = (lr <= ll)
        elif l[1] == '=':
            result = (lr == ll)
        elif l[1] == '>=':
            result = (lr >= ll)
        elif l[1] == '<':
            result = (lr < ll)
        elif l[1] == '>':
            result = (lr > ll)
        if result == True and len(l) == 5:
            lr = ll
            ll = round(eval(l[4]), 5)
            if l[3] == '<=':
                result = (lr <= ll)
            elif l[3] == '=':
                result = (lr == ll)
            elif l[3] == '>=':
                result = (lr >= ll)
            elif l[3] == '<':
                result = (lr < ll)
            elif l[3] == '>':
                result = (lr > ll)
        return result
    else:
        return 'Thong Tin Nhap Chua Chinh Xac,Vui Long Nhap Lai'


def phuongtrinhbacnhat(a, b):
    if a == 00:
        return 'Vo Nghiem'
    else:
        return -b/a


def phuongtrinhbachai(a, b, c):
    delta = b**2-(4*a*c)
    if delta < 0:
        return 'Vo Nghiem'
    else:
        return (-b+(delta**0.5))/(2*a), (-b-(delta**0.5))/(2*a)


def phuongtrinhbacba(a, b, c, d):
    if a != 0:
        delta = b**2 - 3*a*c
        if delta > 0:
            x1 = (-b + sqrt(delta))/(3*a)
            x2 = (-b - sqrt(delta))/(3*a)
            return x1, x2
        elif delta == 0:
            x = -b/(3*a)
            return x
        else:
            p = (3*a*c - b**2)/(3*a**2)
            q = (2*b**3 - 9*a*b*c + 27*a**2*d)/(27*a**3)
            k = (q/2)**2 + (p/3)**3

            if k < 0:
                r = sqrt(-k)
                acos = acos(-q/(2*r))
                x1 = 2*cbrt(sqrt(-p**3/27))*cos(acos/3)-b/(3*a)
                x2 = 2*cbrt(sqrt(-p**3/27))*cos((acos+2*pi)/3)-b/(3*a)
                x3 = 2*cbrt(sqrt(-p**3/27))*cos((acos+4*pi)/3)-b/(3*a)
                return x1, x2, x3
            elif k == 0:
                x1 = -2*cbrt(q/2)-b/(3*a)
                x2 = cbrt(q/2)-b/(3*a)
                return x1, x2
            else:
                r = sqrt(k)
                u = cbrt(r-q/2)
                v = -cbrt(r+q/2)
                x1 = u+v-b/(3*a)
                return x1
    else:
        return 'Day khong phai la phuong trinh bac ba'


def phuongtrinhbacbon(a,b,c,d,e):
    x = symbols('x')
    kq = Eq(a*x**4 + b*x**3 + c*x**2 + d*x + e, 0)
    ketqua = solve(kq, x)
    return ketqua


def phuongtrinhbacnam(a,b,c,d,e,f):
    x = symbols('x')
    kq = Eq(a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f, 0)
    ketqua = solve(kq, x)
    return ketqua


class Vector_2_Chieu():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cong(self, new_v):
        return self.x + new_v.x, self.y + new_v.y

    def tru(self, new_v):
        return self.x - new_v.x, self.y - new_v.y

    def nhan(self, new_v):
        return self.x * new_v.x, self.y * new_v.y

    def chia(self, new_v):
        return self.x / new_v.x, self.y / new_v.y

    def tichvohuong(self, new_v):
        return self.x * new_v.x + self.y * new_v.y

    def gocgiuahaiduongthang(self, new_v):
        a = abs(self.x * new_v.x + self.y * new_v.y) / (sqrt(self.x **
                                                             2 + self.y ** 2) * sqrt(new_v.x ** 2 + new_v.y ** 2))
        b = acos(a)
        return degrees(b.real)


class Vector_3_Chieu():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def cong(self, new_v): return self.x + \
        new_v.x, self.y+new_v.y, self.z+new_v.z

    def tru(self, new_v): return self.x-new_v.x, self.y-new_v.y, self.z-new_v.z

    def nhan(self, new_v): return self.x * \
        new_v.x, self.y*new_v.y, self.z*new_v.z

    def chia(self, new_v): return self.x / \
        new_v.x, self.y/new_v.y, self.z/new_v.z

    def tichvohuong(self, new_v): return self.x * \
        new_v.x+self.y*new_v.y+self.z*new_v.z

    def gocgiuahaiduongthang(self, new_v):
        a = abs(self.x*new_v.x+self.y+new_v.y+self.z+new_v.z)/(sqrt(self.x **
                                                                    2+self.y**2+self.z**2)*sqrt(new_v.x**2+new_v.y**2+new_v.z**2))
        b = acos(a)
        return degrees(b.real)


class thongke():
    def __init__(self, a):
        self.a = a

    def tong(self):
        return round(sum(self.a), 5)

    def sophantu(self):
        return len(self.a)

    def trungbinh(self):
        return self.tong() / self.sophantu()

    def min(self):
        return min(self.a)

    def max(self):
        return max(self.a)

    def trungvi(self):
        sorted_a = sorted(self.a)
        n = len(self.a)
        if n % 2 != 0:
            return sorted_a[(n + 1) // 2 - 1]
        else:
            a1 = sorted_a[n // 2 - 1]
            a2 = sorted_a[n // 2]
            return (a1 + a2) / 2

    def quartiles(self):
        sorted_a = sorted(self.a)
        n = len(self.a)
        q1 = sorted_a[(n + 1) // 4 - 1]
        q2 = self.trungvi()
        q3 = sorted_a[(3 * (n + 1)) // 4 - 1]
        return q1, q2, q3
    		


