def calculate_area(width, length):
    return width * length

print('Land control')
print('-'*10)

width = float(input('Width (m): '))
length = float(input('Length (m): '))

area = calculate_area(width, length)

print(f'The area of ​​a plot of land {width}x{length} is {area}m²')