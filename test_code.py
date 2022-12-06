from random import randint




random_choice = randint(1, 9)
is_guess_number = False
while not is_guess_number:
    Guess_the_numbers = int(input('Guess a number between 0 and 9\n'))
    if Guess_the_numbers == random_choice:
        is_guess_number = True
        print('you found me')
    elif Guess_the_numbers > random_choice:
        print('Too high , try again!')
    else:
        print('Too low, try again!')