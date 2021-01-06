list1 = [10,20,30,40]
list2 = []
i = 0
while i < len(list1):
    list2.insert(0,list1[i])
    i = i + 1
    print(list2)
print(list1)

