# Print a welcome message
print("Welcome to the Tip Calculator!")

# Take the total bill amount from the user
bill = float(input("What was the total bill? $"))

# Take the tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Take the number of people splitting the bill
people = int(input("How many people to split the bill? "))

# Calculate the tip amount
tip_amount = (tip_percentage / 100) * bill

# Calculate the total bill including tip
total_bill = bill + tip_amount

# Calculate how much each person should pay
bill_per_person = total_bill / people

# Display the final amount rounded to 2 decimal places
print(f"Each person should pay ${bill_per_person:.2f}")
