import csv

# Initialize variables
total_votes = 0
candidates = set()
votes_per_candidate = {}
percentage_of_votes = 0
election_winner = ""

# Open the .csv file in read mode
with open('PyPoll/Resources/election_data.csv', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()[1:]

# Count the total number of votes (number of rows)
total_votes = len(lines)

# Open the .csv file in read mode
with open('PyPoll/Resources/election_data.csv', 'r') as file: 
    next(file)  # Skip the header row
    
    # Read each row and extract candidate names
    for line in file:
        candidate = line.strip().split(',')[2]
        candidates.add(candidate)

# Open the .csv file in read mode
with open('PyPoll/Resources/election_data.csv', 'r') as file:
    next(file)  # Skip the header row
    
    # Read each row and extract candidate names
    for line in file:
        candidate = line.strip().split(',')[2]
        
        # Update the total number of votes for the candidate
        if candidate in votes_per_candidate:
            votes_per_candidate[candidate] += 1
        else:
            votes_per_candidate[candidate] = 1

# Calculate the total number of votes cast
total_votes = sum(votes_per_candidate.values())

# Open a text file in write mode to export the results
with open('election_results.txt', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Calculate and write the percentage and total number of votes for each candidate
    for candidate, votes in votes_per_candidate.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    
    # Find the winner based on the candidate with the highest number of votes
    winner = max(votes_per_candidate, key=votes_per_candidate.get)
    output_file.write(f"Winner: {winner}\n")

# Print the analysis results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in votes_per_candidate.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")

print("Analysis results exported to election_results.txt")