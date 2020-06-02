# Import Dependencies
import os
import csv

# Initialize variables
total_months = 0
delta_sum = 0
increases = []
decreases = []



# Read information from csv
# csvpath = os.path.join("Py-Challenge/PyBank/Resources/budget_data.csv")
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    # We can only look at the current row within the loop
    for row in csvreader:

        # Add 1 to the total number of months 
        total_months = total_months + 1

        # Total profits
        # print(row) 

        # Average of changes of profits
       
        # delta_sum = (current_profit - previous_profit) + delta_sum
        # If we are in the first row, don't do anything with the delta_sum
        if total_months == 1:
            prev_profit = int(row[1])
        
        # If we are in the second + row, add the difference to the delta_sum
         # {(Feb - Jan)+ (Mar - Feb) + (Apr - Mar)}/ (number of months - 1)
            # calc greatest increase
            # calc greatest decrease 

        else:
            delta_sum = int(row[1]) - prev_profit + delta_sum
            net_change = int(row[1]) - prev_profit 
            if net_change > 0:
                increases.append(net_change)
            else:
                decreases.append(net_change)
            prev_profit = int(row[1])
        
# print to screen
print("average change in profits")
print(delta_sum/(total_months-1))
print()     
print("greatest increase")
print(max(increases))
print()
print("greatest decrease")
print(min(decreases))


# Print to text file 
Final= open('python_challenge/PyBank/a', 'w')
Final.write('File has content.')
Final.close()

