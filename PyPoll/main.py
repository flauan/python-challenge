#----------------------------------------------------------------------
# Poll Results Summary (PyPoll)
# Author: Fervis Lauan
#----------------------------------------------------------------------
# Modification History:
#
#----------------------------------------------------------------------

import os
import csv

total_votes=0
filenum=0

candidate_dict={}

# Loops through 2 input files
# Modify range for the number of file
# to process

for x in range(2):
    filenum+=1
    print("Processing file election_data_"+str(filenum)+".csv")
    csvpath = os.path.join('data', 'election_data_'+str(filenum)+'.csv')
    line_ctr=0
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:

            if line_ctr>0:
                total_votes+=1            
                found=0
                for key, val in candidate_dict.items():                                
                    if key==row[2]:
                        found=1
                        break
                if found==1:
                    candidate_dict[row[2]]=candidate_dict[row[2]]+1
                else:
                    candidate_dict[row[2]]=1
                        
                line_ctr+=1
            else:
                line_ctr+=1
            
pct_vote=0.00
top_vote=0

print("")
print("Election Results")
print("-------------------------------")
print("Total Votes: "+str(total_votes))
print("-------------------------------")
for key, val in candidate_dict.items():     
    pct_votes=float("{0:.2f}".format((val/total_votes)*100))
    print(key+": "+str(pct_votes)+"% ("+str(val)+")")

    if val>top_vote:
        winner=key
        top_vote=val
    elif val==top_vote:
        winner=winner+" & "+key
print("-------------------------------")
print("Winner: "+winner)
print("-------------------------------")

pct_vote=0.00
top_vote=0
outfile=open("./data/PyPoll_Output.txt","w")
outfile.write("Election Results\n")
outfile.write("-------------------------------\n")
outfile.write("Total Votes: "+str(total_votes)+"\n")
outfile.write("-------------------------------\n")
for key, val in candidate_dict.items():     
    pct_votes=float("{0:.2f}".format((val/total_votes)*100)+"\n")
    outfile.write(key+": "+str(pct_votes)+"% ("+str(val)+")\n")

    if val>top_vote:
        winner=key
        top_vote=val
    elif val==top_vote:
        winner=winner+" & "+key


outfile.write("-------------------------------\n")
outfile.write("Winner: "+winner+"\n")
outfile.write("-------------------------------\n")
outfile.close()
