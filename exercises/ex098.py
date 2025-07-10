import time

print('-=-'*15)
print('Counting from 1 to 10 by 1s')
for i in range(1, 11):
    print(i, end=' ')
    time.sleep(0.5)

print('\n' + '-=-'* 15)
print('Counting from 10 to 0 by 2s')
for i in range(10, -1, -2):
    print(i, end=' ')
    time.sleep(0.5)

print('\n' + '-=-'* 15)
print('Now is your time to personalized the counting!')
def cont():
    start = int(input('Start: '))
    end = int(input('End: '))
    step = int(input('Step: '))

    if step == 0:
        print('Step cannot be 0. Using step = 1.')
        step = 1
    elif step < 0:
        step = abs(step)
    
    print('-=-'*15)
    print(f'Counting from {start} to {end} by {step}s')

    if start < end:
        for i in range(start, end + 1, step):
            print(i, end=' ')
            time.sleep(0.5)
    else:
        for i in range(start, end - 1, -step):
            print(i, end=' ')
            time.sleep(0.5)
cont()          