# Design Document

## Overview
This document outlines the design for the DATA Acquisition CLI  application. The application extracts data from CSV files, restructures it and outputs it in a more useful format or form.

## Architecture
The application follows a modular design with following the components:
- Model: Defines data structures.
- Extract: Contains logic to extract and transform the data.
- Main: Handles command-line arguments and coordinates the extraction process.

## Modules
1. `model.py`: Defines the `XYPair` class.
2. `extract.py`: Contains the `PairBuild` class and its subclass.
`acquire.py`: Main CLI application.

## Data Flow
1. Read CSV file.
2. Extract and transform data.
3. Output transformed data specified directory.

## Extensibility
The application is designed to be extensible to handle multiple input formats and data sources.