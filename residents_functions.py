import pandas as pd 
import numpy as np 
from datetime import datetime
import sqlite3
from sqlite3 import Error
from setuptools import setup
import pathlib
import csv
import json


here = pathlib.Path(__file__).parent.resolve()

# Get long description from the readme file
long_description = (here / "readme.md").read_text(encoding="utf-8")


# Create a database connection to a SQLite database
# Defining the function
def create_connection(db_file):
    conn = None
    # Catching Errors
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# Passing the file to the function to create database
if __name__ == '__main__':
    create_connection(r"C:\sqlite\db\pythonsqlite.db")

# Requesting input from user to add residents into dataframe
def add_rows(residents_data):
    more_residents = True
    while more_residents:
        new_resident = {'Room': (int(input("Enter Room number of new resident: "))),
                        'Name': (int(input("Enter the fullname of new resident: "))),
                        'Date_of_birth': (int(input("Enter Date of Birth of new resident: "))),
                        'Sex': (int(input("Enter new resident's gender(female or male): "))),
                        'Dementia': (int(input("Enter the type of Dementia of the new resident: "))),
                        'Allergies': (int(input("Enter the new resident's allergies: "))),
                        'Order': (int(input("Enter life/death order: ")))
        }
        residents_data = residents_data.append(new_resident, ignore_index = True)
        more_residents = input('Add another [Y, N]: ')

        if more_residents == 'N':
            return residents_data
            break
        else:
            continue
df = add_rows(df)





