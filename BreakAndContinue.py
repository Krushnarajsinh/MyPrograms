print(" Example fore Break Statement")
i=1
while i<=5:
    if i==3:
        break                   # using break statement you can jump out from the loop or your pointer point to the line after the
                                #loop is ended
    else:
        print(i,"Hello")
    i=i+1
print("Example for Continue statement")
j=1
while j<=6:
    if j==3:
        j=j+1
        continue                     #continue statement only skip particular(one) iteration or your pointer points the line where
                                     # your loop lies.
    elif j==6:
        pass                        #When you want to put empty your if,else,elif,function,class block you can use pass or this
                                    #statement simply pass that block .
    else:
        print(j,"Hello")
    j=j+1
print("Finish")

