import sys
if len(sys.argv) <= 2:
    print("Usage: python bodmas.py <a> <b>")
    raise ValueError ("You must specify the agument variables to perform the operation")
class Bodmas:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def bracket(self):
        a = int(self.a)
        b = int(self.b)
        return('The bracket of {} and {} is; {}\n'.format(self.a, self.b, a * b))
    def order(self):
        a = int(self.a)
        b = int(self.b)
        return('The order of {} and {} is; {}\n'.format(self.a, self.b, a ** b))
    def division(self):
        a = int(self.a)
        b = int(self.b)
        return('The division of {} and {} is; {:.2f}\n'.format(self.a, self.b, a / b))
    def multiplication(self):
        a = int(self.a)
        b = int(self.b)
        return('The multiplication of {} and {} is; {}\n'.format(self.a, self.b, a * b))
    def addition(self):
        a = int(self.a)
        b = int(self.b)
        return('The addition of {} and {} is; {}\n'.format(self.a, self.b, a + b))
    def subtraction(self):
        a = int(self.a)
        b = int(self.b)
        return('The subtraction of {} and {} is; {}\n'.format(self.a, self.b, a - b))



b=Bodmas(sys.argv[-2],sys.argv[-1])

print(b.bracket(),
b.order(),
b.division(),
b.multiplication(),
b.addition(),
b.subtraction(), end="\n")