list1 = [1,2,3,4,5,6,7]
i = 0
list2 = []
while i < len(list1):
    if list1[i] % 2 == 0:
       list2.append(list1[i])
    i += 1
print(list2)
