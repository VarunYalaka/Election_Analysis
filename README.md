# Election Analysis

## Overview of Project
Tom is a Colorado board of elections employee. He is looking to automate the election report process using python. If this audit is done successfully with Python, the code will be used to audit not only other congressional districts, but also senatorial districts and local elections. 

#### Script should display: 
* Total number of votes cast
* Total number of votes each candidate received
* The Percentage of votes for each candidate 
* The percentage of votes by county
* Winner based on popular vote 
* Winning vote count and percentage 


## Election results:
----------------------------------------------
* Total Votes: 369,711 
----------------------------------------------
County Votes:

Jefferson: 10.5% (38,855)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

-------------------------------
* Largest County Turnout: Denver
----------------------------------

Candidate Breakdown:

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

---------------------------------------

#### * Winner: Diana DeGette

Winning Vote Count: 272,892

Winning Percentage: 73.8%

---------------------------------------

Using for loop to to get the county from the county dictionary.
 
![Screen Shot 2022-09-12 at 10 53 56 PM](https://user-images.githubusercontent.com/44387918/189824727-743ba440-cd2d-4fdd-9ecc-33f97a6fc971.png) 

Save the winning candidate's name to the text file

![Screen Shot 2022-09-12 at 10 57 54 PM](https://user-images.githubusercontent.com/44387918/189824768-80a42650-8e26-41f6-8e8d-255ac3a6b8e1.png) 
  
## Summary
This code is useful for other elections if the county name in the second column and the candidate name in the third column. Results including winner, winning Vote Count and winning Percentage along with county votes. 

With some modifications - 

1. This script can be used to provide results based on the state and zip code per vote. 
2. Required to add similar to counties summary blocks of scripts for state and zipcode.
3. Another column indicating the age of the voter to know the majority voter's age for reporting purposes.    

