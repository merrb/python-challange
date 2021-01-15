import os
import csv

#path to folder
path = "03-Python_02-Homework_Instructions_PyPoll_Resources_election_data.csv"


#varibles
votes = []
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
        print(votes.append(row[1]))

        #print(row)
        #print(row.count(candidates))
        #percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)

        #total votes
        #candidate_total_votes

#total number of candidates
     #candidates
