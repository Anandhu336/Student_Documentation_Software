#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd

def get_file_path():
    return input("Please enter the file path of the CSV file: ")

def load_csv_data(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except FileNotFoundError:
        print("Error: CSV file not found. Please restart the software!")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def load_data_pandas(file_path):
    try:
        df_data = pd.read_csv(file_path, header=0, encoding='utf-8')
        df_data['Race'] = df_data['Race'].str.lower()
        df_data['Parental_involvement'] = df_data['Parental_involvement'].str.lower()
        df_data['Mother_education_level '] = df_data['Mother_education_level '].str.lower()
        
         
        
        return df_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

