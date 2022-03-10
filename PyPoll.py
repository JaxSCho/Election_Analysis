# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of canidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependicies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load, 'r') as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name for each row.
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate lists.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If True then set winning_count = votes and winning_percent = vote_percentage and winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    #print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    print(winning_candidate_summary)

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

    # Write title to the file.
     txt_file.write("Counties in the Election\n-------------------------\n")

    # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")


# Close the files
election_data.close()
txt_file.close()