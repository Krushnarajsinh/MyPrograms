ab=list(map(int,input("Enter The Range:").split()))
#print(ab)
a=ab[0]
b=ab[1]
flag=False
lip_list=[]
for i in range(a,b+1):
    if i%4==0:
        if i%100==0:
            if i%400==0:
                flag=True
            else:
                flag=False
        else:
            flag=True
    else:
        flag=False

    if flag==True:
        lip_list.append(i)
print(lip_list)
