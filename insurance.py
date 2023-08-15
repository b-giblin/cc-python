# Author: Brian Giblin
# Date: 8/15/23
# Description: A short program using f strings and user input to simulate an insurance policy.

company_name = input("What is your insurance companies name?") 
emplyee_amount = input("How many employees do you have?")
location = input("What is your city, counrty, or state?")
lowest_price = input("What is your lowest priced policy?")
highest_price = input("What is your highest priced policy?")

print(f"We are {company_name} located in {location}. Our {emplyee_amount} employees can help you find the policy that is right for you with policies ranging from {lowest_price} to {highest_price} per month!")

