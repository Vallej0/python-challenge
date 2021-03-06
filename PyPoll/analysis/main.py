import csv
import os
import pathlib


csvpath = os.path.join(pathlib.Path(__file__).parent.resolve(),"..",'Resources','election_data.csv')

with open (csvpath) as file:
    reader = csv.reader(file)
    reader.__next__()    #Skips the first line
    Total_Votes = 0
    candidates = {} #Create an empty dictionary of candidates. Key = Name, Value = votes

    for row in reader:
        #[Voter ID, County, Candidate]
        Total_Votes +=1 

        if row[2] not in candidates:
            # variable[key] = value
            candidates[row[2]] = 0

        candidates[row[2]] += 1

    


print("Election Results")
print("------------------------------------------------")
print(f"Total Votes:{ Total_Votes}")
print("------------------------------------------------")
hihestName = 0
highestVotes = 0
for name, votes in candidates.items():                         # for KEY, VALUE in 
    percent = round(votes/Total_Votes*100,3)
    print(f"{name}: {percent}% ({votes})")
    if votes > highestVotes:
        highestName = name
        highestVotes = votes
print("------------------------------------------------")
print(f"Winner: {highestName}")
print("------------------------------------------------")

output_path = os.path.join(pathlib.Path(__file__).parent.resolve(), ".", "output.txt")

with open(output_path, 'w') as out_put_file:
    out_put_file.write("Election Results\n")
    out_put_file.write("------------------------------------------------\n")
    out_put_file.write(f"Total Votes:{ Total_Votes}\n")
    out_put_file.write("------------------------------------------------\n")
    hihestName = 0
    highestVotes = 0
    for name, votes in candidates.items():                         # for KEY, VALUE in 
        percent = round(votes/Total_Votes*100,3)
        out_put_file.write(f"{name}: {percent}% ({votes})\n")
        if votes > highestVotes:
            highestName = name
            highestVotes = votes
    out_put_file.write("------------------------------------------------\n")
    out_put_file.write(f"Winner: {highestName}\n")
    out_put_file.write("------------------------------------------------\n")