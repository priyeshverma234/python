#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
'''Make methods to 
1. Display-Display the details. 
2. Add- Add the movie details. '''

class MovieDetails():
    def __init__(self):
        self.artist='NA'
        self.year='NA'
        self.rating='NA'
    def add(self,aname,y,rt):
        self.artist=aname
        self.year=y
        self.rating=rt
    def display(self):
        print("Artist : ",self.artist,"\nYear of release : ",self.year,"\nRatings : ",self.rating)
ch=input("Do you want to add details ? Y:N \n choice :- ")
a=MovieDetails()
if(ch=='y' or ch=='Y'):
        aname=input("enter artist name ")
        y=int(input("enter year of release "))
        rt=int(input("enter ratings "))
        a.add(aname,y,rt)
        a.display()
        
#Q.5- Create a class Animal as a base class and define method animal_attribute.

class animal():
    def animal_attribute(self):
        print("Class animal")
class tiger(animal):
    pass
obj=tiger()
obj.animal_attribute()

#Create another class Tiger which is inheriting Animal and access the base class method.
#Q.6- What will be the output of following code. 
'''
    class A:
        def f(self):
            return self.g()

        def g(self):
            return 'A'

    class B(A):
        def g(self):
            return 'B'

    a = A()
    b = B()
    print a.f(), b.f()
    print a.g(), b.g()
'''
#Answer 6 :
'''
output of this code will generate error as print statement ha no brackets
otherwise it will print =
A B
A B
'''

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
#create class rectangle and square which inherits shape and access the method Area.
    
class shape():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("area : ",self.l*self.b)
class square(shape):
    pass
class rectangle(shape):
    pass
l=int(input("enter length "))
b=int(input("enter breadth "))
if(l==b):
    obj=square(l,b)
    obj.area()
else:
    obj=rectangle(l,b)
    obj.area()
    
