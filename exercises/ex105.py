def notes(*n, situation=False):
    data = {}

    data['total'] = len(n)
    data['bigger'] = max(n)
    data['minor'] = min(n)
    data['average'] = sum(n) / len(n)

    if situation:
        if data['average'] >= 7:
            data['situation'] = 'Good'
        elif data['average'] >= 5:
            data['situation'] = 'Reasonable'
        else:
            data['situation'] = 'Bad'
    return data

answer = notes(5.5, 9, 7.5, 8, situation=True)
print(answer)