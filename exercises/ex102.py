def factorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' x ' if c > 1 else ' = ')
        f *= c
    return f

print(factorial(5))              
print(factorial(5, show=True))   
print(factorial())               