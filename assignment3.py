'''                             LIST                      '''

# Q.1- Create a list with user defined inputs.
a=[]
b=int(input("enter the size of list "))
for i in range (b):
    c=int(input("enter element of list "))
    a.append(c)
print(a)
# Q.2- Add the following list to above created list: 
# [‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
d=['google','apple','facebook','microsoft','tesla']
a.extend(d)
print(a)

# Q.3 - Count the number of time an object occurs in a list.
a=[]
b=int(input("enter the size of list "))
for i in range (b):
    c=int(input("enter element of list "))
    a.append(c)
num=int(input("enter the element whose occurence you want to find"))
print(a.count(num))

# Q.4 - create a list with numbers and sort it in ascending order.
list=[]
n=int(input("enter no of elements in the list"))
for i in range (n):
    m=int(input("enter value"))
    list.append(m)
print("before sorting :- ",list)
list.sort()
print("after sorting :- ",list)

# Q.5 - Given are two one-dimensional arrays A and B which are sorted in ascending order.
# Write a program to merge them into a single sorted array C that contains every item from
# arrays A and B, in ascending order. [List]
X=[6,2,7,4,9]
Y=[4,7,1,9,5]
C=[]
X.sort()
Y.sort()
C.extend(X)
C.extend(Y)
print(C)

# Q.6 - Count even and odd numbers in that list.
list2=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for i in list2:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("no of even elements = ",even)
print("no of odd elements = ",odd)
            
'''                      TUPLES                            '''

# Q.1-Print a tuple in reverse order.

# Q.2-Find largest and smallest elements of a tuples. 

'''                      STRINGS                            '''
# Q.1- Convert a string to uppercase.
string="my name is priyesh verma"
print(string.upper())

# Q.2- Print true if the string contains all numeric characters.
str1=input("enter the string ")
length=len(string)
count=0
for i in range(length):
    if str1.isdigit():
        count=0
    else:
        count=1
if count==0:
    print("True")
else:
    print("False")
    
# Q.3- Replace the word "World" with your name in the string "Hello World". 
str2="Hello World"
print("before replacing : ",str2)
print("after replacing",str2.replace("World","Priyesh"))
