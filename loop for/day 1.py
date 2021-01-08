# list1 = ['blue','red','white','green',5]
# for color in list1:
#     print(color)


# for i in range(100,200):
#     # print(i)
#
#     if i % 2 == 0:
#     print(i)

# result = 1
# for i in range(1,6):
#      # 10*9*8*7*6....*1
#      # 10!
#
#      result *= i
# # print(result)
#
# for i in 'blue', 'red','white','green',5:
# # print(i)
#
#     try:
#     # print(1 + '3')
#     except TypeError:
#     # print(1)
#
#     list1 = [1, 2, 3]
#     try:
#     # print(list1[4])
#     except IndexError:
# # print(list1[-1])
#
#
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print(0)
#


# a = int(input())
# b = int(input())
# count_years = 0
# if 1<=a<=b<=10:
#     while a <= b:
#         a = a * 3
#         b = b * 2
#         count_years += 1
#     # print(count_years)


numbers = list(map(int,input().split()))
a = numbers[0]
b = numbers[0]
count_years = 0
if 1 <= a <= b <= 10:
    while a <= b:
        a = a * 3
        b = b * 2
        count_years += 1
    print(count_years)
list(int(input()))












