import os
import csv

#Set path for file
poll_csv = os.path.join("Resources","election_data.csv")

totalVotes=0
candidates=[]
candVotes=[]
candTally=0
grtstVotes=0 #Keeps track of which candidate has the highest amount of votes
winner=""

#Calculates the candidates' percentage of votes compared to the total
def percent(candVotes, total):
    return (candVotes*100)/total

with open(poll_csv,'r') as poll_in:
    reader=csv.reader(poll_in,delimiter=",")

    #Skip header
    header=next(poll_in)
    
    for row in reader:
        #Tallies the total votes throughout the file
        totalVotes+=1
        #Adds the candidate to the dict if they're not already in there, then tallies their vote
        if row[2] not in candidates: 
            candidates.append(row[2])
            candVotes.append(1)
        else:
            #Goes through the dict to find the candidate that matches the file row, then tallies their vote
            for x in range(len(candidates)):
                if candidates[x]==row[2]:
                    candVotes[x]+=1

#Set path for output
poll_output=os.path.join("analysis","election_analysis.csv")

with open(poll_output, 'w') as pollFile:
    writer = csv.writer(pollFile, delimiter=',')
    writer.writerow(['Election Results'])
    print("Election Results")
    writer.writerow(['--------------------------------------------------------'])
    print("--------------------------------------------------------")
    writer.writerow(['Total Votes: ',str(totalVotes)])
    print("Total Votes: "+str(totalVotes))
    writer.writerow(['--------------------------------------------------------'])
    #Goes through the dict to grab the candidates' names and votes, and tracks who has the greatest amount
    for x in range(len(candidates)):
        writer.writerow([candidates[x],': ','{:.2f}'.format(percent(candVotes[x],totalVotes)),'% (',str(candVotes[x]),')'])
        print(candidates[x]+": "+'{:.2f}'.format(percent(candVotes[x],totalVotes))+"% ("+str(candVotes[x])+")")
        if candVotes[x]>grtstVotes:
            grtstVotes=candVotes[x]
            winner=candidates[x]

    writer.writerow(['--------------------------------------------------------'])
    print("--------------------------------------------------------")
    writer.writerow(['Winner: ',winner])
    print("Winner: "+winner)
    writer.writerow(['--------------------------------------------------------'])
    print("--------------------------------------------------------")

