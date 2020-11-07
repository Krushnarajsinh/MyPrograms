#TODO:he Minion Game

s=input("Enter Any Atring Here:")
s=s.upper()
#print(s)
player1,player2=0,0
#l="AEIOU"
l1=['A','E','I','O','U']

for i in range(len(s)):
    if s[i] in l1:
        #print(i)
        player1+=len(s)-i
        #print(player1)
    else:
        player2+=len(s)-i
        #print(player2)

if player1>player2:
    print("Stuart",player1)

elif player2>player1:
    print("Kevin",player2)
else:
    print("Draw")