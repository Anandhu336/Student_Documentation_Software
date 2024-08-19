#!/usr/bin/env python
# coding: utf-8

# In[1]:


from get_file_path import get_file
# Import the csv module for reading CSV files
import csv
#import the pandas module
import pandas as pd

#function to load csv file using csv module 
def load_csv_data(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            #create a csv adder object 
            reader = csv.reader(file)
            #convert the reader object into list of rows 
            data = list(reader)
        #return the list of rows 
        return data
    except FileNotFoundError:
        #handle the case if file not found 
        print("Error: CSV file not found. Please restart the software!")
        return None
    except Exception as e:
        #handle any other exceptions that may occur 
        print(f"Error: {e}")
        return None
#function to load data into a pandas DataFrame
def load_data_pandas(file_path):
    try:
        ## Read the CSV file into a pandas DataFrame
        df_data = pd.read_csv(file_path, header=0, encoding='utf-8')
        # Convert specific columns to lowercase
        df_data['Race'] = df_data['Race'].str.lower()
        df_data['Parental_involvement'] = df_data['Parental_involvement'].str.lower()
        df_data['Mother_education_level '] = df_data['Mother_education_level '].str.lower()
        
         
        #return the data frame 
        return df_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

