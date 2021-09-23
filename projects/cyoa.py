"""Choose your own adventure: number guessing game."""

__author__ = "730405432"

from random import randint

winning_number: int = randint(1, 10)
# points will keep track of number of attempts made by the user which is equivalent to their score, lowest score wins
points: int 
player: str = ""
guess: int
WINKY: str = "\U0001F60F"
PEACE_FINGERS: str = "\U0000270C"
CRY_EMOJI: str = "\U0001F622"


def main() -> None:
    """Number Guessing Game with Lil Nas X!"""
    greet()
    game()


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
        quit()
    else:
        if choice == "C":
            print(f"Bye bit***s{PEACE_FINGERS}")
            quit()
        else:
            rules()


def rules() -> None:
    """Rules of Lil Nas Numbers."""
    print(f"I'm thinking of a number 1-10, take a guess! You win if you guess what number I'm thinking, the lowest score wins! If you get it on the first try, I'll let you call my by my name. {WINKY}")


# Imput portion of the game, while loop will continue until the correct value is chosen.
def game() -> int:
    """Game execution and user input."""
    winning_number: int = randint(1, 10)
    # attempts will keep track of number of attempts made by the user which is equivalent to their score, lowest score wins
    points: int = 0
    guess: int = int(input("What's your initial guess? "))
    if guess == winning_number:
        print("You're right! Now you can join me on the Old Town Road of champions!")
        points = points
    else:
        while guess != winning_number and points < 3:
            print("Hahaha thats not it!")
            more_guessing: int = int(input("Take another shot at it: "))
            if more_guessing == winning_number:
                points = points + 1
                print(f"You did it! Your final score is {points}, Billy Ray would be so proud! Now we can party til the Sun Goes Down!")
                # the addition of the one represents the initial guess the player made
                return points + 1
            else:
                while more_guessing != winning_number and points < 3:
                    even_more_guessing: int = int(input("You're so close, try again: "))
                    points = points + 1
                    if even_more_guessing == winning_number:
                        points = points + 2
                        print(f"That's my number! Your final score is {points}, You belong in the ~number~ Industry Baby!")
                    else:
                        points = points + 2
                        print(f"You lost, sorry it looks like we aren't pyschically linked.{CRY_EMOJI}")
# the addition of the one represents the initial guess the player made
    print(f"Your final score is {points}! Billy Ray would be so proud!")
    return points


if __name__ == "__main__":
    main()