año = 2020

divisible4 = (año % 4 == 0) and (año % 100 != 0)
divisible400 = año % 400 == 0

if divisible4 or divisible400:
    print('Leap año!')
else:
    print('Not a leap año')
