#function defination
def calc_sum(a, b): # parameters
    sum = a + b
    print(sum)
    
calc_sum(5, 8) #function call,, arguments
calc_sum(9, 7)
calc_sum(25, 45)

# avg of three number
def avg_num(a,b,c):
    avg=(a+b+c)/3
    print(avg)

avg_num(8,5,2)
avg_num(5,2,9)

# bellow this is for user define
a= int(input("enter first number"))
b= int(input("enter second number"))
c= int(input("enter third number"))
avg_num(a,b,c)
 
# waf to print the length of list
cities=["contai", "digha","ramnagar", "egra","kolaghat"]
bikes=["Honda","KTM","R15","Royal Enfeld"]

def cal_len(list):
    print(len(list))

cal_len(bikes)
#waf to print a list in a single line
def cal_len(list):
    for item in list:
        print(item, end=" ")

cal_len(cities)

# waf to caculate a factorial of a number
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)    

n= int(input("enter a number"))
cal_fact(n)
# WAF to convert USD To INR
def converter(usd_val):
    inr_val = usd_val*92.04
    print(usd_val,"USd=", inr_val,"INR")

usd_val= int(input("enter the USD value:"))

converter(usd_val)


def odd_even(number):
    if(number % 2 == 0):
        print("this is even number")
    else:
        print("this is odd number")    

number= int(input("enter a number:"))        
odd_even(number)

#recursion
  #wap to print Nto1 using recursion
def show(n):
    if(n==0):
       return
    print(n)

    show(n-1)

n= int(input("enter a number:"))
show(n)

# wap for factorial of a number using recursion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
n= int(input("enter the number:"))    
print("factorial", fact(n))
# calculate sum of first n numbers using recursion method
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n

n= int(input("enter the number:"))
sum = cal_sum(n)        
print(sum)
# wap a recursion function to print all element in a list
def print_list(list,idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list, idx+1) 

fruits = ["mango","banana","apple","water melan"]       
print_list(fruits)