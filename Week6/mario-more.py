# program that generates a pyramid with user defined height
from cs50 import get_int


def main():
    while True:
        height = int(get_int("Height: "))
        if (height >= 1 and height <= 8):
            break
    generate_pyramid(height)


def generate_pyramid(height):
    spaces = height - 1

    while (spaces >= 0):
        if (spaces > 0):
            print(" " * spaces, end="")
        print("#" * (height - spaces), end="")
        print("  ", end="")
        print("#" * (height - spaces))
        spaces -= 1


main()
