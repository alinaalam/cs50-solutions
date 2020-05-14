# a program that calculates the minimum number of coins required to give a user change
from cs50 import get_float


def main():
    while True:
        change = get_float("Change owned: ")
        if (change >= 0):
            break
    calculate_change(change * 100)


def calculate_change(change):
    coins = 0

    while (change > 0):
        if (change >= 25):
            change = change - 25
        elif (change >= 10):
            change = change - 10
        elif (change >= 5):
            change = change - 5
        else:
            change = change - 1
        coins += 1

    print(coins)


main()
