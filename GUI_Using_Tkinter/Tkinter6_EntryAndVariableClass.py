from tkinter import *
root=Tk()
root.geometry("733x434")
root.title("My Details")
#There are 4 types of variable class in tkinter
#1.StringVar 2.BooleanVar 3.IntVar 4.DoubleVar
#this classes are usefull for taking some input from the users
#By Using Entery() We can provide User Entery To the GUI
#there are different packing techanice in tkinter .pack() and .grid() are usefull for packing Eny logic or event in GUI
#Use of .grid() method is same as of excel sheet in excel first block is represented by row=0 and column=0 , here similar techanice is used

label_1=Label(root,text="Enter User_Name:",font=("lucidacalligraphy",20,"bold italic"))
label_2=Label(root,text="Enter User_password:",font=("lucidacalligraphy",20,"bold italic"))
label_1.grid()
label_2.grid(row=1)


root.mainloop()