string = ""
string = input()

list1 = []
nstr = ""
for i in string:
    list1.append(i)
list1.sort()
for i in list1:
    nstr+=i
print(nstr)
