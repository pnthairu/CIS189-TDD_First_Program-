#Start Program
"""
Program: Variable.py
Author: Paul Thairu
Last date modified: 06/03/2020

The purpose of this program is to write a function
that converts a persons age (number of years) into months
"""
# Creating a function convert_to_months that takes in a parameter for one's age in years
def convert_to_months(age_in_years):
    # return user age in years input and converts to months
    return age_in_years*12


if __name__ == '__main__':
    # Get user input and store a variable
    age_in_years = input("Please enter the age in years: ")
    # Declare and initialize a variable age_in_months from user input and converting into months
    age_in_months = convert_to_months(float(age_in_years))
    # Output for the age in months after converting from years to months
    print("Your age in months is " + str(age_in_months))

#End of Program

