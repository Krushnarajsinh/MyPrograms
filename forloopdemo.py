
print("Prime numbers between 1-10 is here:")
for i in range(11):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:                    # Concept of for-else
            print(i)
