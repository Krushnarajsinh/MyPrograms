import math
a=int(input("Enter Starting Range:"))
b=int(input("Enter Ending Range:"))
prime_l=[]
composite_l=[]
count=0
composite_count=0
print("Prime numbers from a={} to b={}".format(a,b))

for i in range(a,b+1):
    if i==1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if (i%j)==0:
            composite_count+=1
            composite_l.append(i)
            break
    else:
        count+=1
        prime_l.append(i)
print("Your Prime Number List Is Ready")
print(prime_l)
print("Your Composite List Is Ready")
print(composite_l)
print("This range contain {} prime numbers".format(count))
print("This range contain {} composite Numbers".format(composite_count))
