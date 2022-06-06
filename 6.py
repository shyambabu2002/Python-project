from listmaker import make_list

def prime(n):
    for i in range(2,int(n/2)):
        if (n%i == 0):
            return 0
    return 1


string =
print("Enter a List : ")
string = input()

list1 = make_list(string)

for i in list1 :
    if prime(i) :
        print(i)
    



