def make_list(string):
    a = 0
    list1 = []
    for i in string:
         if i.isdigit():
             a = a*10 + int(i)
         else:
            list1.append(a)
            a = 0
    list1.append(a)
    return list1
