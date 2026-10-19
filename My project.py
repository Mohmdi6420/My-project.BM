# Question 1: String Manipulation
raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD"

# Step a: Strip whitespace and convert to lowercase
cleaned_step_a = raw_feedback.strip().lower()

# Step b: Replace terminology and remove internal extra spaces
cleaned_step_b = " ".join(cleaned_step_a.replace("speaker", "presenter").split())

# Step c: Apply title case and output via f-string
final_cleaned_feedback = cleaned_step_b.title()

print(f"Original Text: '{raw_feedback}'")
print(f"cleaned Text:  '{final_cleaned_feedback}'")


# Question 2a: Write list of feedback to file
feedback_list = [
    "The Presenter Was Great But The Room Was Cold",
    "The Workshop Content Was Very Informative",
    "Great Session And Interactive Discussion"
]

with open("feedback.txt", "w") as file:
    for item in feedback_list:
        file.write(item + "\n")

# Question 2b: Read and print file contents line by line
print("--- Initial Reading of feedback.txt ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())

# Question 2c: Append a new feedback line and read again
with open("feedback.txt", "a") as file:
    file.write("I Really Enjoyed The Examples Provided Today\n")

print("\n--- Updated Reading of feedback.txt ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())

# Question 3: Exception Handling Implementation
try:
    with open("feedback.txt", "r") as file:
        content = file.readlines()
        print("\nSuccessfully read feedback file for safety verification.")
except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")
except PermissionError:
    print("Permission denied. Close the file and try again.")
finally:
    print("Operation completed.")

# Question 4: Analysis and Report Writing
total_feedback = 0
mentions_of_great = 0

try:
    with open("feedback.txt", "r") as file:
        lines = file.readlines()
        total_feedback = len(lines)
        
        for line in lines:
            if "great" in line.lower():
                mentions_of_great += 1

    # Format summary block
    summary_text = (
        "=== Workshop Feedback Summary ===\n"
        f"total Feedback: {total_feedback}\n"
        f"mentions of 'Great': {mentions_of_great}\n"
    )

    # Write summary to file
    with open("summary.txt", "w") as summary_file:
        summary_file.write(summary_text)

    # Display summary on console using f-strings
    print("\n" + summary_text)

except FileNotFoundError:
    print("Unable to analyze: feedback.txt missing.")
