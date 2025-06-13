words = ('learning', 'person', 'house', 'united states')

for word in words:
    print(f'\nIn word "{word.upper()}" we have these vowels: ', end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')