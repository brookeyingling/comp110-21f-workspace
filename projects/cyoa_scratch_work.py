"""Choose your own adventure: murder mystery guessing game."""

from random import randint


def main() -> None:
    """Number Guessing Game with Lil Nas X!"""
    greet()
    game()
    print(f"Finally! Way to go your score is {attempts}! Now you can join me on the Old Town Road of Champions!")


def greet() -> None:
    """Game greeting and learn player's name --> segue into input portion of the game."""
    player: str = input("What's your name? ")
    print(f"Hey {player} it's Lil Nas X and welcome to Lil Nas Numbers! I'm thinking of a number 1-10, take a guess! If you win I'll let you call my by my name. \U0001F60F")


# Imput portion of the game, while loop will continue until the correct value is chosen.
def game() -> int:
    winning_number: int = randint(1, 10)
    # attempts will keep track of number of attempts made by the user which is equivalent to their score, lowest score wins
    attempts: int = 0
    # i is a variable the represents the maximum amount of attempts that can be made in the game
    i: int = 0
    guess: int = int(input("What's your initial guess? "))
    if guess == winning_number:
        print("You're right! You belong in the ~number~ Industry Baby")
        attempts = attempts + 1
    else:
        while guess != winning_number and i < 11:
            print("Hahaha thats not it!")
            more_guessing: int = int(input("Take another shot at it: "))
            if more_guessing == winning_number:
                attempts = attempts + 1
                # the addition of the one represents the initial guess the player made
                return attempts + 1
            else:
                while more_guessing != winning_number and i < 11:
                    more_guessing: int = int(input("Take another shot at it: "))
                    i = i + 1
                    attempts = attempts + 1
                    if more_guessing == winning_number:
                        attempts = attempts + 1
                        print("That's my number!")
                # the addition of the one represents the initial guess the player made
    return attempts + 1
    
    print(f"Your final score is {attempts}! Now we can party til the Sun Goes Down!")


if __name__ == "__main__":
    main()

guess: int = int(input("What is your initial guess? "))
winning_number: int = randint(1, 10)
# attempts will keep track of number of attempts made by the user which is equivalent to their score, lowest score wins
attempts: int = 0
player: str = input("What's your name? ")





def greet() -> None:
    """Game greeting and learn player's name --> segue into input portion of the game."""
    player: str = input("What's your name? ")
    print(f"Hey {player} it's Lil Nas X and welcome to Lil Nas Numbers! What do you want to do, here are your options: ")
    print("A: Play my awesome game!")
    print("B: Recieve an affirmation from yours truly!")
    print("C: Exit the game because you're lame.")
    A: str
    B: str
    C: str
    choice: str = input("What Old Town Road are you going to choose? ")
    if choice == "B":
        print("Live your life to its fullest potential and don’t really care too much about what other people think of you.")
    else:
        if choice == "C":
            print("Bye bit***s \U0000270C")
        else:
            game()