list1 = []
n = 0
count = 0
print("Enter -1 to stop")
print("Enter {} number:".format(count))

n = int(input())
while(n != -1):
    list1.append(n)
    count+=1
    print("Enter {} number:".format(count))
    n = int(input())
print(list1)

print("Enter asc or desc: ",end = '')
comm = input()

sort = False

while not (sort):
    sort = True
    for j in range(0,count-1):
        if (list1[j+1] < list1[j]):
            sort = False
            list1[j+1],list1[j] = list1[j],list1[j+1]


while ((comm != "asc") & (comm != "desc")):
    print("invalid input type again")
    comm = input()
if (comm == "asc"):
    print(list1)        
elif comm == "desc":
    print(list1[::-1])

