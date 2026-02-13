class Complex:
    def __init__(self, r=0.0, i=0.0):
        self.__real = r
        self.__img = i
    def __add__(self, other):
        c3 = Complex()
        c3.__real = self.__real + other.__real
        c3.__img = self.__img + other.__img
        return c3
    def __sub__(self, other):
        c3 = Complex()
        c3.__real = self.__real - other.__real
        c3.__img = self.__img - other.__img
        return c3
    def print_complex(self):
        print(f"({self.__real}+{self.__img}j)")
        

comp1 = Complex()
comp1.print_complex()
print()

comp2 = Complex(1.5,2.5)
comp2.print_complex()
print()

comp3 = Complex(2.5,4.0)
comp3.print_complex()
print()

comp4 = comp2 + comp3
comp4.print_complex()
print()

comp5 = comp2 - comp3
comp5.print_complex()
