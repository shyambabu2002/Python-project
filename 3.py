#Q3
print("Enter the command format (2+3): ",end="")
command = ""
command = input()
com_lst = []

a = 0
sum1 = 0

for i in command :
    if i.isdigit():
        a *= 10
        a += int(i)
        #print(a)
    else :
       
        com_lst.append(a)
        a = 0
        com_lst.append(i)
com_lst.append(a)

#print(com_lst)
a = com_lst[0]
b = com_lst[2]

if com_lst[1] == "+":
    sum1 = a+b
    print("result: ",sum1)
elif com_lst[1] == "*":
    sum1 = a*b
    print("result: ",sum1)
elif com_lst[1] == "/":
    sum1 = a/b
    print("result: ",sum1)
elif com_lst[1] == "-":
    sum1 = a-b
    print("result: ",sum1)
else :
    print("Invalid input")
    



    
