#Genesis Ortiz-Leon
# # 09/14/26
# P1HW2
# Calculator for travel expenses

print("This Program calculates and displays travel expenses")
print(" ")

# User input

budget = int(input("Enter Budget: "))
place = input("Enter your travel destination: ")
gas_money = int(input("How much do you think you will spend on gas? "))
accom_hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))
print(" ")

# Calculations

print("--------Travel Expenses--------")
print("Location: " + place)
print("Initial Budget: " + str(budget))
print(" ")
print("Fuel: " + str(gas_money))
print("Accomodation: " + str(accom_hotel))
print("Food: " + str(food))
print(" ")
print("Remaining Balance: " + str(budget - gas_money - accom_hotel - food))