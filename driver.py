"""
##### RANDOM NAMES #####
AUTHOR: Leslie A. McFarlin, Principal UX Architect @ Wheels-Donlen
CREATE DATE: 30 July 2022
LATEST UPDATE: 28 September 2022

DESC: random_names randomly generates the following:
      - first and last names

VERSION CHANGES: Moved location and vehicle functions to separate python files for improved function management.
"""


# Imports
import os
import csv # NOTE: THIS CAN READ TXT FILES
import pandas as pd
import random
import string as st



##### READ IN NECESSARY FILES #####
# Read in the first names text file
with open('first_name.txt', 'r') as f:
    reader = csv.reader(f)
    first_names = list(reader)
    
# Read in the last names text file
with open('last_name.txt', 'r') as f:
    reader = csv.reader(f)
    last_names = list(reader)

    

##### GLOBAL VARIABLES #####
# Uppercase letters
letters = st.ascii_uppercase
# Integers
numbers = st.digits



##### RETURN RANDOM NAMES #####
# First Name
def firstName(first_names):
    # Get a random index value
    idx = random.randint(0, len(first_names)-1)
    # Get a the corresponding first name
    first_name = first_names[idx][0].rstrip()
    # Return first name
    return first_name



# Last Name
def lastName(last_names):
    # Get a random index value
    idx = random.randint(0, len(last_names)-1)
    # Get the random last name
    last_name = last_names[idx][0].rstrip()
    # Return last name
    return last_name



# Create emails for drivers
def getEmail(first_name, last_name, company):
    # Create - convert to lower case
    company_domain = "-".join(company.lower().split(" "))+".com"
    # Create the ID
    email_id = first_name + "." + last_name
    # Create the email addresses
    email_addr = email_id + "@" + company_domain
    # Return
    return email_addr
    
    
    
# Create phone numbers
def getPhoneNumber():
    # Area code
    area_code = str(random.randint(100,999))
    # Prefix
    prefix = str(random.randint(100,999))
    # Line number
    line_number = [(''.join(random.choice(str(numbers)))) for i in range(0,4)]
    line_number_str = ''.join(map(str, line_number))
    # Full phone number
    phone_number = area_code + prefix + line_number_str
    # Return
    return phone_number
    
    
    
# Generate a driver ID
def getDriverID():
    # Randomly generate a driver ID
    driver_id = ''.join(random.choice(letters + str(numbers)) for x in range(5))
    # Return
    return driver_id
    