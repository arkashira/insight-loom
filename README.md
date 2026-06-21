# Insight Loom
Insight Loom is a data ingestion and normalization platform that automatically parses and stores documents from Google Drive and Dropbox.

## Features
* OAuth integration for Google Drive and Dropbox
* PDF, DOCX, and TXT file extraction and storage
* Metadata includes file name, owner, and last modified date

## Requirements
* Python 3.8+
* Poetry 1.2.0+

## Installation
1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Run tests: `poetry run pytest`
4. Run the platform: `poetry run python src/data_ingestion.py`
