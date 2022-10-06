"""
##### MAIN #####
AUTHOR: Leslie A. McFarlin, Principal UX Architect @ Wheels-Donlen
CREATE DATE: 25 Feb 2022
UPDATE DATE: 27 Sept 2022

DESC: data_generator is a python program to generate random data sets for use in UX prototypes.
      It automatically generates company, fleet, vehicle, and driver details.
      Users need to include the following information: 
      Number of companies, country/ies, number of fleets, number of records needed

VERSION CHANGES: Switched to generator class to improve time + complexity. 
                 More modularization.
"""

##### IMPORTS #####
# Generate data frame
import pandas as pd

# Random numbers as needed
import random

# Assist with string functionality
import string as st

# Additional python modules
from driver import * # Generate driver details
from locations import * # Generate locations in the US and Canada
from vehicles import * # Generate vehicle details
from fleet import * # All fleet functionality



##### USER INPUTS #####

# Check that the user has entered an int value between 1 and 500
def recordPromptChecker(prompt):
    # Handling records_count input
    while True:
        # Check is an integer
        try:
            count = int(input(prompt))
        # Throw an error if the data type is not int
        except ValueError:
            print("The vehicle count must be a whole number.")
            continue
        # If value is out of range
        if count < 1 or count > 500:
            print("Please enter a value between 1 and 500.")
            continue
        else:
            break
    # No issues with input
    return count
    
    
    
# Check that the user has entered an acceptable Y/N response
def multiFleetChecker(prompt):
    # Fleet response list
    response_list = ['Yes', 'No', 'Y', 'N', 'yes', 'no', 'y', 'n']
    # Handling multi_fleet input
    while True:
        # Check is a string
        try:
            fleets = str(input(prompt)) 
        # Throw an error if not a string
        except ValueError:
            print("Please indicate yes or no.")
            continue
        # If value is not acceptable.
        if fleets not in response_list:
            print("Please indicate yes or no.")
            continue
        else:
            break
    # No issues with input
    return fleets
    
    
    
# Check that the user has entered a covered country
def countryChecker(prompt):
    # Country list
    country_list = ['US', 'Canada', 'Both', 'us', 'canada', 'both']
    # Handling country input
    while True:
        # Check is a string
        try:
            locale = str(input(prompt))
        except ValueError:
            print("Please indicate US, Canada, or both.")
            continue
        # If value is not acceptable
        if locale not in country_list:
            print("Please indicate US, Canada, or both.")
            continue
        else: 
            break
    # No issues with input
    return locale
    
    
    
##### RETURN COMPANY DETAILS #####   
# Get the country of the company
def getName(country):
    # If the US
    if country == 'us':
        company_name = "ABC Corp"
    # If Canada
    elif country == 'canada':
        company_name = "Can Corp"
    # Return the company's country
    else:
        company_name = "Client-Corp"
    # Return the company name
    return company_name



##### UPDATE DATAFRAME #####
def updateDF(dataframe, idx, value):
    # Column counter
    col_counter = 0
    # Iterate across columns
    for col in dataframe.columns:
        # Insert the value
        dataframe.at[idx, col] = value
        
    
    
########## USER INPUT PROMPTS ##########
# User inputs will serve as global variables accessible to all within the program
# Number of records to create
records_count = recordPromptChecker('How many vehicles do you need? [1-500]:')

# Check if single or multiple fleets.
multi_fleet = multiFleetChecker('Should there be multiple fleets? [Y/N]:')

# Country/ies company/ies should be in
country = countryChecker('Which countries should the fleet(s) be in? [Canada, US, both]:')

# Company name - Based on user input prompts
company_name = getName(country)


 
##### MAIN MODULE #####
def main():
    """ INITIALIZE A DATAFRAME """
    # Dataframe indexer
    idx = 0
    # Column list for the dataframe
    col_list = ['Vehicle ID',
                'Year',
                'Make and Model',
                'VIN',
                'Plates',
                'Fleet ID',
                'Division ID',
                'First Name',
                'Last Name',
                'Driver ID',
                'Email',
                'Phone Number',
                'Street Address',
                'City',
                'State/Province',
                'Zip/Postal Code']
    # Dataframe to generate a CSV file
    dataset = pd.DataFrame(columns = col_list)
    
    """ SET UP THE FLEET BASICS """
    # Number of fleets
    fleet_count = fleetCount(multi_fleet, records_count)
    # List of fleet IDs
    fleet_id_list = getFleetList(country, fleet_count)
    # Calculate fleet size
    base_fleet_size, extra_fleet_size = fleetSizeCalculator(records_count, fleet_count)
    # Link fleet ID to fleet size
    fleet_id_dictionary = fleetSizer(fleet_id_list, base_fleet_size, extra_fleet_size)
    
    """ ITERATE THROUGH LIST OF FLEET IDs """
    dataset_values_list = []
    for _id in fleet_id_list:
        # Generate all of the fields that only change with fleet ID
        this_division_id = divIDCreator(_id) # Division ID
        # Location fields
        # US
        if _id[0] == '3':
            state_province, city, zip_postal_code = cityState(states)
        # Canada
        else: 
            state_province, city, zip_postal_code = cityProvince(provinces)
        # Retrieve the size of that fleet
        this_fleet_size = fleet_id_dictionary[_id]
        # Initialize a counter variable
        counter = 0
        # Generate all of the data points unique to the 
        while counter < this_fleet_size:
            # Names - for ease of updating using pandas at()
            first_name = firstName(first_names)
            last_name = lastName(last_names)
            # Update the dataframe
            dataset.at[idx, 'Vehicle ID'] = getVehicleID()
            dataset.at[idx, 'Year'] = year()
            dataset.at[idx, 'Make and Model'] = makeModel(vehicles)
            dataset.at[idx, 'VIN'] = getVIN()
            dataset.at[idx, 'Plates'] = getPlates()
            dataset.at[idx, 'Fleet ID'] = _id
            dataset.at[idx, 'Division ID'] = divIDCreator(this_division_id) # Tied to Fleet ID
            dataset.at[idx, 'First Name'] = first_name
            dataset.at[idx, 'Last Name'] = last_name
            dataset.at[idx, 'Driver ID'] = getDriverID()
            dataset.at[idx, 'Email'] = getEmail(first_name, last_name, company_name)
            dataset.at[idx, 'Phone Number'] = getPhoneNumber()
            dataset.at[idx, 'Street Address'] = getAddress()
            dataset.at[idx, 'State/Province'] = state_province # Tied to Fleet ID
            dataset.at[idx, 'City'] = city
            dataset.at[idx, 'Zip/Postal Code'] = zip_postal_code
            # Update the counter
            counter += 1
            # Update the idx
            # idx should align with counter value at the end
            idx += 1
    
    # Return CSV
    dataset.to_csv('prototype_fleet_data.csv', index=False)
    
    # Alert user
    print("Your data is ready. Check the directory you're running this script from for a CSV file named prototype_fleet_data.")
    
##### EXECUTE MAIN #####
main()