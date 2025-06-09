numbers = ('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')

while True:
    ask = int(input('Enter a number from 0 to 20: '))
    if ask >= 1 and ask <= 20:
        print(f'You entered the number {numbers[ask - 1]}')
        break
    else:
        print('Number out of range. Enter a number from 0 to 20: ')