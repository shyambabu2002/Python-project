from listmaker import make_list

string = ""
list1 = []

print("Enter a list of no. : ")
string = input()

list1 = make_list(string)

list1.sort()

print(list1)
num = 0
max1 = 0
sum1 = 1
for i in range(0,len(list1) -1):
    if (list1[i] == list1[i+1]) :
        sum1+=1
    elif list1[i] != list1[i+1]:
        if max1<sum1:
            max1  = sum1
            num = list1[i]
        sum1 = 1
print(max1,",",num)
