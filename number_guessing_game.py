#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: September 2019
# This lets the user guess a number


def main():
    # set number
    number = 5
    # input
    guess = int(input("Guess my number between 0 and 9: "))
    # process
    if guess == number:
        # output
        print()
        print("Correct! My number was", number)
    # process
    if guess != number:
        # output
        print()
        print("Sorry. Better luck next time")


if __name__ == "__main__":
    main()
