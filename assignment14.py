#Q.1 Write a python program to print the cube of each value of a list using list comprehension:-
lst = []
for i in range(int(input("Enter size of list\n"))):
    a = int(input("Enter value\t"))
    lst.append(a)
lstCube = [ x**3 for x in lst ]
print(lstCube)


#Q.2 Write a python program to get all the prime numbers in a specific range using list comprehension:-
lst1 = [ x for x in range(2,int(input("Enter number till what you want prime numbers\t"))) if all(x%y!=0 for y in range(2,x)) ] 
print(lst1)


#Q.3  Write the main differences between List Comprehension and Generator Expression:-
'''A Generator Expression is doing basically the same thing as a List Comprehension does, but the GE does it lazily.
A List Comprehension, just like the plain range function, executes immediately and returns a list.
A Generator Expression, just like xrange returns and object that can be iterated over.
The comparision is not perfect though, because in an object returned by the generator expression, we cannot access an element by index.
The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets [] while the Generator expression is enclosed in plain parentheses ().
l = [n*2 for n in range(1000)] # List comprehension
g = (n*2 for n in range(1000))  # Generator expression
Type
The type of resulting values are list and generator respectively:
print(type(l))  # 'list'
print(type(g))  # 'generator' '''


'''            Lambda and Map            '''
#Q.1 Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression:-
Celsius = [35.1, 35.4, 36.7, 36.8]
Fahrenheit = [ x*(9/5) + 32 for x in Celsius ]
print(Fahrenheit)

#Q.2 Apply an anonymous function to square all the elements of a list using map and lambda:-
a=[2,5,7,8,9]
b=list(map(lambda x:x**2,a))
print(b)


'''         FILTER & REDUCE          '''
#Q.1 Filter out all the primes from a list:-
lst2 = [1,2,3,4,7,9,11,14,15,17,18,19,22,27]
def isPrime(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            c=1
            break
    if c!=1:
        return True
    else:
        return False
n = list(filter(isPrime,lst2))
print(n)

#Q.2 Write a python program to multiply all the elements of a list using reduce:-
from functools import *
lst3 = [1,2,3,4,5,6]
ls = reduce( lambda x,y:x*y,lst3 )
print(ls)
