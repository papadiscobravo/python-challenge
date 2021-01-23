import os
import csv

#Which challenge is this?
challenge = "PyBank"
# sourceFilepath = "Resources/budget_data.csv" would work on a Mac but...
sourceFilepath = os.path.join("Resources", "budget_data.csv")
# is ecumenical.
# Same with destinationFilepath = "analysis/analysis.txt" as compared to
destinationFilepath = os.path.join("analysis", "analysis.txt")

print("\n\n\nThis is the " + challenge + " python challenge.\n")
# The challenge indicates to verify the script can read from the filepath stored in sourceFile.
# <----(This is based on code from the 2nd night of Python, activity 5.)
# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(sourceFilepath, 'r') as text:

    # This stores a reference to a file stream
    # print(text)

    # Store all of the text inside a variable called "allData"
    allData = text.read()

    # Printing Useful for Debugging (PUfD)
    # Print the contents of the text file
    # print(lines)
# ---->

# The challenge continues. Calculate the total number of months included in the dataset:
lines = len(open(sourceFilepath).readlines(   ))
totalMonths = lines-1

# Calculate the net total amount of "Profit/Losses" over the entire period.
# I'll do this as a running total:
# This creates a variable to temporarily store this month's profit and loss:
thisMonthProfitLoss = 0

# This is the running total of profits and losses:
netProfitLoss = 0

# This creates a variable called line, in case I need to tell something to
# start not at the header but at the second line of text: 
line = 2

# This creates a variable called row, in case I need to tell something to
# start not at the header but at the second row of csv: 
row = 2

# This creates a variable called row to test for the header (row 0)
# and not try to run a calcualation on it,
# and to increment what row of the csv the for-loop is on.  
thisRow = 0

# This stores the highest monthly profit so far as the for-loop goes through the csv:
recordProfit = 0

# This stores the highest monthly loss so far as the for-loop goes through the csv:
recordLoss = 0

# This is based in part on the Netflix class exercise:
# Open the CSV
with open(sourceFilepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through adding this month's profit or loss to the running total:
    for row in csvreader:
            thisMonthData = (row)
            # PUfD
            # print(thisMonthData)
            # print(thisMonthData[0])
            if thisRow > 0:
                thisMonthProfitLoss = int(thisMonthData [1])
                netProfitLoss += thisMonthProfitLoss
                if thisMonthProfitLoss > recordProfit:
                    recordProfit = thisMonthProfitLoss
                if thisMonthProfitLoss < recordLoss:
                    recordLoss = thisMonthProfitLoss
            # PUfD
            # print(row)
            # print(thisMonthProfitLoss)
            # print(type(thisMonthProfitLoss))
            # print(recordLoss)
            # print(recordProfit)
            thisRow += 1


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes:
avgMonthlyChg = round(netProfitLoss / totalMonths,2)

# print to screen...
print("Analysis")
print("---------------------------------------------")
print(f"Total months: {totalMonths}")
print(f"Net total amount of profits/losses: ${netProfitLoss}")
print(f"Average monthly change: ${avgMonthlyChg}")
print(f"Greatest monthly profit increase: ${recordProfit}")
print(f"Greatest monthly profit decrease: ${recordLoss}\n")
print(f"For questions about this script")
print(f"email Paul Bernhardt at papadiscobravo@gmail.com\n\n\n")

# ...and write to an external file.
# Open the file using the "append" argument:
f = open(destinationFilepath, "a")

# row 1: title
f.write("Analysis")

# row 2: underline
f.write("\n---------------------------------------------")

# row 3: count
f.write("\nTotal months: " + str(totalMonths))

# row 4: total
f.write("\nNet total amount of profits/losses: $" + str(netProfitLoss))

# row 5: average
f.write("\nAverage monthly change: $" + str(avgMonthlyChg))

# row 6: record profit
f.write("\nGreatest monthly profit increase: $" + str(recordProfit))

# row 7: record loss
f.write("\nGreatest monthly profit decrease: $" + str(recordLoss))

# row 8: signature
f.write("\n\nFor questions about this script,")

# row 9: signature
f.write("\nemail Paul Bernhardt at papadiscobravo@gmail.com\n\n")

# -------->

