#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop. 
dic = eval(input("enter dictionary "))
info = int(input("enter the value "))
for key,value in dic.items():
    if info==value:
        break
print(key)

#Q.2- Create a dictionary and store student names and create nested dictionary to store the
#subject wise marks of every student.Print the marks of a given student from that dictionary for every subject. %
#Hint: Use nested dictionary to store subjects marks.
dic1={'Priyesh':{'maths':40,'phy':50,'chem':56},'Vasu':{'maths':55,'phy':85,'chem':70},'Raghav':{'maths':66,'phy':78,'chem':80}}
s=str(input("enter name of the student "))
for(key,value) in dic1.items:
    if s==key:
        print('maths = ',dic1[key]['maths'])
        print('phy = ',dic1[key]['phy'])
        print('chem = ',dic1[key]['chem'])
