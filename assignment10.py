#Q.1- Write a Python program to read n lines of a file.
f=open("Q1.txt","r")
print(f.read())
f.close()

#Q.2- Write a Python program to count the frequency of words in a file.
f=open("Q1.txt","r")
x=f.read()
y=input("enter word to count the frequency ")
z=x.count(y)
print("\n",y,"occur",z," times")
f.close()

#Q.3- Write a Python program to copy the contents of a file to another file
f=open("Q2.txt","r")
a=f.read()
f.close()
print("before copying ")
c=open("Q3.txt","r")
b=c.read()
print(b,"\n")
print("after copying ")
c.close()
c=open("Q3.txt","a")
c.write(a)
c.close()
c=open("Q3.txt","r")
d=c.read()
print(d)
c.close()

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
f=open("Q4.txt","r")
a=open("Q5.txt","r")
c=open("Q6.txt","w")
b=f.readlines()
d=a.readlines()
for x,y in zip(b,d):
    c.write(x)
    c.write(y)
c.close()
c=open("Q6.txt","r")
e=c.read()
print(e)
c.close()
a.close()
f.close()

#Q.5- Write a Python program to write 10 random numbers into a file.
#Read the file and then sort the numbers and then store it to another file.
l=[]
a=open("file1.txt","w")
for i in range(1,11):
    b=int(input("enter no "))
    l.append(b)
a.write(str(l))
a.close()
a=open("file1.txt","r")
b=a.readlines()
print(b)
a.close()
l.sort()
d=open("file2.txt","w")
d.write(str(l))
d.close()
d=open("file2.txt","r")
e=d.read()
print(e)
d.close()

