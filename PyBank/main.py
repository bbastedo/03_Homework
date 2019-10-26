import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

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


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        # print(row[1])
        # print(type(row[1]))
        if float(row[1]) > 0: 
            tempincrease = float(row[1])
            tempincreasemonth = str(row[0])
        else:
            tempdecrease = float(row[1])
            tempdecreasemonth = str(row[0])
            if tempincrease > maxIncrease:
                maxIncrease = tempincrease
                maxIncreasemonth = tempincreasemonth
            if tempdecrease < maxDecrease:
                maxDecrease = tempdecrease
                maxDecreasemonth = tempincreasemonth
        totalMonths = totalMonths + 1
        totalAmount = totalAmount + float(row[1])
        
print("--------Financial Analysis----------")        
print(f"Total Months: {totalMonths}")
print(f"Total ${totalAmount}")
print(f"Greatest Increase in Profits: ${maxIncrease} in {maxIncreasemonth}")
print(f"Greatest Decrease in Profits: ${maxDecrease} in {maxDecreasemonth}")

output_file = os.path.join("output", "PyBankResults.txt")
with open(output_file, "w", newline="") as text_file:
    text_file.write("--------Financial Analysis----------\n")
    text_file.write(f"Total Months: {totalMonths}\n")
    text_file.write(f"Total ${totalAmount}\n")
    text_file.write(f"Greatest Increase in Profits: ${maxIncrease} in {maxIncreasemonth}\n")
    text_file.write(f"Greatest Decrease in Profits: ${maxDecrease} in {maxDecreasemonth}\n")
    text_file.write(f"Total Months: {totalMonths}\n")

# with open(output_file, "w", newline="") as datafile:
#     writer = txt.writer(datafile)

#     writer.write("--------Financial Analysis----------")
#     writer.writerow(f"Total Months: {totalMonths}")
#     writer.writerow(f"Total ${totalAmount}")
#     writer.writerow(f"Greatest Increase in Profits: ${maxIncrease} in {maxIncreasemonth}")
#     writer.writerow(f"Greatest Decrease in Profits: ${maxDecrease} in {maxDecreasemonth}")

tempdecrease = 0
tempincrease = 0

