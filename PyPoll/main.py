import os
import csv
import collections as ct

csvpath = os.path.join("..", "Resources", "election_data.csv")

with open(csvpath, newline='') as poll:
    csvreader = csv.reader(poll, delimiter=",")
    votes = ct.Counter()
    csv_header = next(csvreader)

    # Set variable for Columns
    candidate = []
    votes = []

    for row in poll:
        candidate.append(row[2])
        # The total number of votes cast (answer: Total Votes: 3521001)
        votes_total = len(candidate)
        print("Total Votes:", cotes_total)

        # A complete list of candidates who received votes
        with open(poll) as f:
            votes = ct.Counter()
            reader = csv.reader(f)
            next(reader)
            for line in reader:
                candidate = line[-1]
                votes[candidate] += 1
                print(votes)
                print(votes.most_common(1))
  # The percentage of votes each candidate won
# see other solved doc 
  # The total number of votes each candidate won
# See other solved doc 
  # The winner of the election based on popular vote.
#see other solved doc 

# Error : 
--------------------------------------------------------------------------
TypeError                                 Traceback(most recent call last)
<ipython-input-20-451614b89e95 > in < module >
21
22         # A complete list of candidates who received votes
-- -> 23 with open(poll) as f:
     24             votes = ct.Counter()
     25             reader = csv.reader(f)

TypeError: expected str, bytes or os.PathLike object, not _io.TextIOWrapper

# Answer
#    Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
-------------------------
# Winner: Khan
-------------------------
# had trouble figuring out
