import csv
import random
import sys

def read_csv_file(input_file):
    """
    Reads a CSV file and returns a list of dictionaries representing each row.
    """
    rows = []
    with open(input_file, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            rows.append(row)
    return rows

def create_pairs(rows):
    """
    Creates pairs of people based on opposite genders and shared interests.
    If no shared interests, pairs are still created randomly.
    """
    matches = []
    males = [row for row in rows if row['Gender'].strip().lower() == 'male']
    females = [row for row in rows if row['Gender'].strip().lower() == 'female']

    while males and females:
        male = random.choice(males)
        female = random.choice(females)

        male_interests = set(male['Select three interests'].split(';'))
        female_interests = set(female['Select three interests'].split(';'))
        shared_interests = male_interests.intersection(female_interests)

        # Remove the paired individuals from the list
        males.remove(male)
        females.remove(female)

        match = {
            'Male': male['Name'],
            'Female': female['Name'],
            'Shared Interests': ', '.join(shared_interests) if shared_interests else 'None'
        }
        matches.append(match)

    return matches

def main(input_file):
    rows = read_csv_file(input_file)
    pairs = create_pairs(rows)
    if pairs:
        print("Matches:")
        for pair in pairs:
            print(f"{pair['Male']} and {pair['Female']} (Shared Interests: {pair['Shared Interests']})")
    else:
        print("No matches found.")

if __name__ == '__main__':
    main(sys.argv[1])
