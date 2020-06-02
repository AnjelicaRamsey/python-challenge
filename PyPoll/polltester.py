# import dependancies
import os
import csv

# Initialize variables
total_votes = 0
votes = {}
vote_percentage = {}
candidate = ""
# Read information from csv
# csvpath = os.path.join('Resources','electiontest.csv')

with open("PyPoll/Resources/election_data.csv") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Loop calculating total votes
    for row in csvreader:
        # votes = row [0]
        candidate = row[2]
        total_votes += 1

        if candidate not in votes:
             votes[candidate] = 1
        else:
             votes[candidate] = votes[candidate] + 1

    # Calculate vote percentage (part/whole)*100
    # Notes:float is decimal/fractional
for candidate in votes:
    candidate_votes = votes[candidate]
    can_percent = (float(candidate_votes)/float(total_votes))*100 
    # dictionary
    print(f'{candidate} has {can_percent}')

# print final results 
# print(votes)
print("Election Results")
print()
print("Total Votes:", total_votes)
print()
print(f"(votes)")




# Export the results to text file
Final= open('PyPollFinal.txt', 'w')
Final.write("Total votes:{}\n".format(total_votes)) 
for key in votes.keys():  
    Final.write(key)
    Final.write(" votes:{}\n".format(votes[key]))
Final.close()


