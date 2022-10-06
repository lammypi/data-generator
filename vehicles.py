"""
##### VEHICLES #####
AUTHOR: Leslie A. McFarlin, Principal UX Architect @ Wheels-Donlen
CREATE DATE: 28 September 2022

DESC: random_names randomly generates the following:
      - Vehicle manufacturer and model combinations
"""

# Imports
import os
import csv # NOTE: THIS CAN READ TXT FILES
import pandas as pd
import random
import string as st
from datetime import date



##### READ IN NECESSARY FILES #####
# Read in make and models of vehicles
with open('vehicles.txt', 'r') as f:
    reader = csv.reader(f)
    vehicles = list(reader)



##### GLOBAL VARIABLES #####
# Uppercase letters
letters = st.ascii_uppercase
# Integers
numbers = st.digits



##### RETURN RANDOM YEAR, MAKE, MODEL #####    
# Generate a year randomly within the past 3 years from the current one
def year():
    # Get a year
    current_year = int(date.today().year)
    # Previous years - up to 3 years back
    prev_year_boundary = current_year - 3
    # Year range
    year = random.randint(prev_year_boundary, current_year)
    # Return year
    return year



# Generat a make and model
def makeModel(vehicles):
    # Random index value
    idx = random.randint(0, len(vehicles)-1)
    # Get the vehicle
    make_model = vehicles[idx][0]
    # Return vehicle
    return make_model
    
    

# Generate vehicle IDs
def getVehicleID():
    # Randomly generate a vehicle ID
    vehicle_id = ''.join(random.choice(letters + str(numbers)) for x in range(6))
    # Return vehicle ID
    return vehicle_id



# Generate a VIN
"""
NOTE: This will not generate real VINs. Real VINs operate on a check sum regarding number values and placements.
That is not being implemented here out of fear of generating a real VIN that could be tied to a client or to 
a non-client.
"""
def getVIN():
    # Randomly generate a VIN
    vin = ''.join(random.choice(letters + str(numbers)) for x in range(17))
    # Return VIN
    return vin
    
    
    
# Generate a license plate
"""
NOTE: Some states have specific patterns for vehicle types, but those will not appear here.
This function only generates a generic 6-char alphanumeric string.
"""
def getPlates():
    plate_number = ''.join(random.choice(letters + str(numbers)) for x in range(6))
    # Return plate number
    return plate_number