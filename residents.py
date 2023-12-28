import pandas as pd 
import numpy as np 
from datetime import datetime
import sqlite3
from sqlite3 import Error
import os
import time
import traceback
import sys
from sys import platform
from setuptools import setup
import pathlib
import csv
import json
from colored import Fore, Back, Style


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
        return conn
    except Error as e:
        print(e)
        return None

# Close the connection to a SQLite database
def close_connection(conn):
    try:
        conn.close()
        return True
    except Error as e:
        print(e)
        return False
    

# Passing the file to the function to create database
if __name__ == '__main__':
    try:
        begintime=datetime.now()
        print("Start of Main Processing - " + str(begintime.strftime("%H:%M:%S")))
        db_file = r"C:\sqlite\db\pythonsqlite.db"

        # Connect to database
        conn1=create_connection(db_file)

        # Close connection
        if conn1 != False:
            close_connection(conn1)
            # Set succes info
            exitcode=0
            exitmessage='DB test program completed successfully'
        
        
    # Catch exceptions
    except Exception as ex:
        exitcode=99
        exitmessage=str(ex)
        print('Traceback Info')
        traceback.print_exc()

    # Final processing
    finally:
        print('ExitCode:' + str(exitcode))
        print('ExitMessage:' + exitmessage)
        endtime=datetime.now()
        print("End of Main Processing - " + str(endtime.strftime("%H:%M:%S")))
        print("Elapsed Processing Time - " + str(endtime - begintime))


file_name = "list.csv"

try:
    # Open the file in read mode
    residents_file = open(file_name, "r")
    residents_file.close()
    print("In try block")
except FileNotFoundError:
    residents_file = open(file_name, "w")
    residents_file.write("title,compelte\n")
    residents_file.close()
    print("In except block")


print(f"{Fore.blue}{Back.black}Welcome to Resident's Info{Style.reset}")

# def residents_data():
#     # Defining the function to start the dataframe when called.
#     residents_data_frame = pd.DataFrame({
#         "Room": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#         "Name": [
#             "Mama Morales",
#             "Josephine Sawtell",
#             "Claudio Martin",
#             "Geneve Ray",
#             "Rose Smith",
#             "Charlotte George",
#             "Mark Williamson",
#             "Sharon Allen",
#             "David Stoten",
#             "Judith Powel",
#         ],
#         "Date_of_birth": ["12/03/1946", "24/05/1939", 
#                         "06/08/1949", "14/01/1952", 
#                         "03/12/1944", "07/11/1951", 
#                         "10/10/1948", "29/02/1939", 
#                         "18/11/1948", "03/03/1943",
#         ],
#         "Sex": ["female", "female", "male", "female",
#                 "female", "female", "male", "female", 
#                 "male", "female",
#         ],
#         "Dementia": ["Alzheimer's Disease", "Unspecified Dementia",
#                     "Alzheimer's Disease", "Vascular Dementia", 
#                     "Alzheimer's Disease", "Creutzfeldt-Jakob Disease", 
#                     "Frontotemporal Dementia", "Parkinson's Dementia", 
#                     "Alzheimer's Disease", "Alzheimer's Disease",
#         ],
#         "Allergies": [["Paracetamol", "Aspirin", "Codeine"], 
#                     "NKA", "Adhesive dressings", "Donzepril", 
#                     "NKA", "NKA", "Oxycodone", 
#                     ["Diltiazem", "Amoxicillin", "Enalaprin Ramipril"], 
#                     "Morphine", ["Morphine", "Aspirine", "Anti-Inflammatories", 
#                     "Tregetol", "Mouthwash", "Penicillin", "Codeine", 
#                     "Valium", "Marcaine"],
#         ],
#         "Order": ["NFR", "CPR", "CPR", "CPR", "NFR", "NFR", "CPR", 
#                 "NFR", "NFR", "NFR",
#         ]
#     })
#     return residents_data_frame

# df = residents_data()

data = pd.DataFrame()

# Requesting input from user to add residents into dataframe
def add_rows(data): 
    # Adding rows until there's an 'N' input
    more_residents = True
    while more_residents: 
        new_resident_data_frame = {
                        'Room': int(input("Enter Room number of new resident: ")),
                        'Name': str(input("Enter the fullname of new resident: ")),
                        'Date_of_birth': datetime.strptime(input("Enter Date of Birth of new resident(DD-MM-YYYY): "), "%d-%m-%Y"),
                        'Sex': str(input("Enter new resident's gender(female or male): ")),
                        'Dementia': str(input("Enter the type of Dementia of the new resident: ")),
                        'Allergies': str(input("Enter the new resident's allergies: ")),
                        'Order': str(input("Enter life/death order: "))
        }
        print("Type of data before append:", type(data))
        data = pd.concat([data, pd.DataFrame([new_resident_data_frame])], ignore_index=True)
        # data = data._append(new_resident_data_frame, ignore_index = True)
        # pd.concat([data, new_resident_data_frame])
        print("Type of data after append:", type(data))

        more_residents = input('Add another [Y, N]: ')

        if more_residents.upper() == 'N':
            # print("Type of data after append:", type(data))
            return data

# data = pd.DataFrame()

user_input = ""

# data = add_rows(data)

print(data)

while user_input != "N":
    data = add_rows(data)
    print(data)
    user_input = input('Add another resident [Y, N]: ')
    # if(user_input == "Y"):
    #     data = add_rows(data)

print(data)


print("Thank you for using Resident's Terminal Application")






