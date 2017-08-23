#----------------------------------------------------------------------
# Converter and File Export (PyBoss)
# Author: Fervis Lauan
#----------------------------------------------------------------------
# Modification History:
#
#----------------------------------------------------------------------

import os
import csv

filenum=0

emp_id=["Emp ID"]
emp_fname=["First Name"]	
emp_lname=["Last Name"]	
emp_dob=["DOB"]
emp_ssn=["SSN"]
emp_state=["State"]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

import datetime

# Loops through and combine the 2 input 
# files. Modify range base on the number
# of files to process

for x in range(2):
    filenum+=1
    print("Processing file employee_data"+str(filenum)+".csv")
    csvpath = os.path.join('data', 'employee_data'+str(filenum)+'.csv')
    line_ctr=0
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:

            if line_ctr>0:
                strpos=row[1].index(' ')                
                fname=row[1][0:strpos]
                lname=row[1][strpos+1:]
                emp_id.append(row[0])                
                emp_fname.append(fname)
                emp_lname.append(lname)

                emp_dob.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%d/%m/%Y'))
                emp_ssn.append("***-**-"+row[3][7:])
                emp_state.append(us_state_abbrev[row[4]])

                line_ctr+=1
            else:
                line_ctr+=1



lst=zip(emp_id,emp_fname,emp_lname,emp_dob,emp_ssn,emp_state)

with open("./data/PyBoss.csv", "w") as output:
  writer = csv.writer(output, lineterminator='\n')
  for line in lst:
      writer.writerow(line)

print("Output file created: PyBoss.csv")