team = []

while True:
    player = {}
    goals = []

    player['name'] = input('Player\'s name: ')
    games = int(input(f'How many games did {player['name']} play? '))

    for i in range(games):
        goals.append(int(input(f'  Goals in game {i + 1}: ')))
    
    player['goals'] = goals[:]
    player['total'] = sum(goals)

    team.append(player.copy())

    cont = input('Do you want to add another player? [Y/N] ').strip().upper()[0]
    if cont == 'N':
        break

print('-=' * 30)
print(f'{"Code":<5}{"Name":<15}{"Goals":<20}{"Total":<5}')
print('-' * 50)

for i, p in enumerate(team):
    print(f'{i:<5}{p["name"]:<15}{str(p["goals"]):<20}{p["total"]:<5}')

while True:
    print('-' * 50)
    code = int(input('Show details of which player? (999 to stop): '))
    if code == 999:
        break
    if code >= len(team):
        print(f'Error! There is no player with code {code}.')
    else:
        print(f'-- Performance of {team[code]["name"]}:')
        for i, g in enumerate(team[code]["goals"]):
            print(f'   In game {i + 1}, scored {g} goal(s).')