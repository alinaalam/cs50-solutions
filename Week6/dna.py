# a program that checks for DNA sequences
from sys import argv
import sys
import csv


def main():
    if (len(argv) != 3):
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    dna_database = read_dna_database(argv[1])
    dna_sequence = read_dna_sequence(argv[2])

    # the header also contains 'name' in it
    header = list(dna_database[0].keys())

    strs = count_strs(dna_sequence, header)
    find_person(dna_database, strs)


def read_dna_database(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        return list(reader)


def read_dna_sequence(filename):
    file = open(filename, "r")
    return file.read()


def count_strs(dna_sequence, header):
    strs = {}

    for i in range(1, len(header)):
        key = header[i]
        key_length = len(key)

        max_substring = 0
        temp_max = 0
        for j in range(len(dna_sequence)):
            if ((dna_sequence[j:j + key_length]) == key):
                temp_max += 1
                # check for the next occurring substrings and add them
                while dna_sequence[j - key_length: j] == dna_sequence[j: j + key_length]:
                    temp_max += 1
                    j += key_length

            max_substring = max(max_substring, temp_max)
            temp_max = 0

        strs[key] = max_substring

    return strs


def find_person(people, strs):
    for i in range(len(people)):
        person_found = True
        for header in strs.keys():
            if (int(people[i][header]) != strs[header]):
                person_found = False
                break
        if (person_found):
            print(people[i]['name'])
            exit()
    print("No match")


main()
