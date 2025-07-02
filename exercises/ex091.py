import random

players = ['Player1', 'Player2', 'Player3', 'Player4']

results = {}

for player in players:
    results[player] = random.randint(1,6)

ranking = sorted(results.items(), key=lambda x: x[1], reverse=True)

print(f'The numbers sorted: ')
for player, number in results.items():
    print(f'- The {player} sorted {number}')

print('Player rankings:')
for position, (player, number) in enumerate(ranking, start=1):
    print(f'- {position}th place: {player} with {number}')