class Person:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


person = Person(4, 7)
print(person.add())

if __name__ == '__main__':
    import doctest
    doctest.testmod()
