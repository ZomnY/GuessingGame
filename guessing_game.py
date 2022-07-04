import random

def set_range ():
    """ 
    This function queries the user to enter the upper bound for the guessing game.
    The entry has to be greater than 0 and an integer.
    """

    range = 0
    while range == 0:
        try:
            range = int(input("Set the range of the guessing game. It needs to be greater than 1 and an integer. \nINPUT: "))
        except ValueError:
            range = 0
            
        if range < 1:
            print("Entry error! Again.")
            range = 0
    return range


def guess(x):
    """
    This is the function that runs the guessing game against the computer.
    The parsed value sets the upper bound for the game. It needs to be greater than 0 and an integer.
    """

    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"\n\nYay, congrats. You have guessed the number {random_number} correctly!")


guess(set_range())

close = input("\n\n-- Press enter to close the programm --")