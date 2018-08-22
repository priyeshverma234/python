# Q.1- Reverse the whole list using list methods.
a = int(input("enter the number of elements in the list "))
list = []
for i in range(a):
    b=int(input("enter the element "))
    list.append(b)
print(list)
print("After reversing : ")
print(list[::-1])

# Q.2- Print all the uppercase letters from a string.
str1=input("enter string ")
for i in str1:
    if(i>='A' and i<='Z'):
        print(i)

# Q.3- Split the user input on comma's and store the values in a list as integers.a
n=input("enter number using commas ").split(",")
list2=[]
for i in n:
    a=int(i)
    list2.append(a)
print(list2)

# Q.4- Check whether a string is palindromic or not.
str1=input("enter string ")
str2=str1[::-1]
if(str2==str1):
    print("palindrome")
else:
    print("not palindrome")

# Q 5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
import copy as c

'''              DeepCopy               '''

x=[42,12,35,[68,48,79],21,30]
y=c.deepcopy(x)
print("-----DeepCopy------")
print("List 1 : ",x)
print("List 2 : ",y)
y[3][0] = 15
y[3][1] = 10
print("After changing List 2 ")
print("List 1 : ",x)
print("List 2 : ",y)

'''               ShallowCopy            '''

l=[56,78,65,[5,32,59],22,36]
m=c.copy(l)
print("-----ShallowCopy-----")
print("List 1 : ",l)
print("List 2 : ",m)
m[3][0] = 40
m[3][1] = 50
print("After changing List 2 ")
print("List 1 : ",l)
print("List 2 : ",m)

# DIFFERENCE

'''
1. Changes made in deep copy of a list are never reflected in the original list
   whereas changes made in shallow copy of a list are always reflected in the original list.
2. In deepcopy, object is copied to other object whereas in shallow copy reference of object
   is copied in other object.
'''
