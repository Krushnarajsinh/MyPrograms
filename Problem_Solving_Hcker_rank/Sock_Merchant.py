n=int(input())
ar=list(map(int,input().split()))
dict={}

for i in range(len(ar)):
    count = 0
    for j in range(len(ar)):
        if ar[i]==ar[j]:
            count=count+1
            dict[ar[i]]=count
#print(dict)
result=0
pair=0
for i in dict:
    #print(dict[i])
    a=dict[i]%2
    #print("This",a)
    #print("here",i-a)
    result+=dict[i]-a

    #print(result)
print(result//2)


