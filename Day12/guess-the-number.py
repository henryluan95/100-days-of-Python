import random;
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    guessing_number = random.randint(0, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        numbers_of_guess = 10
    else:
        numbers_of_guess = 5

    game_over = False
    def check_guess(guess, guessing_number, numbers_of_guess):
        if (guess < guessing_number):
            print("Too low.")
            return numbers_of_guess - 1
        elif (guess > guessing_number):
            print("Too high.")
            return numbers_of_guess - 1
        else:
            print("You wins")

    print(guessing_number)
    guess = 0
    while guess != guessing_number:
       print(f'You have {numbers_of_guess} attempts remaining to guess the number')
       guess = int(input("Make a guess: "))
       numbers_of_guess = check_guess(guess, guessing_number, numbers_of_guess)
       if(numbers_of_guess == 0):
           print("You loses")
           return


game()
