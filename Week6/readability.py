# a program that calculates the readability grade by using Coleman-Liau index; index = 0.0588 * L - 0.296 * S - 15.8
import re
from cs50 import get_string


def main():
    text = get_string("Text: ")
    grade = calculate_index(text)

    if (grade < 1):
        print("Before Grade 1")
    elif (grade >= 16):
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def calculate_index(text):
    words = count_words(text)

    L = (count_letters(text) * 100) / words
    S = (count_sentences(text) * 100) / words

    index = 0.0588 * L - 0.296 * S - 15.8

    return round(index)


def count_words(text):
    return len(text.split())


def count_letters(text):
    letters = 0
    text_length = len(text)
    
    for i in range(text_length):
        if (text[i].isalpha()):
            letters += 1
    
    return letters
    

def count_sentences(text):
    # need to subtract 1 because it also gives back an empty string
    return len(re.split(r"[.!?]", text)) - 1


main()
