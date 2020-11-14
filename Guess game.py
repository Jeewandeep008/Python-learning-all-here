# GUESS GAME
def guess_game(s_no):
    # The secret code will be stored here
    secret_name = s_no
    # The answer of the user will be stored here temporarily
    guess = ""
    # The number of times the user has guessed from beginning
    guess_counts = 0
    # The number of times the user can guess
    guess_limit = 3
    # If the user has
    out_of_guess = False

    while guess != secret_name and not(out_of_guess):
        if guess_counts < guess_limit:
            guess = input('What is chocolate made of? : ')
            guess_counts += 1
        else:
            out_of_guess = True

    if out_of_guess:
        print('You are out of guesses & YOU LOSE !')
    else:
        print('You won the GAME !')

# print(guess_game('coco'))

# Unlimited guesses
def guess_game_1(secret_no):
    # The secret code will be stored here
    secret_name = secret_no
    user_guess = ""
    # Condition
    while user_guess != secret_name:
        user_guess = input('What is chocolate made of? : ')

    else:
        print('You won the Game !!')

print(guess_game_1('coco'))
