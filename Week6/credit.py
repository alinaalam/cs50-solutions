# a program that determines whether a provided credit card number is valid according to Luhn’s algorithm
import re
from cs50 import get_int


def main():
    while True:
        credit_card = get_int("Number: ")
        if (credit_card > 0):
            break
    validate_credit_card(credit_card)


def validate_credit_card(credit_card):
    sum = calculate_sum(credit_card)
    value = "INVALID"

    if (sum % 10 == 0):
        credit_card_str = str(credit_card)
        number_of_digits = len(credit_card_str)

        # american express
        if (number_of_digits == 15 and re.search("^(34)|(37)", credit_card_str)):
            value = "AMEX"
        elif (number_of_digits == 16 and re.search("^(51)|(52)|(53)|(54)|(55)", credit_card_str)):
            value = "MASTERCARD"
        elif (number_of_digits == 13 or number_of_digits == 16 and re.search("^4", credit_card_str)):
            value = "VISA"

    print(value)


def calculate_sum(credit_card):
    index = 1
    sum = 0

    while (credit_card > 0):
        number = credit_card % 10

        if (index % 2 == 0):
            number *= 2

        while (number > 0):
            sum += (number % 10)
            number //= 10

        credit_card //= 10
        index += 1

    return sum


main()
