# Data Acquisition CLI

## Overview
This application extracts data from CSV files, restructures it, and outputs it in a more useful form. It is designed to be flexible and extensible, allowing for addition of new data sources and formats.


## Installation
clone the repository:
```sh
git clone git clone https://github.com/Abbey-commit/python-project.git cd  data-acquisition-cli
```

Install dependdencies using Poetry:
```sh
poetry install
```

## Usage
To run the application, use the following command:
```sh
poetry run python src/acquire.py -o output_directory data/Ascombe_quartet_data.csv