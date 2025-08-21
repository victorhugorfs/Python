try:
    a = int(input('Numerator'))
    b = int(input('Denominator'))
    r = a / b
except (ValueError, TypeError):
    print('We had a problem with the data types you entered!')
except ZeroDivisionError:
    print('It is not possible to divide a number by zero!')
except KeyboardInterrupt:
    print('The user preferred not to provide the data!')
except Exception as error:
    print(f'The error found was: {error.__cause__}')
else:
    print(f'The result is: {r:.1f}')
finally:
    print('Come back soon!')