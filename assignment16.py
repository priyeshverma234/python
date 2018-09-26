#Q.1- Write a python script to create a databse of students named Students.
import pymongo
client=pymongo.MongoClient()
data=client['Students']
collection=data['students_collection']

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.

#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
for i in range(0,10):
    name=input('Enter name - ')
    marks=int(input('Emter marks - '))
    collection.insert_one({'Name':name,'Marks':marks})
b=collection.find()
for c in b:
    print(c)

#Q.4- Print the names of all the students who scored more than 80 marks.
d=collection.find({"Marks":{"$gt":80}})
for i in d:
    print(i)
