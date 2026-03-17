#del keyword
class Student:
    def __init__(self,name):
        self.name = name

s1= Student("subhajit")
print(s1.name)
del s1.name
print(s1.name)

#private attributes and method

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)    

acc1 = Account("11542896354","abgsd@1487")
print(acc1.acc_no)
print(acc1.reset_pass)    

#inheritance
# single inheritance
class Car:
    colour="black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod  
    def stop():
        print("car stoped..")

class ToyootaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = ToyootaCar("fortunar")
cae2 = ToyootaCar("Inova")        
print(car1.start())
print(car1.colour)

# multi_level inheritance

class Car:
    
    @staticmethod
    def start():
        print("car started..")

    @staticmethod  
    def stop():
        print("car stoped..")

class ToyootaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        
class Fortunar(ToyootaCar):  
    def __init__(self, type):
        self.type = type

car1 = Fortunar("petrol")
car1.start()  

#multiple inheritance
class A:
    varA ="welcome to kolkata"
class B :
    varB ="welcome to digha"

class C(A,B):
    varC = "welcome to ramnagar"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)   

# super method()
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod  
    def stop():
        print("car stoped..")

class ToyootaCar(Car):
    def __init__(self,name,type):
        self.name= name
        super().__init__(type)
        

car1 = ToyootaCar("Inova","electric")
print(car1.type)

#property 
class Student:
    def __init__(self,phy,math,chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    @property
    def persentage(self):
        return str((self.phy+ self.math+ self.chem)/3) + "%"

stu1 = Student(98,81,86)       
print(stu1.persentage)    
stu1.phy = 88
print(stu1.persentage)

#polymorphism
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownum(self):
        print(f"{self.real} + {self.img}i")

    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg  = self.img + num2.img
        return Complex(newreal, newimg)

    def __sub__(self, num2):
        newreal = self.real - num2.real
        newimg  = self.img - num2.img
        return Complex(newreal, newimg)


num1 = Complex(4, 3)
num1.shownum()

num2 = Complex(5, 9)
num2.shownum()

num3 = num1 + num2
num3.shownum()

num4 = num1 - num2
num4.shownum()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):   # usually singular form
        return 2 * (22/7) * self.radius


c1 = Circle(56)
print("Area:", c1.area())
print("Perimeter:", c1.perimeter())              


class Employee:
    def __init__(self,salary,role,dept):
        self.salary = salary
        self.role = role
        self.dept = dept

    def showdata(self):
        print("salary=", self.salary)
        print("role=",self.role)    
        print("dept =", self.dept)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name =name
        self.age = age
        super().__init__("engineer","IT","60000")

engg1 = Engineer("subhajit ", 22)
engg1.showdata()  


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

    def __str__(self):
        return f"Order(Item: {self.item}, Price: {self.price})"


# Example usage
order1 = Order("Laptop", 50000)
order2 = Order("Phone", 30000)

print(order1)   # Order(Item: Laptop, Price: 50000)
print(order2)   # Order(Item: Phone, Price: 30000)

# Comparison using >
if order1 > order2:
    print("Order1 is more expensive than Order2")
else:
    print("Order2 is more expensive than Order1")