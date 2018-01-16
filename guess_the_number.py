import random

correct = 'you guessed correctly!'
too_low = 'Too Low'
too_high = 'too high'
guesses = 0

def configure_range():
    '''Set the high and low values for the random number'''
    low = int(input("Lowest possible number for secret number?\n"))
    high = int(input("Highest possible number for secret number?\n"))
    return low, high


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
    replay = "y"

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while replay=="y" or replay=="Y" or replay=="Yes" or replay=="YES":
        try:
            guess = get_guess()
            guesses+=1
            result = check_guess(guess, secret)
            print(result)

            if result == correct:
                print("Number of guesses: " + str(guesses))
                replay = input("Would you like to play again? (y/n)\n")
                if replay!="y" or replay!="Y" or replay!="Yes" or replay!="YES":
                    print("Goodbye!")
                    exit(0)
                (low, high) = configure_range()
                secret = generate_secret(low, high)
                guesses = 0

        except ValueError:
            print('needs to be a number, guess again')
            guess = get_guess()


if __name__ == '__main__':
    main()
