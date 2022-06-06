card = ""
print("Enter card number: ",end="")
card = input()
while (len(card) != 16) :
    card = input()
for i in range(0,len(card)):
    if i <= 11:
        print("*",end="")
    else :
        print(card[i],end="")

