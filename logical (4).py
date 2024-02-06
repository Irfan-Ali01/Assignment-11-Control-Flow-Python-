year=int(input('Enter Year: '))
if year%4==0:
    print(year,' is a Leap Year')
elif year%4!=0:
    print(year,' is not a Leap Year')
else:
    print('Invalid Operation')