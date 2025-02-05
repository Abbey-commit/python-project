import argparse
import logging
import csv
import json
from model import XYPair
from pathlib import Path
from extract import Series1Pair, Series2Pair, Series3Pair, Series4Pair

def get_options():
    parser = argparse.ArgumentParser(description="Data Acquisition CLI")
    parser.add_argument("source_file", type=str, help="Path to the source CSV file")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output directory")
    return parser.parse_args()

def main():
    logging.basicConfig(level=logging.INFO)
    options = get_options()
    output_dir = Path(options.output)

    if not output_dir.exists():
        logging.error(f"Output directory {output_dir} does not exist.")
        return
    
    with open(options.source_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # Skip header row
        series1_pairs = []
        series2_pairs = []
        series3_pairs = []
        series4_pairs = []
    
    for row in reader:
        series1_pairs.append(Series1Pair().from_row(row))
        series2_pairs.append(Series2Pair().from_row(row))
        series3_pairs.append(Series3Pair().from_row(row))
        series4_pairs.append(Series4Pair().from_row(row))

    output_files = [
        ("series_1.json", series1_pairs),
        ("series_2.json", series2_pairs),
        ("series_3.json", series2_pairs),
        ("series_4.json", series4_pairs)
    ]

    for filename, data in output_files:
        with open(output_dir / filename, 'w') as outfile:
            for item in data:
                json.dump(item.asdict(), outfile)
                outfile.write('\n')

    logging.info("Processing completed successfully.")

if __name__ == "__main__":
    main()