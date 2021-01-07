x = 2
list1 = [1,2,3,2,2,2,2,2]
i = 0
len_list1 = len(list1)
while i < len_list1:
    if x in list1:
        list1.remove(x)
    i = i + 1
print(list1)