# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables for data output
total_votes = 0
candidates = []
candidate_votes = [0, 0, 0]

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store the header row
    csv_header = next(csvreader)

    #iterate through file to count votes
    for row in csvreader:
        total_votes += 1
        
        # add unique candidates names into a list
        if row[2] not in candidates:
            candidates.append(row[2])
        # add conditionals to count up all the votes
        if row[2] == candidates[0]:
            candidate_votes[0] += 1
        elif row[2] == candidates[1]:
            candidate_votes[1] += 1
        else:
            candidate_votes[2] += 1

# create a function to use the candidate votes to determine the percentages
def percentage(totalvotes,candidate_votes):
    percentages = []
    for votes in candidate_votes:
        percentages.append(round(100*votes/totalvotes, 3))
    return percentages

# run function to get the percentages
percentages = percentage(total_votes, candidate_votes)

# find election winner
index_max = candidate_votes.index(max(candidate_votes))
election_winner = candidates[index_max]

# print all the results
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes))
print('-------------------------')
print(candidates[0] + ': ' + str(percentages[0]) +'% (' + str(candidate_votes[0]) +')')
print(candidates[1] + ': ' + str(percentages[1]) +'% (' + str(candidate_votes[1]) +')')
print(candidates[2] + ': ' + str(percentages[2]) +'% (' + str(candidate_votes[2]) +')')
print('-------------------------')
print('Winner: ' + election_winner)
print('-------------------------')

# Create output file
# Specify the file to write to
output_path = os.path.join("analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write('Total Votes: ' + str(total_votes) + '\n')
    txtfile.write('-------------------------\n')
    txtfile.write(candidates[0] + ': ' + str(percentages[0]) +'% (' + str(candidate_votes[0]) +')\n')
    txtfile.write(candidates[1] + ': ' + str(percentages[1]) +'% (' + str(candidate_votes[1]) +')\n')
    txtfile.write(candidates[2] + ': ' + str(percentages[2]) +'% (' + str(candidate_votes[2]) +')\n')
    txtfile.write('-------------------------\n')
    txtfile.write('Winner: ' + election_winner +'\n')
    txtfile.write('-------------------------\n')