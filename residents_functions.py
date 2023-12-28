import csv
import json

def add_resident(file_name):
    print("Add resident")
    # Ask the title of the resident
    resident_name = input("Enter new resident: ")
    # Open file - list.csv
    with open(file_name, "a") as f: 
        writer = csv.write(f)
        # Insert values 
        writer.writerow([resident_name, "False"])
    
