#Q.1- Name and handle the exception occured in the following program:
'''
    a=3
     if a<4:
        a=a/(a-3)
         print(a)
'''
a=3
try:
    if a<4:
        a=a/(a-3)
except ZeroDivisionError:
        print("Zero Division Error")
        print(a)
      
    
#Q.2- Name and handle the exception occurred in the following program: 
#l=[1,2,3] 
#print(l[3]) 

try:
    l=[1,2,3]
    print(l[3])
except IndexError as msg:
    print('Error : ',msg)

#Q.3- What will be the output of the following code:

    # Program to depict Raising Exception
'''    
    try:
        raise NameError("Hi there")  # Raise Error
    except NameError:
        print("An exception")
        raise  # To determine whether the exception was raised or not
'''

'''
Answer 3 :
output will be :- An exception
                  NameError : Hi there
'''
 
#Q.4- What will be the output of the following code: 
'''
     # Function which returns a/b
    def AbyB(a , b):
        try:
            c = ((a+b) / (a-b))
        except ZeroDivisionError:
            print("a/b result in 0")
        else:
            print(c)
    
    # Driver program to test above function
    AbyB(2.0, 3.0)
    AbyB(3.0, 3.0)
'''
'''
output:-
-5.0
a/b result in 0
'''
    
#Q.5- Write a program to show and handle following exceptions: 
#1. Import Error 
#2. Value Error 
#3. Index Error

'''                  Import Error               '''
try:
    import Priyesh
except ImportError as msg:
    print(msg)

'''                  Value Error                '''
try:
    n=int(input())
    print(n)
except ValueError:
    print("enter input")
    
'''                   Index Error                '''
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Inex error")
    print(l)
