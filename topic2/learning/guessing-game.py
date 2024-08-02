from random import randint
#Initialise secret value and reset variables
secret_number = randint(0,100)
correct = False
first_guess = True
points = 200
guess_count = 0
#Print answer for testing purposes
#print(f'DEBUG: Answer = {secret_number}')
print(f'Guess the number between 1 and 100. The first guess is free, but after that, you\'ll start losing 10 more points than the last every turn you don\'t get it right!')
#Run until user is correct
while correct != True:
    guess_count += 1 #Increment guess count
    user_input = int(input('Guess your number between 1 and 100!\n'))
    if user_input == secret_number: #If correct
        print(f'Correct! You got the number in {guess_count} guesses')
        break
    elif points <= 0: #Out of points condition
        print(f'You lose! The correct answer was: {secret_number}')
        break
    else: #Incorrect answer logic
        if user_input > secret_number: #If too high, let them know
            print(f'Incorrect! Your number was too high')
        else: #Otherwise, too low, let them know
            print(f'Incorrect! Your number was too low!')
        if not first_guess: #From guess 2 onwards, user will lose an incrementing amount of points per round, a turn counter would do the same thing but this is scarier. It equates to 7 guesses, they need to use a binary sort.
            points_lost = (guess_count*10)-10
            print(f'You just lost {points_lost} points!')
            points -= points_lost
            print(f'You have: {points} points remaining')
        else: #First guess is free, flip the value of first guess here so it doesn't run twice.
            first_guess = False
            print(f'The first guess was free, you still have {points} points')

