# Weather ETL Project
A simple ETL (Extract, Transform, Load) pipeline that fetches real-time weather data from OpenWeatherMap, cleans it, and saves it into a CSV file using Python.

## Project Structure
config.py : Configuration file for API key, list of cities, units, and API base URL.

weather_fetcher.py : Module to extract weather data from OpenWeatherMap API.

cleaner.py : Module to clean and structure the raw JSON data into a pandas DataFrame.

main.py : Main script to run the ETL pipeline and save data to CSV.

notebooks/etl_demo.ipynb : Jupyter Notebook demonstrating the ETL process interactively.

weather_data.csv : Output CSV file generated after running the project.

requirements.txt : List of Python dependencies.

## Features
Extract real-time weather data for multiple cities.

Transform JSON responses into a structured pandas DataFrame.

Load and save cleaned data into CSV for further analysis.

## Installation
1. Clone the repository:
bash
git clone <your-repo-url>
cd weather-etl-project

2. Install dependencies:
bash
pip install -r requirements.txt
3. Add your OpenWeatherMap API key in config.py.

## Usage
bash
python main.py

This will fetch weather data, clean it, and save it to weather_data.csv.

## Demo in Jupyter Notebook
Open notebooks/etl_demo.ipynb to see the ETL process step by step.


## Notes
Modify the CITIES list in config.py to fetch data for more cities.
Each run of main.py overwrites weather_data.csv unless you add a timestamp to the filename.

