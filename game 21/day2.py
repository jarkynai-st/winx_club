players = ['nurjanat','akylbek','jarkynai','aigerim','baiel']
scores = []
import random
i = 0
while i < len(players):
    print(f'Добро пожаловать, {players[i]}')
    score = random.randint(2,11) + random.randint(2,11)
    print(score)
    check = input('да/нет')
    while check == 'да':
        score += random.randint(2,11)
        print(score)
        check = input('да/нет')
        if score > 21:
            score = 0
    scores.append(score)
    i += 1

max_score = max(scores)
winner = players[scores.index(max_score)]
print(f'Победитель: {winner}, с баллами {max_score}')

