import csv
import json
import sys

def csv_to_json(csv_file, json_file):
    # Open the CSV file and read its contents
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        # Convert CSV data to a list of dictionaries
        data = list(csv_data)

    # Remove spaces from keys and values
    for entry in data:
        entry_no_spaces = {key.replace(" ", ""): value.replace(" ", "") for key, value in entry.items()}
        data[data.index(entry)] = entry_no_spaces

    # Write the JSON data to a file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_csv_file> <output_json_file>")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    output_json_file = sys.argv[2]

    csv_to_json(input_csv_file, output_json_file)
