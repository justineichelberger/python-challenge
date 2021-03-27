# import modules
import os
import csv

# open text file to write results
analysis_path = os.path.join("analysis", "financial_analysis.txt")
f = open(analysis_path, "w")

# print header to terminal
print("Financial Analysis")
print("---------------------------------------------------")
# write header to text file
print("Financial Analysis", file=f)
print("---------------------------------------------------", file=f)

# open source file
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    budget_data = csvreader
    
    # store header in variable "header"
    header = next(budget_data)

    # split date and profit columns into separate lists
    budget_data_month_list = []
    budget_data_profit_list = []
    for row in budget_data:
        budget_data_month_list.append(row[0]) 
        budget_data_profit_list.append(row[1])

    # print next row to terminal
    print(f"Total Months: {len(budget_data_month_list)}")
    # write next row to text file
    print(f"Total Months: {len(budget_data_month_list)}", file=f)

    # find sum of profit column
    total_profits = 0
    for profit in budget_data_profit_list:
        total_profits += int(profit)

    # print next row to terminal
    print(f"Total: ${total_profits}")
    # write next row to text file
    print(f"Total: ${total_profits}", file=f)

    # generate list for profit fluctuation month-to-month
    profit_delta_list = [0]
    length = int(len(budget_data_profit_list))
    for profit in range(1,length):
        profit_delta_list.append(int(budget_data_profit_list[profit]) - int(budget_data_profit_list[profit-1])) 

    # calculate average profit fluctuation
    total_profit_swing = 0
    average_profit_swing = 0
    for profit_delta in profit_delta_list:
        total_profit_swing += int(profit_delta)
    average_profit_swing = total_profit_swing / int(length-1)

    # print next row to terminal
    print(f"Average Change: ${round(average_profit_swing, 2)}")
    # write next row to text file
    print(f"Average Change: ${round(average_profit_swing, 2)}", file=f)

    # find date and amount of greatest sequential profit increase and decrease
    greatest_decrease = 0
    greatest_increase = 0
    max_increase_index = 0
    max_decrease_index = 0
    for profit_delta_min_max in range(1, length-1):
        if profit_delta_list[profit_delta_min_max] > greatest_increase:
            greatest_increase = int(profit_delta_list[profit_delta_min_max])
            max_increase_index = int(profit_delta_min_max)
        if profit_delta_list[profit_delta_min_max] < greatest_decrease:
            greatest_decrease = int(profit_delta_list[profit_delta_min_max])
            max_decrease_index = int(profit_delta_min_max)
          
# print next rows to terminal
print(f"Greatest Increase in Profits: {budget_data_month_list[max_increase_index]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {budget_data_month_list[max_decrease_index]} (${greatest_decrease})")
# write next rows to text file
print(f"Greatest Increase in Profits: {budget_data_month_list[max_increase_index]} (${greatest_increase})", file=f)
print(f"Greatest Decrease in Profits: {budget_data_month_list[max_decrease_index]} (${greatest_decrease})", file=f)

# stop writing to text file
f.close()

# archive resource with additional information from analysis process appended by creating "updated_budget_data.csv"
header.append('Profit Fluctuation')
cleaned_csv = zip(budget_data_month_list, budget_data_profit_list, profit_delta_list)
output_file = os.path.join("Resources", "updated_budget_data.csv")
with open(output_file, 'w', newline='') as new_file:
    writer = csv.writer(new_file, delimiter = ',')
    writer.writerow(header)
    writer.writerows(cleaned_csv)