#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
def area(r):
    a=float(4*3.14*r*r)
    return a
num=int(input("enter radius of sphere "))
b=area(num)
print("area of sphere is ",b)

#Q.2- Write a function “perfect()” that determines if parameter number is a perfect
#number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself),
#sum to the number. E.g., 6 is a perfect number because 6=1+2+3]. Q.3- Print multiplication
#table of n using loops, where n is an integer and is taken as input from the user.
def perfect(num):
    x=0
    for i in range (1,num):
        if(num%i==0):
            x+=i
    if x == num:
        return 1
    else:
        return 0
for i in range(1,1000):
    y=perfect(i)
    if (y==1):
        print(i)

#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
def table(n):
    for i in range(1,11):
        print(n,'X',i,'=',n*i)
num=int(input("enter integer "))
table(num)

#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(base,exp):
    if(exp==1):
        return base
    if(exp!=1):
        return (base*power(base,exp-1))
b=int(input("enter base "))
e=int(input("enter exponential value "))
print("Result - ",power(b,e))
