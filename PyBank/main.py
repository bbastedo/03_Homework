# PyBank Homework
# Author: Ben Bastedo

# import dependencies
import os
import csv

# Open CSV file from Resources folder
csvpath = os.path.join("Resources","budget_data.csv")

# Initialize variables as int, doubles, and strings
totalMonths = 0
totalAmount = 0 
maxIncrease = 0 
maxDecrease = 0
tempincrease = 0.00
tempdecrease = 0.00 
tempincreasemonth = ""
tempdecreasemonth = ""
maxIncreasemonth = ""
maxDecreasemonth = ""

# Opening CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Storing CSV header row
    csv_header = next(csvreader)
    # For each row in CSV file:
    for row in csvreader:
        # If amount in column 2 is greater than 0, set temporary increase variable = to amount and set temporary increase month variable = to month in column 1
        if float(row[1]) > 0: 
            tempincrease = float(row[1])
            tempincreasemonth = str(row[0])
        # Else If amount in column 2 is less than 0, set temporary decrease variable = to amount and set temporary decrease month variable = to month in column 1
        else:
            tempdecrease = float(row[1])
            tempdecreasemonth = str(row[0])
            # Checking if positive amount is greater than largest increase so far. If so, set the maxIncrease = tempIncrease. Same with maxMonth = tempMonth
            if tempincrease > maxIncrease:
                maxIncrease = tempincrease
                maxIncreasemonth = tempincreasemonth
            # Checking if negative amount is greater than largest decrease so far. If so, set MaxDecrease = tempDecrease. Same with MaxDecreaseMonth = TempDecreaseMonth
            if tempdecrease < maxDecrease:
                maxDecrease = tempdecrease
                maxDecreasemonth = tempincreasemonth
        # Add one to total month counter
        totalMonths = totalMonths + 1
        # Sum up total overall change
        totalAmount = totalAmount + float(row[1])
        
# Print Financial Analysis in terminal
print("--------Financial Analysis----------")        
print(f"Total Months: {totalMonths}")
print(f"Total ${totalAmount}")
print(f"Greatest Increase in Profits: ${maxIncrease} in {maxIncreasemonth}")
print(f"Greatest Decrease in Profits: ${maxDecrease} in {maxDecreasemonth}")

# Create output file and write financial analysis to .txt file
output_file = os.path.join("output", "PyBankResults.txt")
with open(output_file, "w", newline="") as text_file:
    text_file.write("--------Financial Analysis----------\n")
    text_file.write(f"Total Months: {totalMonths}\n")
    text_file.write(f"Total ${totalAmount}\n")
    text_file.write(f"Greatest Increase in Profits: ${maxIncrease} in {maxIncreasemonth}\n")
    text_file.write(f"Greatest Decrease in Profits: ${maxDecrease} in {maxDecreasemonth}\n")
    text_file.write(f"Total Months: {totalMonths}\n")

# reset temporary variables back to 0. 
tempdecrease = 0
tempincrease = 0

