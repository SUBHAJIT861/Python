#List and tuple
"""marks = [62.2,78.5,96.1,41.2,85.8,45.6]
print(marks)
print(type(marks))
print(len(marks))
print(marks[2])
print(marks[0])
# list mutable
student = ["subhajit", 96.36,20,"digha"]
print(student)
print(student[0])
student[0] = "sayan"
print(student)
# list slicing
markes = [58,25,41,78,96,99]
print(markes[1:4])
print(markes[ :4])
print(markes[2: ])
print(markes[-4:-1])
#list Methods
list = [5,3,8]
list.append(7) # add one element in the edn of the list
print(list)
list.sort() # sort in ascending order or small to large
print(list)
list.sort(reverse = True)# sort in decending order or large to small
print(list)
list.reverse()
print(list)
list.insert(2,4)
print(list)
list.remove(5) # according to particular number basis
print(list)
list.pop(2) # according to range of the list
print(list)

tup = (2,8,5,8,7)
print(tup)
print(type(tup))
print(tup[2])
print(tup[1:3])
print(tup.index(7))
print(tup.count(8))

# wap to ask the user to enter names of their 3 favorites movies&store them in a list

movies = []
mov1 = input("enter first movie:")
mov2 = input("enter second movie:")
mov3 = input("enter third movie:")


movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# wap to check if a list contains a palindrome of element(use copy()method)
list1 = [1,2,1]
list2 = [1,2,8]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

# wap to count the number of student with the great A in the following tuple
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))

#sort the abovevalues in a list& sort them from A to D.
tup = ["C","D","A","A","B","B","A"]
tup.sort(reverse=True)
print(tup)"""