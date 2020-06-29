import os 
import csv
import sys

# print to the text file 
original_stdout = sys.stdout 

with open('output.txt', 'w') as f:
    sys.stdout = f

    print("Financial Analysis")
    print("___________________")

    csvpath = os.path.join("Resources","budget_data.csv")

    with open (csvpath, newline= "") as csvfile:
        csvreader = csv.reader (csvfile,delimiter=",")
        csvheader = next(csvreader)

# sum of profits/losses
        net_total = []
        total_months = []
        for row in csvreader:
            net_total.append(int(row[1]))
        total_months.append(row[0])

# total months count
        print("Total Months: " + str(len(total_months)))
# net total of profits/losses
        print("Total: " + str(sum(net_total)))

    with open (csvpath, newline= "") as csvfile:
        csvreader = csv.reader (csvfile,delimiter=",")
        csvheader = next(csvreader)

# find average revenue change
    average_change_list = []
    previous_month = 0

    for x in range(len(net_total)):
        if x == 0:
            previous_month = net_total[x]
        else:
            monthly_change = net_total[x] - previous_month
            average_change_list.append(monthly_change)
            previous_month= net_total[x]

    length = len(average_change_list)
    total = sum(average_change_list)
    profit_loss_average = total / length
    print("Average Change: $" + str(round(profit_loss_average,2)))

# find greatest increase and greatest decrease
    with open (csvpath, newline= "") as csvfile:
        csvreader = csv.reader (csvfile,delimiter=",")
        csvheader = next(csvreader)

        change_months = []
        for row in csvreader:
            change_months.append(row[0])
        change_months.remove("Jan-2010")
    greatest_increase = max(average_change_list)
    greatest_decrease = min(average_change_list)

    mydict = dict(zip(change_months, average_change_list))
    for key,value in mydict.items():
        if value == greatest_increase:
            print("Greatest Increase in Profits: " + key,value)
        elif value == greatest_decrease:
            print("Greatest Decrease in Profits: " + key,value)

# reset sys.stdout
    sys.stdout = original_stdout

# print to the terminal
with open('output.txt', 'r') as f:
    print(f.read())
