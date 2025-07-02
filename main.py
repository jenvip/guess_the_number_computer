import random

def computer_guess(x): #computer guesses number based on user's input
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': #c for correct
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1 #example: if computer guesses 8 in a range of 1-10, and it's too high, then 9 & 10 are gone --> the new range has to be 8 - 1 = 7 so from 1-7
        elif feedback == 'l':
            low = guess + 1

    print(f'Congrats! The computer guessed the number {guess} correctly!')


computer_guess(10)
