# a program that imports csv file and stores it in database
from sys import argv
import sys
import cs50
import csv


def main():
    if (len(argv) != 2):
        sys.exit("Usage: python import.py characters.csv")

    filename = argv[1]
    reader = read_csv_file(filename)
    store_data_in_db(reader)


def read_csv_file(filename):
    with open(filename) as data:
        reader = csv.DictReader(data)
        return list(reader)


def store_data_in_db(reader):
    # open that file for SQLite
    db = cs50.SQL("sqlite:///students.db")

    for row in reader:
        name = row['name'].split(" ")
        first_name = name[0]
        middle_name = name[1] if (len(name) == 3) else None
        last_name = name[len(name) - 1]

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                   first_name, middle_name, last_name, row['house'], row['birth'])


main()
