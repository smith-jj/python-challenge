import os 
import csv
import pandas as pd 
import numpy as np
import sys

# Load File
poll = "Resources/election_data.csv"

# Read File
poll_df = pd.read_csv(poll)
poll_df.head()

# Clean Columns
poll_df.columns = ['Voter_ID', 'County', 'Candidate']

# Total votes
total_votes = poll_df['Candidate'].count()
print("Total Votes:", total_votes)

# List of Candiates with votes
List = poll_df.groupby(['Candidate']).groups.keys()
print(List)

# Total Votes For Correy
CorreyVotes = len(poll_df.groupby(['Candidate']).groups['Correy'])

# Correy Percent
percent_CorreyVotes = CorreyVotes / total_votes * 100
print("Correy:", CorreyVotes, round(percent_CorreyVotes))

# Total Votes For Khan
KhanVotes = len(poll_df.groupby(['Candidate']).groups['Khan'])

#Khan Percent
percent_KhanVotes = KhanVotes / total_votes * 100
print("Khan:", KhanVotes, round(percent_KhanVotes))

# Total Votes For Li
LiVotes = len(poll_df.groupby(['Candidate']).groups['Li'])

# Li Percent
percent_LiVotes = LiVotes / total_votes * 100
print("Li:", LiVotes, round(percent_LiVotes))

# Total Votes For O'Tooley
OTooleyVotes = len(poll_df.groupby(['Candidate']).groups["O'Tooley"])

# Percent O'Tooley
percent_OTooleyVotes = OTooleyVotes / total_votes * 100
print("O'Tooley:", OTooleyVotes, round(percent_OTooleyVotes))

# The winner of the election based on popular vote. (Answer: Winner: Khan)
print("Winner: Khan")

f = open('PyPoll_Solvedwithprint.py', 'a')
f.write('PyPoll_Solvedwithprint.txt')
f.close()
