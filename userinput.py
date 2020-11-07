x=int(input("Enter any number here:"))
if x%2==0:
    print("Given Number Is Even")
else:
    print("Given Number Is Odd")
ch=input("Enter any Charecter here:")[0]
print(ch)
if ch>="a" and ch<="z":
    print("Enter charecter is in between a-z")
elif(ch>="0" and ch<="9"):
    print("Enter charecter is in between 0-9 ")
elif(ch>="A" and ch<="Z"):
    print("Enter charecter is in between A-Z")
else:
    print("Enter Input is not a charecter")


