age = 12

guess = int(input('please guess my name:'))
print('your guess is', guess)

if guess > age:
    print('I am not that old')
elif guess < age:
    print('Do I look so young?')
else:
    print('Yes, you are right')


    
        