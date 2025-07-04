data0 = dict()
data1 = list()

data0['name'] = str(input('Player\'s name: '))
games = int(input(f'How many games did {data0["name"]} play? '))

goals = []

for g in range(games):
    goal = int(input(f'How many goal(s) in game {g + 1}? '))
    goals.append(goal)

data0['goals'] = goals
data0['total'] = sum(goals)

data1.append(data0.copy())

print('-=-' *30)
print(data1)
print('-=-' *30)

print(f'The name is {data0["name"]}')
print(f'He did {data0["goals"]}')
print(f'Total goal(s) is {data0["total"]}')
print('-=-' *30)

print(f'The player {data0["name"]} played {games} matches.')
for i, g in enumerate(data0['goals']):
    print(f'=> In game {i + 1}, he did {g} goal(s).')
print(f'It was a total {data0["total"]} goal(s)')