
#Pseudo code for election results
# 1. The total umber of votes cast
# 2. Names of candidates who received votes 
# 3. The total number of votes each candidte won
# 4. The percentage of votes each candidate won 
# 5. The winner of election based on the popular vote   

import csv
from email import header 
import os

file_to_load = os.path.join("Election_Analysis/Resources", "election_results.csv")

file_to_save = os.path.join("Resources", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
   
    headers = next(file_reader)
    print(headers)