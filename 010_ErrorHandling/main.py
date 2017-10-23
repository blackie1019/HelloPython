inputStr = ''
while inputStr != 'q':
    print('Please input any number!')
    try:
        inputStr = input()
        number = int(inputStr)
        if(number>100):
            print('Your input is more than 100')
        else:
            print('Your input is less than or equal to 100')
    except ValueError:
        print('Error Happen via input incorrct!')