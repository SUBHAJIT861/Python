info = {
    "name" : "subhajit ",
    "subject": ["python","c", "java","dsa"],#list also run in dictionary
    "topic" : ("dictionary","set"),# tupple also run
    "age" : 21,
    "is_adult" : True,
    "cgpa" : 8.2,
}
print(info)
print(type(info))
# if we find the value through key 
print(info["name"])

null_dict = {}
null_dict["name"] = "subhajit"
print(null_dict)
# nested dictionary
student = {
     "name" : "subhajit sahoo",
     "subject" : {
        "phy" : 95,
        "chem" : 98,
        "math": 99,
     }
}
print(student)
print(student["subject"])
print(student["subject"]["chem"])
# return all key
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
# return all values
print(student.values())
print(list(student.values()))
print(len(list(student.values())))
# return all (key,value) pairs as tuples
print(student.items())
print(list(student.items()))
print(len(list(student.items())))
#return the key according to values
print(student.get("name"))
print(list(student.get("name")))
print(len(list(student.get("name"))))
#insert the specified item  to the dictionary
student.update({"city" : "digha"})
print(student)

new_dict= {"city" :"kolkata","age": 25}
student.update(new_dict)
print(student)

# set in python
collection = {1,2,3,4, "hello", "world"}# set is unique and unordered
collection = {1,2,2,4,3,4, "hello", "world","hello"}# set did not print duplicate values
print(collection)
print(type(collection))
print(len(collection))
collection = set() # empty set syntex
collection.add(1)
collection.add(2)
collection.add("somu")
collection.add((9,7,3,4))
collection.remove(1)
print(collection)
print(type(collection))
print(len(collection))
print(collection.pop())#pop means random remove elements from the set
print(collection.pop())

set1 = {1,2,5,8,7}
set2 = {5,7,3,9,0}
print(set1.union(set2))
print(set1.intersection(set2))

#store following word meanning in a python dictonary
dictionary = {
     
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts &figures"]
}   
print(dictionary)

#practic no 2
student = {
    "python","java","c++","python","javascript","java","python","c++","java","c"
}
print(len(student))
# wap to enter marks of 3 subject from the user and store them i a dictionary. start with an empty dictionary&
# add one by one. use sub name as key& marks as value
marks = {}

y=int(input("enter chem :"))
marks.update({"chem" : y})

y=int(input("enter phy :"))
marks.update({"phy" : y})

y=int(input("enter math :"))
marks.update({"math" : y})

print(marks)

#figure out a way to store 8&8.0 as seperate values in the set.
values = {
    ("float" , 8.0),
    ("int" , 8)
}
print(values)
