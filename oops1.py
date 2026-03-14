#creating class
class Student:
    name = "subhajit sahoo"
#creating object(instance)
s1 = Student()
print(s1.name)

class Car:
    colour = "blue"
    brand= "BMW"

c1 = Car()
print(c1.colour)
print(c1.brand)

# constructor
class Student:
    #default constructor
    def __init__(self):
        pass
    # parameterised constructor
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in database")

s1 = Student("subhajit", 98)      
print(s1.name,s1.marks)
s2=Student("suman", 100)
print(s2.name,s2.marks)

#class & instance attributes

class Student:
    college_name = "Narula institute of technology"
    
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in college database")

s1 = Student("subhajit", 96)
print(s1.name,s1.marks)
s2 = Student("sougata" ,95)
print(s2.name,s2.marks)        
print(s1.college_name)

#Methods
class Student:
    college_name = "Narula institute of technology"
    
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        print("adding new student in college database")
    def welcome(self):
        print("welcome students", self.name)    
    def get_marks(self):
        return self.marks

s1 = Student("subhajit", 96)
s1.welcome()
print(s1.get_marks())

# create a student class that takes name and marks of 3 subject as argument in constructor then create a 
#methode to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum =0
        for val in self.marks:
            sum +=val
        print(self.name,"avg scord is:", sum/3)
                    #OR
        #total = sum(self.marks)      
       # avg = total / len(self.marks) 
        #print(self.name, "avg score is:", avg)


s1 = Student("subhajit", [95, 68, 97])
s1.get_avg()

#ststic method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum =0
        for val in self.marks:
            sum +=val
        print(self.name,"avg scord is:", sum/3)
                    #OR
        #total = sum(self.marks)      
       # avg = total / len(self.marks) 
        #print(self.name, "avg score is:", avg)


s1 = Student("subhajit", [95, 68, 97])
s1.get_avg()
s1.hello()

# abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk =False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started")    

car1 = Car()
car1.start()

# encapsulation is also near about same process with abstraction

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")

    def get_balance(self):
        return self.balance


# Create account object
acc1 = Account(100000, 1141415521445)

# Perform transactions
acc1.debit(20000)
acc1.credit(50000)
acc1.credit(1000)
acc1.debit(60000)

# Print results
print("Final balance =", acc1.get_balance())
print("Account number =", acc1.account_no)
