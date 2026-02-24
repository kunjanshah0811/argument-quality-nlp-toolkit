# Argument_Quality_Data_Processor

This repository contains Python code for processing the "Dagstuhl-15512-ArgQuality" corpus. It involves downloading the corpus, extracting relevant data, storing it as JSON, creating data splits for machine learning tasks, and computing basic statistics.

## Learning Goals

- Working with available data in Python.
- Data splits for Machine Learning.
- Computing basic statistics.

## Tasks

1. **Download the Corpus**
    - Download the corpus for further processing.

2. **Extract Relevant Data and Store as JSON**
    - Extract relevant information per argument:
        - Argument ID
        - Issue
        - Stance on the issue
        - Argumentativeness annotations (from all three annotators)
        - Quality scores (from all three annotators)
        - Effectiveness scores (from all three annotators)
        - Argument text
    - Store the extracted data as JSON.

3. **Create Data Splits**
    - Split the data into three subsets for training ML models:
        - Training set
        - Test set
        - Validation set
    - Perform a 70-20-10 percent split (train-test-validation).
    - Randomly split the data.
    - Ensure no duplicates exist (i.e., the same argument in two splits).

4. **Compute Statistics**
    - Compute basic statistics on the data.

## Usage

1. Clone this repository:

    ```bash
    git clone <repository-url>
    ```

2. Run the Python script:

    ```bash
    python main.py
    ```

3. After execution, you will find the following files generated:
    - `train.json`: Training set
    - `test.json`: Test set
    - `val.json`: Validation set

## Requirements

- Python 3.x
- XML ElementTree (`xml.etree.ElementTree`)
- JSON (`json`)
- OS (`os`)
- Random (`random`)

## Note

- Adjust paths if necessary.
- Ensure that the corpus directory structure matches the expected structure in the code.

