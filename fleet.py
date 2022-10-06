"""
##### FLEET #####
AUTHOR: Leslie A. McFarlin, Principal UX Architect @ Wheels-Donlen
CREATE DATE: 30 Sept 2022

Desc: Fleet-specific functions.

"""



##### IMPORTS #####
# Generate data frame
import pandas as pd

# Random numbers as needed
import random

# Assist with string functionality
import string as st

##### GLOBAL VARIABLES #####
# Uppercase letters
letters = st.ascii_uppercase
# Integers
numbers = st.digits



########## FLEET DETAIL FUNCTIONS ##########
# Indicates the number of fleets to create between 1 and 7.
# multi_fleet is based off of the Y/N user input.
# records_count is based off of the user input.
def fleetCount(multi_fleet, records_count):
    # Initialize variables
    fleet_count = int()
    # Conditional to calculate fleet size
    if multi_fleet.lower() == 'n' or multi_fleet.lower() == 'no':
        # Only create 1 fleet
        fleet_count = 1
    else:
        # Calculate to create the number of fleets
        fleet_count = records_count//5
        # Cap the total number of fleets at 7 to reflect reality
        if fleet_count > 7:
            fleet_count = 7
    # Return the number of fleets
    return fleet_count



# Generate fleet IDs
# country is based on the user input
def createFleetID(country):
    # US
    if country.lower() == 'us':
        id_prefix = '3'
    # Canada
    elif country.lower() == 'canada':
        id_prefix = '7' 
    # Create an id string
    id_string = id_prefix + "".join(random.choices(letters, k=3))
    # Return
    return id_string                                



# Split the fleets between US and Canada
# 70/30 split US-to-Canada
def fleetSplitter(fleet_count):
    # US fleet count
    us_fleet_count = round(fleet_count*0.70) # Nearest whole number
    # Canadian fleet count
    can_fleet_count = fleet_count - us_fleet_count
    # Return calculations
    return us_fleet_count, can_fleet_count



# Create the list of fleet IDs
def getFleetList(country, fleet_count):
    # Fleet ID list
    fleet_id_list = []
    # Counter
    counter = 0
    # If country is US or Canada
    if country.lower() != 'both':
        # Create as many Fleet IDs as there are fleets
        while counter < fleet_count:
            # Append to list
            fleet_id_list.append(createFleetID(country))
            # Increment counter
            counter += 1
    # If country is both
    else:
        # Fleet counts
        us_fleet_count, can_fleet_count = fleetSplitter(fleet_count)
        # US Fleet IDs
        while counter < us_fleet_count:
            fleet_id_list.append(createFleetID('us'))
            counter += 1
        # Reset the counter
        counter = 0
        # Canadian fleets
        while counter < can_fleet_count:
            fleet_id_list.append(createFleetID('canada'))
            counter += 1
        counter = 0
    # Return the fleet id list
    return fleet_id_list
        

    
##### VEHICLES PER FLEET #####
# Calculate the number of vehicles per fleet
# Only called when fleet_count is greater than 1.
# records_count is how many vehicles are needed.
# fleet_count is the number of fleets.
def fleetSizeCalculator(records_count, fleet_count):
    # Floor division to capture the base count per fleet
    base_fleet_size = records_count//fleet_count
    # Find the difference between total_vehicles and base_fleet_size
    # The number here is the amount of vehicle records to split across
    # all of the fleets.
    overflow_size = records_count-(fleet_count*base_fleet_size)
    extra_fleet_size = overflow_size + base_fleet_size 
    # Return fleet sizing
    return base_fleet_size, extra_fleet_size



# Random index selection
def randomIndexSelector(start_int, end_int):
    return random.randint(start_int, end_int)



# Set the size per fleet
# fleet_id_list is the list of fleet IDs
# base_fleet_size is the size of each fleet
# extra_fleet_size is an optional argument that applies only when
# base_fleet_size has remaining vehicle counts after being calculated.
"""
Returns the dictionary needed to power the creation of the rest of the data points.
"""
def fleetSizer(fleet_id_list, base_fleet_size, extra_fleet_size):
    # Create a dictionary to hold the fleet ID and corresponding fleet size
    # key is fleet ID
    # value is fleet size
    fleet_id_dictionary = {}
    # Only if extra_fleet_size > 0
    if extra_fleet_size > 0: 
        # Randomly select an index value
        idx = randomIndexSelector(0, len(fleet_id_list)-1)
        extra_fleet_id = fleet_id_list[idx]
    # Select
    for id_ in fleet_id_list:
        # Verify that extra_fleet_id exists
        try:
            extra_fleet_id
            # When at the designated fleet_id assign it the extra value
            if id_ == extra_fleet_id:
                fleet_id_dictionary[id_] = extra_fleet_size
            # Assign all others the base value
            else:
                fleet_id_dictionary[id_] = base_fleet_size
        # If extra_fleet_id does not exist
        except:
            fleet_id_dictionary[id_] = base_fleet_size
    # Return
    return fleet_id_dictionary



########## DIVISIONS ##########
# Generate random combinations of numbers and letters
def randomGenerator(random_set, int_):
    # Create
    div_component = ''.join(random.choice(random_set) for x in range(int_))
    # Return
    return div_component



# Division ID creator
def divIDCreator(fleet_id):
    # List of counts
    int_counts = [2, 6, 4]
    # List of global variables
    var_list = [letters, numbers, numbers]
    # Division ID string
    division_id = fleet_id
    for i in range(len(int_counts)):
        this_component = randomGenerator(var_list[i], int_counts[i])
        division_id = division_id + ':' + this_component
    # Return
    return division_id