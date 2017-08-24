#----------------------------------------------------------------------
# Revenue Analysis (PyBank)
# Author: Fervis Lauan
#----------------------------------------------------------------------
# Modification History:
#
#----------------------------------------------------------------------

import os
import csv

# Process 1 file
# Modify filenum for the filenumber to process

filenum=1 

tot_rev_chg=0.0
csvpath = os.path.join('data', 'budget_data_'+str(filenum)+".csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    line_ctr=0
    prev_rev=0.00
    prev_rev_change=0.00
    rev_change=0.00
    tot_num_months=0
    tot_amt_rev=0.0      
        
    gti_rev_chg_month=""
    gti_rev_chg_rev=0.00
    gti_rev_chg=0.00
    gtd_rev_chg_month=""
    gtd_rev_chg_rev=0.00
    gtd_rev_chg=0.00

    for row in csvreader:
        print(str(row[0])+"    "+str(row[1])+"     ")

        if line_ctr>0:
            tot_num_months+=1
            tot_amt_rev+=float(row[1])
        
            if line_ctr>1:               
                rev_change=float(row[1])-prev_rev                
                print("Rev Change :"+str(rev_change))
                tot_rev_chg+=rev_change                

                if rev_change>gti_rev_chg:
                    gti_rev_chg_month=row[0]
                    gti_rev_chg_rev=float(row[1])
                    gti_rev_chg=rev_change
                    

                if rev_change<gtd_rev_chg:
                    gtd_rev_chg_month=row[0]
                    gtd_rev_chg_rev=float(row[1])
                    gtd_rev_chg=rev_change                    
                                
            prev_rev=float(row[1])
            
            line_ctr+=1                        
        else:
            line_ctr=1

avg_rev_change=tot_rev_chg/(tot_num_months-1)

print("Final Results: budget_data_"+str(filenum)+".csv")
print("----------------------------------------")
print("Total Months: "+str(tot_num_months)) 
print("Total Revenue: "+str(tot_amt_rev)) 
print("Average Revenue Change: "+str(avg_rev_change)) 
print("Greatest Increase in Revenue: "+gti_rev_chg_month+"  ("+str(gti_rev_chg)+")")
print("Greatest Decrease in Revenue: "+gtd_rev_chg_month+"  ("+str(gtd_rev_chg)+")")

outfile=open("./data/PyBank_Output_"+str(filenum)+".txt","w")
outfile.write("Final Results: budget_data_"+str(filenum)+".csv\n")
outfile.write("----------------------------------------\n")
outfile.write("Total Months: "+str(tot_num_months)+"\n")
outfile.write("Total Revenue: "+str(tot_amt_rev)+"\n")
outfile.write("Average Revenue Change: "+str(avg_rev_change)+"\n")
outfile.write("Greatest Increase in Revenue: "+gti_rev_chg_month+"  ("+str(gti_rev_chg)+")\n")
outfile.write("Greatest Decrease in Revenue: "+gtd_rev_chg_month+"  ("+str(gtd_rev_chg)+")\n")
outfile.close()

