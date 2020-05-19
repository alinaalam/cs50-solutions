# a program that talks to the database and send back result in alphabetical order
from sys import argv
import sys
import cs50
import csv


def main():
    if (len(argv) != 2):
        sys.exit("Usage: python roaster.py house_name")
    get_data_from_database(argv[1])


def get_data_from_database(house):
    # open that file for SQLite
    db = cs50.SQL("sqlite:///students.db")

    rows = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", house)
    for row in rows:
        if (row['middle'] == None):
            print(f"{row['first']} {row['last']}, born {row['birth']}")
        else:
            print(f"{row['first']} {row['middle']} {row['last']}, born {row['birth']}")


main()
