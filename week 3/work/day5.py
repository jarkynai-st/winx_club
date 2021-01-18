# list2 = []
# for i in range(4):
#     name = input()
#     list2.append(name)

# print(list2)


# stones = ['purple', 'green', 'blue', 'orange', 'red', 'yellow']
# list1 = []
# n = int(input())
# for i in range(n):
#     my_stone = input()
#     list1.append(my_stone)
#
# print(len(stones) - n)
# for stone in stones:
#     if stone not in list1:
#         print(stone)


string1 = 'xaxxxxaax'
if len(string1) // 2 < string1.count('a'):
    print('Любимая строка Алисы')
else:
    i = 0
    while string1.count('a') <= len(string1)//2:
        if string1[i] != 'a':
            string1 = string1.replace(string1[i],'',1)

        i += 1

    # print(string1)

string = 'Tom'
unique = []
for letter in string:
    if letter not in unique:
        unique.append(letter)
if len(unique) % 2 == 0:
    print('CHAT WITH HER')
else:
    print('INGORE HIM')


def words(word):
    up_count = 0
    low_count = 0
    for letter in word:
        if letter.isupper():
            up_count += 1
        elif letter.islower():
            low_count += 1
    if up_count > low_count:
        word = word.upper()
    else:
        word = word.lower()
    print(word)

print('HOuSe')























