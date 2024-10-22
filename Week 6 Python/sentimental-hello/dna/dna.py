import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Plese input 2 arguments")

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)

    # TODO: Read DNA sequence file into a variable
    dna_sequence = ""
    with open(sys.argv[2]) as file:
        dna_sequence = file.read()

    # database is a list of dict, e.g. [{'name': 'Alice', 'AGATC': '2', 'AATG': '8', 'TATC': '3'}, {'name': 'Bob', 'AGATC': '4', 'AATG': '1', 'TATC': '5'}, ...]
    # database[0] is the first row, e.g. {'name': 'Alice', 'AGATC': '2', 'AATG': '8', 'TATC': '3'}
    # We then get the columns by calling dict.keys() and put them in a list, so ['name', 'AGATC', 'AATG', 'TATC']
    keys = list(database[0].keys())
    # We drop the first column, so ['AGATC', 'AATG', 'TATC']
    short_tandem_repeats = keys[1:]
    
    # TODO: Find longest match of each STR in DNA sequence
    # we traverse all the STRs
    # for each STR, we use longest_match to get back the count
    # result is a dict to record the count, e.g. {'AGATC': 4, 'AATG': 1, 'TATC': 5}
    result = {}
    for short_tandem_repeat in short_tandem_repeats:
        count = longest_match(dna_sequence, short_tandem_repeat)
        result[short_tandem_repeat] = count

    # TODO: Check database for matching profiles
    # For each person in the database, and for each STR
    # We check if the person's STR count is same as the result's STR count,
    # If the STR count doesn't match, we break the loop and move on to the next person
    # Otherwise, we save his/her name
    name = "No Match"
    for person in database:
        match = True
        for short_tandem_repeat in short_tandem_repeats:
            if int(person[short_tandem_repeat]) != result[short_tandem_repeat]:
                match = False
                break

        if (match):
            name = person['name']

    print(name)
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
