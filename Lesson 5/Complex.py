class Complex(object):
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __add__(self, other):
        new = Complex(self.Re + other.Re, self.Im + other.Im)
        return new

    def __sub__(self, other):
        new = Complex(self.Re - other.Re, self.Im - other.Im)
        return new

    def __mul__(self, other):
        new = Complex(self.Re*other.Re - self.Im*other.Im,
                      self.Re*other.Im + other.Re*self.Im)
        return new

    def __truediv__(self, other):
        new = Complex((self.Re*other.Re + self.Im*other.Im)/
                      (other.Re**2 + other.Im**2),
                      (self.Im*other.Re - self.Re*other.Im)/
                      (other.Re**2 + other.Im**2))
        return new

    def mod(self):
        new = Complex((self.Re**2 + self.Im**2)**(1/2), 0)
        return new

    def __str__(self):
        s = '+'
        if self.Im < 0: s = ''
        return '{:.2f}{}{:.2f}i'.format(self.Re, s, self.Im)



print('Please, enter 2 complex numbers:')
num1 = list(map(int, input().split(sep=' ')))
num2 = list(map(int, input().split(sep=' ')))
num1 = Complex(num1[0], num1[1])
num2 = Complex(num2[0], num2[1])
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1.mod())
print(num2.mod())
