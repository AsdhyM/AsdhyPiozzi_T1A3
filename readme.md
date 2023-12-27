# Terminal Application

## Overview
This is a Database used to store Resident's private and personal information in the Age Care setting. This Terminal Applicacion is under constructin and any new features will be added in the readme file.

### Created a virtual environment and activated it to install packages
To be able to install the packages in the virtual environment, the following commands were used in terminal

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install (package-name)
pip3 freeze>requirements.txt
```

### Imported Packages
This is the list of packages that had to be installed in order to create the terminal app and in order to use them w need to import them in the console.

```py
import pandas as pd 
import numpy as np 
from datetime import datetime
import sqlite3
from sqlite3 import Error
from setuptools import setup
import pathlib
```

### Requirements.txt
After the installation of the packages, the following was typed in terminal to create the requirements.txt which contains a list of the packages and libraries needed for the terminal application to work.  

`pip3 freeze>requirements.txt`

### .DB File
Created db file extension to store the information of the residents called residents_list.db

```py
def = pd.DataFrame(
    {
        "Room": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Name": [
            "Mama Morales",
            "Josephine Sawtell",
            "Claudio Martin",
            "Geneve Ray",
            "Rose Smith",
            "Charlotte George",
            "Mark Williamson",
            "Sharon Allen",
            "David Stoten",
            "Judith Powel",
        ],
        
        "Date_of_birth": ["12/03/1946", "24/05/1939", 
                          "06/08/1949", "14/01/1952", 
                          "03/12/1944", "07/11/1951", 
                          "10/10/1948", "29/02/1939", 
                          "18/11/1948", "03/03/1943",
        ],
        "Sex": ["female", "female", "male", "female",
                "female", "female", "male", "female", 
                "male", "female",
        ],
        "Dementia": ["Alzheimer's Disease", "Unspecified Dementia",
                     "Alzheimer's Disease", "Vascular Dementia", 
                     "Alzheimer's Disease", "Creutzfeldt-Jakob Disease", 
                     "Frontotemporal Dementia", "Parkinson's Dementia", 
                     "Alzheimer's Disease", "Alzheimer's Disease",
        ],
        "Allergies": [["Paracetamol", "Aspirin", "Codeine"], 
                      "NKA", "Adhesive dressings", "Donzepril", 
                      "NKA", "NKA", "Oxycodone", 
                      ["Diltiazem", "Amoxicillin", "Enalaprin Ramipril"], 
                      "Morphine", ["Morphine", "Aspirine", "Anti-Inflammatories", 
                      "Tregetol", "Mouthwash", "Penicillin", "Codeine", 
                      "Valium", "Marcaine"],
        ],
        "Order": ["NFR", "CPR", "CPR", "CPR", "NFR", "NFR", "CPR", 
                  "NFR", "NFR", "NFR",
        ]
    }
)

print(df)
```
