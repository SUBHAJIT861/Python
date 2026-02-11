#while loop
"""i=1
while i<=5:
    print("subhajit",i)
    i+=1

#print numbers from 1to5 or 5to1 and 1 to 100 and 100 to1
i=5
while i>=1:
    print(i)
    i-=1

j=1
while j<=100:
    print(j)
    j+=1

j=100
while j>=1:
    print(j)
    j-=1
#print multiplication table of a number n.
n=int(input("enter tne number:"))
i=1
while i<=10:
    print(n*i)
    i+=1
#print the element of the following list using loops
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx< len(nums):
    print(nums[idx])
    idx+=1
    #search for a number x in this tuple using loops

nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the number:"))
i=0 
while i<len(nums):
    if(nums[i] == x ):
        print("found at idx",i)
    i+=1

# for loop
str = "subhajit"

for char in str:
    if(char == 'a'):
      print("a found")
      break
    print(char)
else:
    print("end")

nums = [1,4,9,16,25,36,49,64,81,100]

for el in nums:
    print(el)

nums = [1,4,9,16,25,36,49,64,81,100]
x= int(input("enter the number:"))
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx",idx)
    idx += 1   

#range function
for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

for i in range(2,20,2):
        print(i)

n= int(input("enter thr number:"))
for i in range(1,11):
    print(n*i)"""

# wap to find the sum of first n numbers
n=5
sum = 0
for i in range(1, n+1):
    sum += i
print("total sum =",sum)    

# wap to find the factorial of first n numbers
n=5
fact= 1
for i in range(1, n+1):
    fact *= i
print("factorial =",fact)   