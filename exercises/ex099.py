import time

def bigger(* num):
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


bigger(1, 3, 6, 8, 9)
bigger(2, 5, 7)
bigger(1, 2)
bigger(5)
bigger()