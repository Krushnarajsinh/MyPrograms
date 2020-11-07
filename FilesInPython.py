#Why we use files?
#Simply if i make one software then it's need some perminant data so that this software fetch that similar data at any time when we open that
#-software.Normally in coding when we give a=5 then in RAM memory is allocated to this value 5 but if we close our program and
#execute again then we lost our previous data a=5 we need to again assign 5 in a
#this should not heppens in ATM machin software for that we need perminant Data
#forthat we can use some DataBase MySQL,oracal and files also
file=open("MyData","r")
print(file.read())
file.close()
#print(file.read()) After closing we can't read that file again
file1=open("abc","w")
file1.write("This is abc file and it is text file\n")
file1.write("Hello gays")
file1.close()
f=open("abc",'r')
print(f.read())
f1=open("abc",'w')
f1.write("This is again i am opening this file")  #all the previous Data are gone
#if we want to write somthing in file but all the previous data must be remains as it is then we can use append('a')
f1.close()
f2=open("abc",'a')
f2.write("\nThis is in append mode")

#if i want to copy all the data in MyData.txt file to the copyData.txt file then do follwing code:-

file=open("MyData",'r')
file1=open("Copy",'w')
for data in file:
    file1.write(data)
print("Data is moved...")

pic=open("MyPic.jpg",'rb')
image=open("CopyPic.jpg",'wb')
for p in pic:
    image.write(p)
print("Image is moved...")




