a= 0
print("1st number: ")
a = int(input())
print("2nd number: ")
b = int(input())
n = a^b
a = n^a
b = n^b
print(a,b)
