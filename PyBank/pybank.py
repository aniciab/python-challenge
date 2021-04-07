import os
import csv
#Find file
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
pybank_path = os.path.join(dir_path, 'Resources')
output_path = os.path.join(dir_path, 'Analysis', "budget_analysis.txt")

print(pybank_path)
print(type(pybank_path))
os.chdir(pybank_path)
#Read file
total_months = 1
total_profit = 0
month_change = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",0] 
with open('budget_data.csv', 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    #total_months += 1
    total_profit += int(first_row[1])
    prev_profit = int(first_row[1])
    
    for row in csvreader:
       # Track the total
       total_months += 1
       total_profit += int(row[1])
       net_change = int(row[1])-prev_profit
       prev_profit = int(row[1])
       net_change_list += [net_change]
       #month_change += int(row[0])
       if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0] #month
            greatest_increase[1] = net_change #profit
       if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change     

avg_profit = sum (net_change_list)/ len(net_change_list)
output = (
    f"Financial Analysis\n"
    f"--------\n"
    f"Total Months: {total_months}\n"
    f"Total:$ {total_profit}\n" 
    f"Average Change: {avg_profit}\n"
    f"Greatest Increase: {greatest_increase}\n"
    f"Greatest Decrease: {greatest_decrease}\n"
)
print(output)
with open(output_path,'w')as txt_file:
    txt_file.write(output)    

        
