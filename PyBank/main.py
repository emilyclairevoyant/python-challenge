import csv
# Initialize variables
total_months = 0
total_profit_losses = 0
changes_in_profit_losses = []
max_profit_increase = 0
max_profit_increase_date = ""
max_profit_decrease = 0
max_profit_decrease_date = ""
previous_profit_loss = None

# Open the CSV file in read mode
with open('PyBank/Resources/budget_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip the header row
    next(csv_reader)
    
    # Loop through the rows in the CSV file to perform the analysis
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])  # Assuming the Profit/Losses column is the second column
        
        # Calculate total number of months
        total_months += 1
        
        # Calculate total Profit/Losses
        total_profit_losses += profit_loss
        
        # Calculate changes in Profit/Losses
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes_in_profit_losses.append(change)
            
            # Check for greatest increase
            if change > max_profit_increase:
                max_profit_increase = change
                max_profit_increase_date = date
            
            # Check for greatest decrease
            if change < max_profit_decrease:
                max_profit_decrease = change
                max_profit_decrease_date = date
        
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_profit_increase_date} (${max_profit_increase})")
print(f"Greatest Decrease in Profits: {max_profit_decrease_date} (${max_profit_decrease})")

# Export the analysis results to a text file
with open('financial_analysis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {max_profit_increase_date} (${max_profit_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {max_profit_decrease_date} (${max_profit_decrease})\n")

print("Analysis results have been exported to financial_analysis.txt.")