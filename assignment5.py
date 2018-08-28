#Q.1- Take an input year from user and decide whether it is a leap year or not.
y=int(input("enter year "))
if y%4==0:
    if y%100==0:
        if y%400==0:
            print(y," is a leap year")
        else:
            print(y," is not a leap year")
    else:
        print(y," is leap year")
else:
    print(y," is not a leap year")
    
#Q.2- Take length and breadth input from user and check whether the dimensions
#are of square or rectangle. 
a=int(input("enter length "))
b=int(input("enter breadth "))
if a == b:
    print("entered dimensions are of a square")
else:
    print("entered dimensions are of a rectangle")
    

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

a = int(input("enter age of Person 1 "))
b = int(input("enter age of Person 2 "))
c = int(input("enter age of Person 3 "))
print('''oldest person's age is ''',max(a,b,c))
print('''youngest person's age is ''',min(a,b,c))

#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then
#using following rules print their place of service. 
'''
1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR". '''

age = int(input("enter your age "))
sex = input("enter your sex (M or F) ")
mts = input("enter your marital status (Y or N) ")
if sex == "m" or sex == "M" :
          if age>20 and age<40 :
              print("you will work anywhere")
          elif age>40 and age<60 :
              print("ypu will work in urban areas")
          else :
              print("ERROR")
else :
    print("you will work in urban areas")

#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than
#1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.                 
quan = int(input("enter the quantity of item "))
cost = 0
if quan>1000:
    cost=quan*100
    cost = cost-cost*0.1
    print("total cost is ",cost)
else:
    cost = quan*100
    print("total cost is ",cost)

'''       LOOPS      '''
 
#Q.1- Take 10 integers from user and print it on screen.
a=[]
for i in range(10):
    x=int(input("enter no "))
    a.append(x)
for i in range(10):
    print(a[i])

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while "true":
    print("infinite")

#Q.3- Create a list of integer elements by user input. Make a new list which will store square
#of elements of previous list.
x=[]
y=[]
num=int(input("enter the size of list "))
for i in range(num):
    a=int(input("enter a number "))
    x.append(a)
    a*=a;
    y.append(a)
print("normal list ",x)
print("list after squaring ",y)


#Q.4- From a list containing ints, strings and floats, make three lists to store them separately 
string=[]
float_=[]
integer=[]
list=[1,2,3,'a','b','c',4,5,1.1,5.6,'d',6.1,6]
for i in list:
    if(type(i) is str):
        string.append(i)
    elif(type(i) is float):
        float_.append(i)
    elif(type(i) is int):
        integer.append(i)
print("list of integer type is ",integer)
print("list of string type is ",string)
print("list of float type is ",float_)

#Q.5- Using range(1,101), make a list containing only prime numbers.
l=[]
for i in range(1,101):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
    if(flag==0):
        l.append(i)
print(l)
 

#Q.6- Print the following patterns: 
'''
 * 
 ** 
 *** 
 ****
'''

x="*"
for i in range(1,5):
    print(i*x)

#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the
#list and delete that element, if found. Iterate over list using for loop.

l1=[]
n=int(input("enter the size of list "))
for i in range(0,n):
    a=int(input("enter number "))
    l1.append(a)
b=int(input("enter the element you want to delete "))
l1.remove(b)
print(l1)



