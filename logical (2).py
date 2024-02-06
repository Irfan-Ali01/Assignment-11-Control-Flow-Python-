while True:
    age=int(input('Enter your Age: '))
    if age<=12:
        print('You are a Child')
    elif age<=17:
        print('You are a Teenager')
    elif age<30:
        print('You are an Adult')
    else:
        print('You are a Senior Citizen')