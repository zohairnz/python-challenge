# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Initialize variables for data output
total_months = 0
total_change = 0

# Initialize variables that will be used to store change within the csv file reading
new_profit_loss = 0
old_profit_loss = 0

# Create Lists to store data
delta = []
dates =[]


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store the header row
    csv_header = next(csvreader)

    #iterate through file to count months, add up the total change
    for row in csvreader:
        total_months += 1
        total_change += int(row[1])
        # cycle through dates and store in list
        dates.append(row[0])
        # find change and store in list
        new_profit_loss = int(row[1])
        delta.append(new_profit_loss-old_profit_loss)
        old_profit_loss = new_profit_loss
        
# Compute max of list to find greatest profit increase
greatest_increase = max(delta)
greatest_decrease = min(delta)

# find index of max and min so we can output the date
index_max = delta.index(max(delta))
index_min = delta.index(min(delta))

# store the dates of max and min values
date_max = dates[index_max]
date_min = dates[index_min]

# Compute average of changes by summing the list of delta and dividing by length
# need to remove the first entry of delta since we are not starting from zero
# round to two decimal places as well
delta.pop(0)
average_change = round(sum(delta)/len(delta),2)

# Print analysis results
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_change))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(date_max) + " ($" + str(greatest_increase) +")")
print("Greatest Decrease in Profits: " + str(date_min) + " ($" + str(greatest_decrease) +")")

# Create output file
# Specify the file to write to
output_path = os.path.join("analysis", "results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write("Total Months: " + str(total_months) + "\n")
    txtfile.write("Total: $" + str(total_change) + "\n")
    txtfile.write("Average Change: $" + str(average_change) + "\n")
    txtfile.write("Greatest Increase in Profits: " + str(date_max) + " ($" + str(greatest_increase) +")\n")
    txtfile.write("Greatest Decrease in Profits: " + str(date_min) + " ($" + str(greatest_decrease) +")")
