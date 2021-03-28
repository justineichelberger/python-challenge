# import modules
import os
import csv

# open text file to write results
analysis_path = os.path.join("analysis", "election_results.txt")
f = open(analysis_path, "w")

# open source file
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    election_data = csvreader

    # store header in variable "header"
    header = next(election_data)
    #print(header)

    # write header to terminal
    print("Election Results")
    print("-------------------------")
    # write header to text file
    print("Election Results", file=f)
    print("-------------------------", file=f)

    # obtain total votes
    candidate_per_vote_list = []
    for row in election_data:
        candidate_per_vote_list.append(row[2])
    total_votes = len(candidate_per_vote_list)
    
    # write total votes to terminal
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    # write total votes to text file
    print(f"Total Votes: {total_votes}", file=f)
    print("-------------------------", file=f)


    # obtain list of unique candidates
    candidate_list = list(set(candidate_per_vote_list))
    candidate_list_length = len(candidate_list)
    
    # count votes for each candidate
    counted_list = []
    votes_per_candidate = []
    for row in range(candidate_list_length):
        counted = candidate_per_vote_list.count(candidate_list[row])
        counted_list.append(counted)
    votes_dictionary = dict(zip(counted_list, candidate_list))

    # sort vote totals and collate with candidate's name
    counted_list_sorted = sorted(counted_list, reverse=True)
    for row in range(candidate_list_length):
        print(f"{votes_dictionary[counted_list_sorted[row]]}: {round(float((counted_list_sorted[row]/total_votes)*100),3)}00% ({counted_list_sorted[row]})")
        print(f"{votes_dictionary[counted_list_sorted[row]]}: {round(float((counted_list_sorted[row]/total_votes)*100),3)}00% ({counted_list_sorted[row]})", file=f)
    
    # write footer to terminal
    print("-------------------------")
    print(f"Winner: {votes_dictionary[counted_list_sorted[0]]}")
    print("-------------------------")
    # write footer to text file
    print("-------------------------", file=f)
    print(f"Winner: {votes_dictionary[counted_list_sorted[0]]}", file=f)
    print("-------------------------", file=f)