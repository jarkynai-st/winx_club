dict1 = {"nurjanat":['pizza','shaurma','car','house','coca-cola'],
         "aigerim":['car','penthose','ticket'],
         "baiel":['hamburger','doner','coca-cola']
         }
dict1['nurjanat'].append(4)
print(dict1)


username = "username"
password = "123456"

def auth(check_user,check_passw):
    if check_user == username and check_passw == password:
        print("OK")
    else:
        print('NOT OK')

auth('username','123456')



