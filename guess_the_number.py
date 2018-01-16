import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'
guesses = 0

def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    guesses = 0

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        try:
            guess = get_guess()
            guesses+=1
            result = check_guess(guess, secret)
            print(result + " Number of guesses: " + str(guesses))

            if result == correct:
                break

        except ValueError:
            print('needs to be a number, guess again')
            guess = get_guess()


if __name__ == '__main__':
    main()
