# i = 0
# while i ** 2 < 10:
#     print(i**2)
#     i+=1


list1 = [1,2,3,4,5,]
i = 0
result = 0
while i < len(list1):
      result = result + list1[i]
      i = i + 1
print(result)


x = 9
list1 = [1,2,3,4,5,6,7,8,9,9,9]
i = 0
count_9 = 0
while i < len(list1):
      if list1[i] == x:
            count_9 += 1
      i += 1
print(count_9)




