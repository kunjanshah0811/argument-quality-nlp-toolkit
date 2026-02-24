# Argument Quality Assessment

This repository contains Python code for automatically assessing the quality of argumentative documents, specifically focusing on student essays on the confirmation bias dimension. The code implements a feature-based supervised approach using text features and machine learning techniques.

## Learning Goals

- Assessing the quality of argumentative documents automatically using text features and ML techniques.

## Tasks

Develop a feature-based supervised approach to automatically assess the quality of arguments in student essays on the confirmation bias dimension.

- **Confirmation Bias:** The absence of opposing arguments.

## Usage

1. Clone this repository:

    ```bash
    git clone <repository-url>
    ```

2. Run the Python script:

    ```bash
    python main.py
    ```

3. After execution, the predictions will be saved in a file named `predictions.json`.

## Requirements

- Python 3.x
- NLTK (`nltk`)
- Pandas (`pandas`)
- NumPy (`numpy`)
- Scikit-learn (`scikit-learn`)

## Note

- Adjust paths and parameters as necessary.
- Ensure that the input data files (`essay-corpus.json` and `train-test-split.csv`) are placed in the `data` directory.
- This script utilizes Support Vector Machine (SVM) for classification tasks.


