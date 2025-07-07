Sentiment Analyzer Project

Overview
This project performs sentiment analysis on movie reviews from the IMDB dataset.
It includes steps for preprocessing raw text, converting sentiment labels to numbers, training a Logistic Regression model, and making predictions on new input.

Project Structure

    data/raw/ : contains the original IMDB dataset

    notebooks/ : contains Jupyter notebooks for data exploration, preprocessing, and model testing

    models/ : stores the trained model and vectorizer (as .pkl files)

    scripts/, app/, etc. : will be used later for refactoring the project into modular components

    .venv/ : local Python virtual environment (excluded from git)

Setup

    Create and activate the virtual environment
    python3 -m venv .venv
    source .venv/bin/activate

    Install dependencies
    pip install -r requirements.txt

    Link the venv to Jupyter
    pip install ipykernel
    python -m ipykernel install --user --name=sentiment-env --display-name "Python (sentiment-env)"

    Start Jupyter Lab
    jupyter lab

Dataset
The IMDB Dataset (50,000 movie reviews) is saved in data/raw/IMDB Dataset.csv
Source: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

Notebook Workflow
01_preprocessing.ipynb

    Loads dataset

    Cleans text (removes HTML, punctuation, etc.)

    Encodes sentiment labels (positive = 1, negative = 0)

    Splits data into train/test

    Applies TF-IDF vectorization

02_model_inference.ipynb

    Loads trained model and vectorizer

    Accepts a manual text input

    Cleans and transforms it

    Predicts sentiment label

Notes

    The data/ folder is committed because the dataset is small.

    The model is a basic Logistic Regression for demo purposes.

    Next steps include moving logic to Python files, adding scripts, packaging with Docker, and automating with CI/CD.
