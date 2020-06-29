import os
import csv
import sys

# create an output txt file 
original_stdout = sys.stdout 

with open('output.txt', 'w') as f:
    sys.stdout = f
    
    csvpath = os.path.join("Resources","election_data.csv")

    print ("Election Results")
    print ("_________________")

    with open (csvpath, newline= "") as csvfile:
        csvreader = csv.reader (csvfile,delimiter=",")
        csvheader = next(csvreader)

    # find total votes cast
        total_votes = []
        candidate_list = []
        for row in csvreader:
            total_votes.append(int(row[0]))
            candidate_list.append(str(row[2]))
        print(" ")
        print("Total Votes: " + str(len(total_votes)))
        print("__________________")

    # list of candidates
    def unique_candidates(candidate_list): 
        unique_list = [] 
        for x in candidate_list: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
        return unique_list

    ucan = unique_candidates(candidate_list) 

    # find total number of votes each candidate won and find winner
        
    khan_count = 0  
    correy_count = 0 
    li_count = 0 
    tooley_count = 0
    winner = ""
    highest = 0 

    for x in ucan:
        if x == "Khan":
            khan_count = int(candidate_list.count("Khan"))
            if khan_count > highest:
                winner = x
                highest = khan_count
        elif x == "Correy":
            correy_count = int(candidate_list.count("Correy"))
            if correy_count > highest: 
                winner = x 
                highest = correy_count
        elif x == "Li":
            li_count = int(candidate_list.count("Li"))
            if li_count > highest:
                winner = x 
                highest = li_count
        elif x == "O'Tooley":
            tooley_count = int(candidate_list.count("O'Tooley"))  
            if tooley_count > highest: 
                winner = x 
                highest = tooley_count

    # find percentage of votes each candidate won
    khan_percent = khan_count / (len(total_votes)) * 100
    correy_percent = correy_count / (len(total_votes)) * 100
    li_percent = li_count / (len(total_votes)) * 100
    tooley_percent = tooley_count / (len(total_votes)) * 100

    # organize 
    print("  ")
    result1 = ucan[0] + ": " + format(khan_percent,'.3f') + "%" + " (" + str(khan_count) + ")"
    result2 = ucan[1] + ": " + format(correy_percent,'.3f') + "%" + " (" + str(correy_count) + ")"
    result3 = ucan[2] + ": " + format(li_percent,'.3f') + "%" + " (" + str(li_count) + ")"
    result4 = ucan[3] + ": " + format(tooley_percent,'.3f') + "%" + " (" + str(tooley_count) + ")"

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print("__________________")

    # print winner 

    print("Winner: " + winner)
    print("__________________")

# reset sys.stdout
    sys.stdout = original_stdout

# print to the terminal
with open('output.txt', 'r') as f:
    print(f.read())
