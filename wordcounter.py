from collections import Counter

# This program counts how many times each word appear in the text file, it then saves the words from the most frequently used to the least frequently used words. 

def CountFrequency(file_path):
    with open(file_path, 'r') as file:
        # Read the contents of the file
        text = file.read()
    
    # Split the text into individual words
    words = text.split()

    # Count the frequency of each word using Counter
    word_counts = Counter(words)

    return word_counts

def SaveReport(word_counts, report_file_path):
    with open(report_file_path, 'w') as report_file:
        # Sort the word counts in descending order based on frequency
        sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

        # Write the sorted word counts to the report file
        for word, count in sorted_counts:
            report_file.write(f"{word}: {count}\n")

# Path to the input text file
input_file_path = "sample.txt"

# Path to the output report file
report_file_path = "word_frequency_report.txt"

# Count the word frequency
word_counts =CountFrequency(input_file_path)

# Save the word frequency report
SaveReport(word_counts, report_file_path)

print("Word frequency report saved successfully.")