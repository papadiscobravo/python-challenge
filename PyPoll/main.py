import os
import csv

#Which challenge is this?
challenge = "PyPoll"
sourceFilepath = os.path.join("Resources", "election_data.csv")
destinationFilepath = os.path.join("analysis", "analysis.txt")

print("\n\n\nThis is the " + challenge + " python challenge. ")
print("This machine's processor is currently at work analyzing election results.")
# Verify the script can read from the filepath stored in sourceFile.
# <----(This is based on code from the 2nd night of Python, activity 5.)
# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(sourceFilepath, 'r') as text:

    # printing useful for debugging (pufd)
    # This stores a reference to a file stream
    # print(text)

    # Store all of the text inside a variable called "allData"
    allData = text.read()

    # pufd
    # Print the contents of the text file--this one's big.
    # print(lines)
# ---->

# The challenge continues. Calculate the total number of votes cast in the dataset.
# There are at least two ways to count:
lines = len(open(sourceFilepath).readlines(   ))
# counting the rows in the document and subtracting one from the total for the header,
# which is really an expression of how many records there are...
totalRecords = lines-1
progressIncrement = 0
progressIncrement = round( totalRecords / 10 , 0)
# pufd
# print(progressIncrement)

# ...or starting a tally at zero and adding one for each vote:
totalVotes = 0

# At a glance, there appear to be four candidates:
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0
# This is dangerous because it misses write-in votes,
# but it will let me test scripting so far,
# and then circle back to figuring out how to enumerate all candidates.
# After all the for-loop tallying, each candidate will need a percentage:
KhanVotePct = 0
CorreyVotePct = 0
LiVotePct = 0
OTooleyVotePct = 0

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


# This is based in part on the Netflix class exercise:
# Open the CSV
with open(sourceFilepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through adding this month's profit or loss to the running total:
    for row in csvreader:
            thisVote = (row)
            # PUfD
            # print(thisVote)
            # print(thisVote[0])
            if thisRow > 0:
                thisCandidate = str(thisVote [2])
                totalVotes += 1

                if thisCandidate == "Khan":
                    KhanVotes += 1
                if thisCandidate == "Correy":
                    CorreyVotes += 1
                if thisCandidate == "Li":
                    LiVotes += 1
                if thisCandidate == "O'Tooley":
                    OTooleyVotes += 1
                if thisRow % progressIncrement == 0:
                    print(f"{round(thisRow / totalRecords * 100,0)}%")
                if thisRow == totalRecords:
                    print("complete")
                
            # pufd
            # print(row)
            # print(thisCandidate)
            # print(type(thisCandidate))
            # print(f"Khan: {KhanVotes}"")
            # print(f"Correy: {CorreyVotes}"")
            # print(f"Li: {LiVotes}"")
            # print(f"O'Tooley: {OTooleyVotes}"")
            thisRow += 1


# Calculate the percent of total votes won by each candidate
KhanVotePct = round( KhanVotes / totalVotes * 100 , 1)
CorreyVotePct = round( CorreyVotes / totalVotes * 100, 1)
LiVotePct = round( LiVotes / totalVotes * 100, 1)
OTooleyVotePct = round(OTooleyVotes / totalVotes * 100, 1)


# read each candidate's name and vote total into a dictionary
allCandidates = {
    KhanVotes: "Khan",
    CorreyVotes: "Correy",
    LiVotes: "Li",
    OTooleyVotes: "O'Tooley"
    }
# pufd
# print(allCandidates)

# Calculate the percent of total votes won by each candidate
mainCandidateVotes = 0
mainCandidateVotes = KhanVotes + CorreyVotes + LiVotes + OTooleyVotes

winnerVotes = max(KhanVotes, CorreyVotes, LiVotes, OTooleyVotes)
# pufd
# print(f"The winner had {winnerVotes} votes.")

# find winnerVotes as a value in the dictionary allCandidates
# and refer to the key that has that value
winner = allCandidates[winnerVotes]

# print to screen...
print("\n\n\n\n\n\nElection Results")
print("---------------------------------------------")
print(f"Records: {totalRecords}")
print(f"Total votes: {totalVotes}")
print("---------------------------------------------")
print(f"Khan: {KhanVotes} votes ({   KhanVotePct   }%)")
print(f"Correy: {CorreyVotes} votes ({    CorreyVotePct   }%)")
print(f"Li: {LiVotes} votes ({     LiVotePct    }%)")
print(f"O'Tooley: {OTooleyVotes} votes ({      OTooleyVotePct    }%)")
print("---------------------------------------------")
print(f"The candidates listed above won \n{mainCandidateVotes} votes ({round(mainCandidateVotes/totalVotes*100)}% of votes).")
print(f"Winner: {winner}")
print("---------------------------------------------")
print(f"For questions about this script")
print(f"email Paul Bernhardt papadiscobravo@gmail.com\n\n\n")

# ...and write to an external file.
# Open the file using the "append" argument:
f = open(destinationFilepath, "a")

# row 1: title
f.write("\nElection Results")

# row 2: underline
f.write("\n---------------------------------------------")

# row 3: records
f.write(f"\nRecords: {totalRecords}")

# row 4: votes
f.write(f"\nTotal votes: {totalVotes}")

# row 5: 
f.write(f"\nKhan: {KhanVotes} votes ({ KhanVotePct }%)")

# row 6: 
f.write(f"\nCorrey: {CorreyVotes} votes ({ CorreyVotePct }%)")

# row 7: 
f.write(f"\nLi: {LiVotes} votes ({  LiVotePct }%)")

# row 8: 
f.write(f"\nO'Tooley: {OTooleyVotes} votes ({ OTooleyVotePct }%)")

# row 9: underline
f.write("\n---------------------------------------------")

# row 10: underline
f.write(f"\nThe candidates listed above won \n{mainCandidateVotes} votes ({round(mainCandidateVotes/totalVotes*100)}% of votes).\n")

# row 11: underline
f.write(f"Winner: {winner}")

# row 12: underline
f.write("\n---------------------------------------------")

# row 13: signature
f.write("\n\nFor questions about this script")

# row 14: signature
f.write("\nemail Paul Bernhardt papadiscobravo@gmail.com\n\n")

# -------->

