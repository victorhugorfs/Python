headquarters = [[], [], []]

for l in range(3):
    for c in range(3):
        value = int(input(f'Type one value for [{l}, {c}]: '))
        headquarters[l].append(value)

print('-='*30)
for line in headquarters:
    for item in line:
        print(f'[{item}]', end= ' ')
    print()