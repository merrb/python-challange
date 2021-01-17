import os
import csv

#path to folder
path = "03-Python_02-Homework_Instructions_PyPoll_Resources_election_data.csv"


#varibles
votes = [0]
candidates = []
precentage_votes = []
candidates_total_votes = []
winner = []

#csvfile
with open(path) as csvfile:

    #csv reader specifies delimter and varible that holds data
    csvreader = csv.reader(csvfile)

    #header row first
    csvheader = next(csvreader)
    
    #python list
    data_list = [row for row in csvreader]

    #total number of candidates in the data set
    num_votes = (len(data_list))

for row in data_list:
        #total number of votes
        #num_votes = num_votes
        #Candidates
        candidate = row[2]
        #Votes per candidate
        if candidate in candidates:
           candidate_index = candidates.index(candidate)
           votes[candidate_index] = votes[candidate_index] + 1
           #print(candidates)
        else:
           candidates.append(candidate)
          
           #print(candidates)           
           votes.append(1)
votes.pop(len(candidates))

print(votes)
for count in range(len(candidates)):
    precentage_votes.append(round(votes[count]/num_votes*100,3))
    #precentage_votes(round(votes.count(candidate)/num_votes*100,3))
    #percentages.append(vote_percentage)
    #if vote_count[count] > most_votes:
        #print(most_votes)
        #most_votes_index = count

#winner = candidates[max_index]

#variable
highvotes = max(votes)

highvotes_index = votes.index(highvotes)

winner = candidates[highvotes_index]


#percentages = [round (i,2) for i in percentages]


    
        #if candidate_total_votes > max_votes:
            #max_votes = candidate_total_votes[x]
            #max_index = x

#winner = candidates[max_index]

  
         #candidate_total_votes.append(row)
           

        #percent = round(int(row[2]) / int(row[3]), 2)

        #print(votes.append(row[0]))
        #print(list.count(data_list))
        #print(string.count(voterid))

        #print(row)
        #print(row.count(candidates))
        #percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)

        #total votes
        #candidate_total_votes

#total number of candidates
     #candidates


print(f'votes: {num_votes}')
print(f'candidates: {candidates}')
print(f'precentage_votes: {precentage_votes}')
print(f'winner: {winner}')


