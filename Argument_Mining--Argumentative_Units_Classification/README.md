# Argument Mining - Argumentative Units Classification

This repository contains Python code for classifying argumentative units using machine learning techniques. The tasks involved in this project include choosing text features, extracting features from the data, choosing and training a machine learning model, and saving the results to a file.

## Tasks

1. **Choose Text Features**
    - Select text features to be used in classification, such as n-grams, POS (Part-of-Speech), and token statistics.

2. **Extract Features from Data**
    - Extract features from the provided data for training the machine learning model.

3. **Choose and Train an ML Model**
    - Select a machine learning model and train it using the extracted features.

4. **Save Results to a File**
    - Save the results of the classification process to a file.

## Learning Goals

- Modeling argumentative units as token sequences.
- Text feature definition and extraction.
- Applying machine learning techniques to mine argumentative units.
- Evaluating the effectiveness of the approach.

## Usage

1. Install the required Python packages:

    ```bash
    pip install pandas numpy nltk scikit-learn
    ```

2. Run the Python script:

    ```bash
    python main.py
    ```

3. After execution, the results will be saved in a file named `predictions.csv`.

## Requirements

- Python 3.x
- Pandas (`pandas`)
- NumPy (`numpy`)
- NLTK (`nltk`)
- Scikit-learn (`scikit-learn`)

## Note

- Ensure that the data files (`test-bio.csv` and `train-bio.csv`) are placed in the `data` directory.
- Adjust paths and parameters as needed in the code.
- This script utilizes Naive Bayes and Support Vector Machine (SVM) classifiers for classification tasks.

