file1 = open('phones.txt', 'r')

list1 = file1.readlines()
list1.append('maksimka')
list1.pop()
print(list1)



