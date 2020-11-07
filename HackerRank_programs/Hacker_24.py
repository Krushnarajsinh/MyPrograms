#itertools.permutations()
from itertools import permutations
s,k=input().split()
print(s)
size=int(k)
#print(sorted(s))
s=sorted(s)
l=list(permutations(s,size))

for i in l:
    print("".join(list(i)))
