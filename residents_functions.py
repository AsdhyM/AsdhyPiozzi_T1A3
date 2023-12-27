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





