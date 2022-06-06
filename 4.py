#q4
def make_list(string):
    a = 0
    for i in string:
         if i.isdigit():
             a = a*10 + int(i)
         else:
            list1.append(a)
            a = 0
    list1.append(a)
    return list1


list1 = []
list2 = []
string = ""
string2 = ""
print("Enter a string: ",end = "")
string = input()

for i in range(0,len(string)):
    string2+= string[i] #strings are immutable
    string2+= string[i]
print(string2)

