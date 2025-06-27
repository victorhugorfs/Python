from random import sample
import time

mega_sena = []

print('-'*30)
print('PLAY MEGA SENA'.center(30))
print('-'*30)

plays = int(input('How many games do you want me to draw? '))

for i in range(plays):
    pc = sample(range(1, 61), 6)
    mega_sena.append(pc)

print('-='*3 + f' DRAW {plays} GAMES ' + '-='*3)

for i, jogo in enumerate(mega_sena, start=1):
    print(f'Game {i}: {sorted(jogo)}')
    time.sleep(1)

print('-='*5 + ' < GOOD LUCK! > ' + '-='*5)