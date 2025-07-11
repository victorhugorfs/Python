import time

def maior(* num):
    size = len(num)

    print('-=-'*30)
    print('Analyzing the reported values...')

    for n in num:
        print(f'{n} ', end='', flush=True)
        time.sleep(0.5)
    print(f'They were informed and {len(num)} values ​​in total.')

    if len(num) == 0:
        print('The biggest number reported it was 0.')
    else:
        print(f'The biggest number reported it was {max(num)}')
    
    print('-=-'*30)


maior(1, 3, 6, 8, 9)
maior(2, 5, 7)
maior(1, 2)
maior(5)
maior()