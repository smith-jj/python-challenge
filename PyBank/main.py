# Create Imports
import os
import csv
import sys

# Load File
csvpath = os.path.join("..", "python-challenge", "Resources", "budget_data.csv")

# Open & Read CSV File
with open(csvpath, newline="") as csvfile:
    budget = list(csv.reader(csvfile, delimiter=","))

    # Set variable for Columns
    Dates = []
    ProfitsLosses = []
    pl_changes = []

    #append Dates and ProfitsLosses
    for row in budget:
        Dates.append(row[0])
        ProfitsLosses.append(row[1])

    for i in range(1, len(ProfitsLosses)):
        # Find the change in Profits/Losses from each row and add to the the list
        pl_changes.append(float(ProfitsLosses[i] - ProfitsLosses[i-1]))
        # Find the pl_change of Profits/Losses from the change.append
        avg_pl_change = sum(pl_changes) / len(pl_changes)
        # The greatest increase in profits print as str()
        GreatestProfits = max(pl_changes)
        # The greatest decrease in losses print as str()
        GreatestLosses = min(pl_changes)
        # locate GreatestProfits (GP) date
        GP_Date = str(date[pl_changes.index(max(pl_changes))])
        # Locate GreatestLosses (GL) date
        GL_Date = str(date[pl_changes.index(min(pl_changes))])

# Print Statements
print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", len(Dates))
print("Net Total: $", sum(ProfitsLosses))
print("Average Change: $", (avg_pl_change))
print("Greatest Increase: ", GP_Date, "$", str(GreatestProfits))
print("Greatest Decrease: ", GL_Date, "$", str(GreatestLosses))




