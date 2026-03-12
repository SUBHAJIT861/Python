
f= open("demo.txt","r") # r for reading mode
data = f.read()
print(data)
print(type(data))
f.close()

f= open("demo.txt","r") 

data = f. read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

f= open("demo.txt","w") # w means over write 
f.write("i want to learn java.125\n")
f.close()

f= open("demo.txt","a") # a means append
f.write("after that want to learn web dev")
f.close()

f= open("demo.txt","r+") # read and over write the data
f.write("subhajit")
print(f.read())
f.close()

f= open("demo.txt","a+") 
f.write("sahoo")
f.close()

import os
os.remove("sample.txt")# file delete 

with open("practic.txt","w")as f:
    f.write("i am subhajit sahoo.\n i am from digha\n")
    f.write("i learn python from apna collage\n i like also java for programming")

with open("practic.txt","r")as f:
    data = f.read()

new_data = data.replace("java","DBMS")    
print(new_data)

with open("practic.txt","w")as f:
    f.write(new_data)


def check_forward():
    word = "apna collage"
    with open("practic.txt", "r") as f:
        data = f.read()
        if data.find(word) != -1:
            print("found")
        else:
            print("not found")

check_forward()    

def check_for_line():
    word = "subhajit"
    data = True
    line_no = 1
    with open("practic.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1    

    return -1

check_for_line()

count = 0

with open("practic.txt", "r") as f:
    data = f.read()
    print(data)

numbers = data.split(",")

for value in numbers:
    if value.strip().isdigit():   # check if it is a number
        value = int(value)
        if value % 2 == 0:
            count += 1

print("Even numbers:", count)