

* Inside of each folder I have just created, I have added the following:

  * A new file called `main.py`. This is the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files I used, with the correct path for my csv file, and the results from my analysis.



## PyBank


* In this challenge, I was tasked with creating a Python script for analyzing the financial records of my company. I was given a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* I created a Python script that analyzed the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculated the changes in "Profit/Losses" over the entire period, and found the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in profits (date and amount) over the entire period

* My analysis is as follows:

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  

## PyPoll



* In this challenge, I was tasked with helping a small, rural town modernize its vote counting process.

* I was given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. My task was to create a Python script that analyzed the votes and calculated each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* My results were as follows:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, your final script should both print the analysis to the terminal and export a text file with the results.