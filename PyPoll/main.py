# This is for PyPoll
import pandas as pd

election = "election_data.csv"

election_pd = pd.read_csv(election)

votes = len(election_pd.index)
correy = len(election_pd[election_pd["Candidate"] == "Correy"])
khan = len(election_pd[election_pd["Candidate"] == "Khan"])
li = len(election_pd[election_pd["Candidate"] == "Li"])
otooley = len(election_pd[election_pd["Candidate"] == "O'Tooley"])
winner = election_pd["Candidate"].value_counts().idxmax()

print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(votes)}")
print("-------------------------")
print(f"Khan:", format(khan/votes, '.3%'), "(",str(khan),")")
print(f"Correy:", format(correy/votes, '.3%'), "(",str(correy),")")
print(f"Li:", format(li/votes, '.3%'), "(",str(li),")")
print(f"O'Tooley:", format(otooley/votes, '.3%'), "(",str(otooley),")")
print("-------------------------")
print(f"Winner: {str(winner)}")
print("-------------------------")

with open("PyPoll.txt", "a") as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print(f"Total Votes: {str(votes)}", file=f)
    print("-------------------------", file=f)
    print(f"Khan:", format(khan/votes, '.3%'), "(",str(khan),")", file=f)
    print(f"Correy:", format(correy/votes, '.3%'), "(",str(correy),")", file=f)
    print(f"Li:", format(li/votes, '.3%'), "(",str(li),")", file=f)
    print(f"O'Tooley:", format(otooley/votes, '.3%'), "(",str(otooley),")", file=f)
    print("-------------------------", file=f)
    print(f"Winner: {str(winner)}", file=f)
    print("-------------------------", file=f)
