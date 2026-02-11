#variable and datatype
name = "subhajit"
age = 21
price = 52.2
old = False
a= None
print(type(name) )
print(type(age) )
print(type(price))
print(type(old))
print(type(a))
#arithmatic operater
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
#relational operater
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#assinment operater
num = 10
num = num+10
#num += 10
print(num )
#logical operater
a= 20
b=10
print (not True)
print(not(a>b))
valu1 = True
valu2 = False
print (valu1 or valu2)
#type conversion
a=10
b="10"
c=int(b) # there is a type conversiob between string to integer
sum= a+c
print(sum)
#input
name = input("enter your age:")
print(name ," year old")

value = int(input("enter some value:"))
print(type(value),value)

value = float(input("enter some value:"))
print(type(value),value)

name = input("enter your name :")
age = int (input("enter your age: "))
marks =float(input("enter your marks:"))

print("welcome", name)
print(type (age),"age =", age)
print(type(marks),"marks =", marks)
#write a program to input 2 num and print their sum
num1 =int(input("enter first num:"))
num2 =int(input("enter second num:"))
sum = num1+num2
print(sum)
#wap to input side of a square & print its area
side=float(input("enter side of a squre:"))
area = side *side
print(area)
#WAP to input 2 floating point number & print their average
num1 = float(input("enter first num"))
num2 = float(input("enyer second num"))
sum = num1 +num2
print("average =",sum/2)

num1 = int(input("enter first num"))
num2 = int(input("enyer second num"))
c= num1 >= num2
print(c)