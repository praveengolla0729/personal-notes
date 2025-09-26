import csv

# open and read the CSV file
with open("karishma_data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("Praveen & Karishma Love Journey Details:")
        print(f"Names       : {row['person1_name']} and {row['person2_name']}")
        print(f"Ages        : {row['age1']} and {row['age2']}")
        print(f"Met at      : {row['meet_at']}")
        print(f"Staying at  : {row['staying_at']}")
        print(f"Plan to marry: {row['planning_to_marry']}")
