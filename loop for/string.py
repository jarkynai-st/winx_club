def remove_from_string(string,x):
    if x in string:
        string = string.replace(x,'')
        print(string)
    else:
        print('NOT OK')

# remove_from_string('lala','a')


string1 = "Winx Club "
# print(string1.startswith('Winx'))


str = "Vasya is the best football player. Vasya is very strong player"
name = 'Petya'

string2 = 'gAtSbY'
X = 'Z'
try:
    print(string2.index('X'))
except ValueError:
    print(1)














