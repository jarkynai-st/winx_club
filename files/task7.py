def game():
    import random

    x = random.randint(1,10)
    i = 0
    while i < 5:
        number = int(input())
        if number == x:
            print('Вы победили')
            break
        elif number > x:
            print(">")
        elif number < x:
            print("<")
        else:
            print('Вы проиграли')
        i += 1

game()

        tries += 1





















