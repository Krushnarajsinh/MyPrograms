"""
   This is multi line codding we can
   Also use this
   but always prefer # to give comments
   even in multilinig also
   because 3 double quats are used for special document perpose

   """
#this is single comments
#we must use '#' for multiline comments also

print("Enter the 5 values")
a=input().split(' ')
if len(a) is 5:
    print(a)
    print("Done")
else:
    print("You can not enter morethan 5 values")
#PYTHON IS A BOTH COMPILED AND INTERPRETED LANGUAGE
#ITS LOGIC IS SIMILAR TO THE JAVA
#TO MAKE PYTHON PORTALBE AND PLATEFORM INDEPENDENT
#FIRST SOURCECODE.PY IS ->COMPLIED THEN ITS CONVERTED INTO->BYTECODE AND THIS bytecode IS THEN -> INTERPRETED BY PVM ->AND GIVE US A MACINECODE(0-1)
#IN JAVA WE HAVE JVM HERE WE HAVE PVM
#whatever we learn in python is all about "cpython" (internally implimantion is done by c language and mostly cpython is used)
#implimentation of python is different like "jython" (here implimentation is done by java language),"pypy","iornpython"(it is implimanted in .net language)