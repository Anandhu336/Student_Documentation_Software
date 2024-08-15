#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv
from Greetings import generate_student_documentation_greeting
from data_loader import load_data_pandas, get_file_path,load_csv_data
from Data_retrieval import change_or_main_menu, get_info_by_id, get_user_choice, get_info_by_race, get_info_by_parental_involvement, get_parental_level, get_info_by_studytime
from Analyse import handle_choice, change_or_main_menu
import Visualization




def display_menu():
    # Call the function to get the greeting message
    greeting_message = generate_student_documentation_greeting()
    

    print("1. Retrieve Data")
    print("2. Analyse Data")
    print("3. Visualization")
    print("4. Exit")


def Main():
    file_path = get_file_path()
    
    df_data = load_data_pandas(file_path)

    if df_data is None or df_data.empty:
        print("Error: Data could not be loaded. Please check the file path or file content And Restart the software.")
        return

    while True:
        display_menu()
        choice = input("Please select an option: ")

        if choice == '1':
            while True:
                data = load_csv_data(file_path)
                print("\nWhich of the following would you like to do? Make your selection from the options shown:")
                print("1. Look up the data records using the provided Student ID number")
                print("2. Retrieve data based on Race")
                print("3. Retrieve data on Parental Involvement and Absences where the number of absences is less than 50")
                print("4. Retrieve data based on study time")
                print("5. Exit")
                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':
                    student_id = input("Enter the student ID: ")
                    get_info_by_id(data, student_id)
                elif sub_choice == '2':
                    race = get_user_choice()
                    if race:
                        get_info_by_race(data, race)
                    else:
                        print("Invalid choice. Please select a valid race.")
                elif sub_choice == '3':
                    parental_involvement = get_parental_level()
                    get_info_by_parental_involvement(data, parental_involvement)
                elif sub_choice == '4':
                    studytime = input("Enter the hours of study: ")
                    get_info_by_studytime(data, Studytime)
                elif sub_choice == '5':
                    print("Thank you")
                    break
                else:
                    print("Invalid choice. Please choose a task again.")

        elif choice == '2':
            while True:
                print("Welcome to the student data analysis tool!")
                print("Please choose an option:")
                print("1. Average absences by parental involvement level")
                print("2. Average math score by race for students with attendance rate over 80%")
                print("3. Average writing score by Health status")
                print("4. Top 3 levels of mother’s education for a specific race of students based on parental involvement levels")
                print("5. Exit")
                sub_choice = input("Enter your choice (1-5): ")

                if not handle_choice(sub_choice, df_data):
                    break

        elif choice == '3':
            while True:
                data = load_data_pandas(file_path)
                Visualization.Visualization(df_data)

    
                break
           

            
        elif choice == '4':
            print("Exiting the Application. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")





if __name__ == "__main__":
    Main()

