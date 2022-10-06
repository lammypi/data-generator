"""
##### LOCATIONS #####
AUTHOR: Leslie A. McFarlin, Principal UX Architect @ Wheels-Donlen
CREATE DATE: 28 September 2022

DESC: random_names randomly generates the following:
      - US City and State combinations
      - Canadian City and Province combinations
      - Street names
"""

# Imports
import os
import csv # NOTE: THIS CAN READ TXT FILES
import pandas as pd
import random
import string as st



##### READ IN NECESSARY FILES #####
# Read in can_provinces
# Generates a nested list where each line is accessed via square brackets.
# Each nested list contains 3 strings: Province, city, postal code
# Access each string using square brackets with indices 0 thru 2.
with open('can_provinces.txt', 'r') as f:
    reader = csv.reader(f)
    provinces = list(reader)
    
# Read in us_states
# Generates a nested list where each line is accessed via square brackets.
# Each nested list contains 3 strings: State, city, zipcode
# Access each string using square brackets with indices 0 thru 2.
with open('us_states.txt', 'r') as f:
    reader = csv.reader(f)
    states = list(reader)
    
# Read in street_names
with open('street_names.txt', 'r') as f:
    reader = csv.reader(f)
    streets = list(reader)
    
    

##### GLOBAL VARIABLES #####
# Uppercase letters
letters = st.ascii_uppercase
# Integers
numbers = st.digits



##### RETURN RANDOM LOCATION NAMES #####
# US City and State
def cityState(states):
    # Get the random integer
    idx = random.randint(0, len(states)-1)
    # Get the nested list for the index
    location = states[idx]
    # Get the city, state, zip
    state = location[0]
    city = location[1]
    zipcode = location[2]
    # Return city, state, zip
    return state, city, zipcode

# Canadian City and Province
def cityProvince(provinces):
    # Get the random integer
    idx = random.randint(0, len(provinces)-1)
    # Get the nested list for the index
    location = provinces[idx]
    # Get the province, city, postal code combo
    province = location[0]
    city = location[1]
    postal_code = location[2]
    # Return city and province
    return province, city, postal_code

# Streets
def streetNames(streets):
    # Types of thoroughfares
    thoroughfares = ['Rd.', 'St.', 'Ave.', 'Pkwy.', 'Hwy.', 'Ln.', 'Blvd.']
    # Get the random integer
    idx = random.randint(0,len(streets)-1)
    # Pick a street type at random
    street_type = thoroughfares[random.randint(0, len(thoroughfares)-1)]
    # Pick a street name at random
    street_name = streets[idx][0]
    # Create the full name
    full_street = street_name  + " " + street_type
    # Return
    return full_street



########## GENERATE ADDRESSES ##########
# Generate a street address
# country refers to the inputted user value
def getAddress():
    addr_size = random.randint(2, 6)
    # For rural addresses
    if addr_size == 6:
        num_pt1 = ''.join(random.choices(str(numbers), k=2))
        dir = random.choice(['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE'])
        num_pt2 = ''.join(random.choices(str(numbers), k=3))
        this_addr = num_pt1+dir+num_pt2
    # For non-rural addresses
    else:
        this_addr = ''.join(random.choices(str(numbers), k=addr_size))
    # Generate the full_address
    street_address = this_addr + " " + streetNames(streets)
    # Return
    return street_address