def backpack (items_list:list):
    i = 0
    list2 = []
    while i < len(items_list):
        item_count = items_list.count(items_list[i])
        list2.append(item_count)
        i += 1
    max_list = max(list2)
    result_etem = items_list[list2.index(max_list)]

    j = 0
    while j < max_list-1:
        items_list.remove(result_etem)
        j += 1
    return items_list

a = backpack(['potato','potato','milk','milk','milk','milk'])
print(a)

list1 = ['potato,''potato','milk','milk','milk','milk']
list2 = [2,2,4,4,4,4]



# i = 0
# while i ** 2 < 10:
#     print(i**2)
#     i+=1

#
# list1 = [1,2,3,4,5,]
# i = 0
# result = 0
# while i < len(list1):
#       result = result + list1[i]
#       i = i + 1
# # print(result)
#
#
# x = 9
# list1 = [1,2,3,4,5,6,7,8,9,9,9]
# i = 0
# count_9 = 0
# while i < len(list1):
#       if list1[i] == x:
#             count_9 += 1
#       i += 1
# # print(count_9)
