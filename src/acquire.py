import argparse
import csv
import json
from pathlib import Path
from extract import Series1Pair, Series2Pair, Series3Pair, Series4Pair

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

def write_json(data, output_path):
    with open(output_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def main(input_file, output_dir):
    output_dir_path = Path(output_dir)
    if not output_dir_path.exists():
        print(f"Creating output directory: {output_dir}")
        output_dir_path.mkdir(parents=True, exist_ok=True)
    
    data = read_csv(input_file)
    pairs = [
        Series1Pair().from_row(data[1]),
        Series2Pair().from_row(data[1]),
        Series3Pair().from_row(data[1]),
        Series4Pair().from_row(data[1])
    ]
    output_path = output_dir_path / "output.json"
    write_json([pair.__dict__ for pair in pairs], output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Acquire and transform data from a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_dir", help="Directory where the output JSON file will be saved.")
    args = parser.parse_args()
    main(args.input_file, args.output_dir)