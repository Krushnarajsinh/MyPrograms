#for rearranging a string into pallindrome we can allow only 1 character  to be an odd number
      #for example:-geeksogeeks
		#here g=2 e=4 k=2 s=2 o=1
		#here we can see that only o is coming odd time so we can said that
		#this strnig can be rearrange into pallindrome
		#further Example:-geeksforgeeks
		#here g=2 e=4 k=2 s=2 f=1 o=1 r=1
		#here f,o,and r comes for odd time
		#three charecters should not be allowed if you wnat to pallindrome of this
		#hence above example can not be a pllindrome
T=int(input("Enter the number of test cases:"))
while T>0:
    s=str(input("Enter String to find it is pallindrome or not:"))
    set=[]

    for i in range(len(s)):
        if set.__contains__(s[i]):
            set.remove(s[i])
        else:
            set.append(s[i])
    if len(set)<=1:
        print("YES")
    else:
        print("NO")

    T-=1
