import os
import csv

#declare variables
total_votes = 0
candidates = {}


#Specify file_path to read in the csv
election_csv = os.path.join("Resources", "election_data.csv")

# Open csv
with open(election_csv) as csvfile:
#Check
#print(election_csv)


    # csv reader with delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    #Check path works and read work
    #print(csvreader)

    #Exclude header from the count
    csv_header = next(csvreader)
    #print(csv_header)

    for row in csvreader:

        #add 1 to votecount for the first row = 0.
        total_votes = total_votes + 1
       
       #set variable to point to row 2 for name of candidates
        candidate = row[2]
       
       #add candidates in dictionary
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1

    #check contents of candidates
    #print(candidates)

        report =[
            'Election Results',
            '--------------------',
            f'Total Votes: {total_votes}',
            '--------------------',
        ]

#Percentage of votes for each candidate
for candidate, vote_count in candidates.items():
    #round to 3 digits
    percentage = round(vote_count / total_votes*100,3)
    #count votes and percentage
    candidates[candidate] = {'votes': vote_count, 'percentage':percentage}
    #show results of each candidate
    report.append(f'{candidate}: {percentage}% ({vote_count})')

winner = max(candidates,key=lambda x: candidates[x]['votes'])

report = report + [
    '--------------------',
    f'Winner: {winner}',
    '--------------------'
]


#print election results
for election_results in report:
    print(election_results)


#save to file
save_path = ("analysis")

name_of_file = 'Election_Analysis.txt'

path_file = os.path.join(save_path, name_of_file)

with open(path_file, 'w') as txtfile:
    txtfile.write('\n'.join(report))  
