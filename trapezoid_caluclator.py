#calculator for right angle trapezoids
import math

class trapezoid:
    def __init__(self, height, base, top):
        self.def_list = [height, base, top]

        assert len(self.def_list) == 3 #all three items must be defined
        assert self.def_list[0] > 0 and self.def_list[1] > 0 and self.def_list[2] >= 0 #the base and height must be bigger than 0
        assert self.def_list[1] > self.def_list[2]

    def get_height(self): 
        height = float(self.def_list[0])
        return height
    
    def get_base(self):
        base = float(self.def_list[1])
        return base
    
    def get_top(self):
        top = float(self.def_list[2])
        return top

    def calc_mid(self): #calculates the value of the mid
        self.mid = float((self.def_list[1] + self.def_list[2])/2)
        return self.mid
    
    def calc_area(self): #calculates the area of the right trapezoid
        self.area = float(trap.calc_mid() * self.def_list[0])
        return self.area

a = float(input("Enter the height of the trapezoid: "))
b = float(input("Enter the base of the trapezoid: "))
c = float(input("Enter the top of the trapezoid: "))

trap = trapezoid(a, b, c)

print("height, base and top are: ", trap.get_height(), trap.get_base(), trap.get_top())

print("the calculated midline and area are: ", trap.calc_mid(), trap.calc_area())
      

def test1():
    assert trap.get_height() == a \
    and trap.get_base() == b\
    and trap.get_top() == c

def test2():
    assert trap.calc_mid == (b+c)/2

def test3():
    assert trap.calc_area == ((b+c)/2) * a

#test1()
#test2()
#test3()