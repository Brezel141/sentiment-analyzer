# Sentiment Analyzer Project

## Overview

This project performs sentiment analysis on movie reviews from the IMDB dataset.  
We preprocess raw text data, convert labels to numeric, and prepare data for machine learning models.

## Project Structure

- `data/raw/` — contains the original dataset CSV  
- `notebooks/` — Jupyter notebooks with exploration and preprocessing  
- `app/`, `models/`, `scripts/` — folders for application code, trained models, and utility scripts  
- `.venv/` — Python virtual environment (ignored in git)


## Dataset

The IMDB Dataset of 50k movie reviews is stored in data/raw/IMDB Dataset.csv.
Source: Kaggle
Notebook Workflow

    01_preprocessing.ipynb: Data loading, cleaning, label encoding, train/test split, and TF-IDF vectorization.
