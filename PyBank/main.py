import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")
#Import csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    #Define the lists
    date=[]
    pl=[]
    pl_change=[]

    #Get Total Months
    for row in csvreader:
        date.append(row[0])
        pl.append(float(row[1]))
    
    total_months=len(date)

    #Get Total PL
    total_pl=sum(pl)
    print(total_pl)

    #Get Average PL Change
    for i in range(1,len(pl)):
        pl_change.append(pl[i]-pl[i-1])
        avg_pl_change=sum(pl_change)/len(pl_change)
    print(avg_pl_change)

    #Get Max and Min PL
    max_pl=max(pl_change)
    print(max_pl)
    
    min_pl=min(pl_change)
    print(min_pl)

    #Get Dates for PL Changes
    max_pl_date =str(date[pl_change.index(max_pl)+1])
    min_pl_date=str(date[pl_change.index(min_pl)+1])
    print(max_pl_date)
    print(min_pl_date)

#Print out results to terminal
print("Financial Analysis")
print("---------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: {total_pl}')
print(f'Average Change: ${round(avg_pl_change,2)}')
print(f'Greatest Increase in Profits: {max_pl_date} (${max_pl})')
print(f'Greatest Decrease in Profits: {min_pl_date} (${min_pl})')

f=open('file.txt', 'w')