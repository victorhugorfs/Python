def record (name='', goals=0):
    print(f'{name if name else "<unknown>"} player scored {goals} goal(s) in the championship.')

print('-'*30)

name_input = input('Player Name: ').strip()
goals_input = input('Total goals: ').strip()

if goals_input.isdigit():
    goals = int(goals_input)
else:
    goals = 0

record(name_input, goals)