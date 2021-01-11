def write_to(filename,text):
    file1 = open(filename,'w')
    file1.write(text)

write_to('text.txt','hellow!')


list1 = [1,2,3,4,5,6,7,8,8,8,1,1,1,7,7]
list2 = []
i = 0
while i < len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i += 1
# print(list2)


list1 = [1,2,3,4,5]
# print(set(list1))


file1 = open('phones.txt')
list1 = file1.readlines()
i = 0
while i < len(list1):
     print(list1[i].strip())
     i += 1





