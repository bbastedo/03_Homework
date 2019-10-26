# PyPoll Homework
# Author: Ben Bastedo

# import dependencies
import os
import csv

# create path to find CSV file to import
csvpath = os.path.join("Resources","election_data.csv")

# initializing variables at 0 as integers
totalVotesCast = 0
KhanTotalVotes = 0
CorreyTotalVotes = 0
LiTotalVotes = 0
OtooleyTotalVotes = 0

# Opening the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# For each row in the CSV file
    for row in csvreader:
        # Adding 1 to the total number of votes as each line is a vote
        totalVotesCast = totalVotesCast + 1
        # If Vote was for Khan, add one to total
        if row[2] == "Khan":
            KhanTotalVotes = KhanTotalVotes + 1
        # If Vote was for Correy, add one to toal
        if row[2] == "Correy":
            CorreyTotalVotes = CorreyTotalVotes + 1
        # If Vote was for Li, add one to total
        if row[2] == "Li":
            LiTotalVotes = LiTotalVotes + 1
        # If Vote was for O'Tooley, add one to total votes
        if row[2] == "O'Tooley":
            OtooleyTotalVotes = OtooleyTotalVotes + 1
    
# Calculating percentages of votes for each candidate and rounded to 3 decimal places.
KhanPercentage = round((KhanTotalVotes/totalVotesCast) * 100,3)
CorreyPercentage = round((CorreyTotalVotes/totalVotesCast) * 100,3)
LiPercentage = round((LiTotalVotes/totalVotesCast) * 100,3)
OtooleyPercentage = round((OtooleyTotalVotes/totalVotesCast) * 100,3)

# Creating dictionary of all votes in order to calculate the popular vote winner
candidates = {'Khan': KhanTotalVotes, 'Correy': CorreyTotalVotes, 'Li': LiTotalVotes, 'O''Tooley': OtooleyTotalVotes}
popular_winner = max(candidates, key=candidates.get)

# Printing out Election results in terminal window
print("--------Election Results----------")
print(f"Total Votes: {totalVotesCast}")
print("----------------------------")
print(f"Khan: {KhanPercentage}% ({KhanTotalVotes})")
print(f"Correy: {CorreyPercentage}% ({CorreyTotalVotes})")
print(f"Li: {LiPercentage}% ({LiTotalVotes})")
print(f"O'Tooley: {OtooleyPercentage}% ({OtooleyTotalVotes})")
print("----------------------------")
print(f"Winner {popular_winner}")
print("----------------------------")

# Creating output file in path ../Output
output_file = os.path.join("Output", "PyPollResults.txt")

# Writes results out for Election in .txt file
with open(output_file, "w", newline="") as text_file:
    text_file.write("-----Election Results-------\n")
    text_file.write(f"Total Votes: {totalVotesCast}\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Khan: {KhanPercentage}% ({KhanTotalVotes})\n")
    text_file.write(f"Correy: {CorreyPercentage}% ({CorreyTotalVotes})\n")
    text_file.write(f"Li: {LiPercentage}% ({LiTotalVotes})\n")
    text_file.write(f"O'Tooley: {OtooleyPercentage}% ({OtooleyTotalVotes})\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Winner {popular_winner}\n")
    text_file.write("----------------------------\n")