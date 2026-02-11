
#string and conditional datatype
str1= "my name is subhajit \n i am an enginner"
print(str1)
#concatenation
str2= "subhajit"
str3 = "sahoo"
finalstr= str2+""+ str3
print(finalstr)
len1=len(str2)
len2=len(str3)
print(len1)
print(len2)
print(len(finalstr))
#indexing
str = "subhajit sahoo"
char= str[11]
print(char)
#slicing
name = "subhajit sahoo"
print(name[0:8])
print(name[9:14])
print(name[0:len(name)])
print(name[-14:-9])#negative indexing
print(name.endswith("sub"))#return true if string ends with "hoo" other false
print(name.capitalize())#capitalize 1st char
print(name.replace("h", "b"))#replace oldchar(h) with new char(b)
print(name.find("s"))#return 1st index of 1st occurrer
print(name.count("s"))#count the occurrence of substr
print(len(name))

name2 = input("enter your name:")
print("length of your name:" , len(name2))
#conditional statement
age= int(input("enter your age:"))

if(age>=18):
    print("can vote and apply for license" )
elif(age<=18):
    print("can not vote and drive")

light = input("enter your light colour:")

if(light == "green"):
    print("go")
elif(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
else:
    print("light is damage")

marks = int( input("enter your number:"))

if marks >= 90:
    print("grade is A")
elif (marks >= 75 and marks < 90):
    print("grade is B")
elif( 75 > marks >= 60):
    print("grade is C")
elif (60 > marks >= 30):
    print("grade is D")
else:
    print("you are fail in exam")
    #nesting

age = int(input("enter your age:"))

if (age >= 18):
    if (age >= 80):
        print("can not drive")
    else:
        print("can drive")
else:
    print("cannot drive")

    
number = int(input("Enter your number: "))

if (number % 2 == 0):
    print("even")
else:
    print("odd")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")


number=int(input("enter your number:"))
if(number % 7 ==0):
    print("this number is multiple of 7")
else:
    print("this is not multiple of 7")    


