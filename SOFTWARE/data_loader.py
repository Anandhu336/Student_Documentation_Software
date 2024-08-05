#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
def load_csv_data(file_path):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        return data
    except FileNotFoundError:
        print("Error: CSV file not found..Please Restart the software!!")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

