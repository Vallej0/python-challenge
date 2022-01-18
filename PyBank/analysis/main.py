import os
import csv
import pathlib


csvpath = os.path.join(pathlib.Path(__file__).parent.resolve(),"..",'Resources','budget_data.csv')

with open (csvpath) as file:
    reader = csv.reader(file)
    data = list(reader)

dateColumn = []
profitLossColumn = []
changeColumn = []

previousProfitLoss = 0

for row in data[1:]:
    dateColumn.append(row[0])
    profitLossColumn.append(int(row[1]))        # row 1 is second column 

    changeColumn.append(int(row[1])-previousProfitLoss)
    previousProfitLoss = int(row[1])

totalMonths = len(dateColumn)
print(f"Total Months: {totalMonths}")

totalChange = sum(profitLossColumn)
print(f"Total: ${totalChange}")

AverageChange = sum(changeColumn[1:])/len(changeColumn[1:])

greatestProfits = max(changeColumn)           #Calculate the max from the profit loss column
index = changeColumn.index(greatestProfits)  #Find where the greatest ins in the profit loss column (index)
greatestDate = dateColumn[index]

leastProfits = min(changeColumn)              #get the corresponding date ar that index
index = changeColumn.index(leastProfits)  #Find where the greatest ins in the profit loss column (index)
leastDate = dateColumn[index]


print(f"Average Change: ${AverageChange}")
print(f"Greates Increase in Profits:: {greatestDate}, (${greatestProfits})")
print(f"Greatest Decrease in Profits: {leastDate}, (${leastProfits})")

output_path = os.path.join(pathlib.Path(__file__).parent.resolve(), ".", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as out_put_file:
    out_put_file.write(f"Total Months: {totalMonths}\n")   
    out_put_file.write(f"Total: ${totalChange}\n")
    out_put_file.write(f"Average Change: ${AverageChange}\n")
    out_put_file.write(f"Greates Increase in Profits:: {greatestDate}, (${greatestProfits})\n")
    out_put_file.write(f"Greatest Decrease in Profits: {leastDate}, (${leastProfits})\n")
