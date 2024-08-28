#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import all the necessary function , modules,libraries  
import pandas as pd
import csv
from get_file_path import get_file
from Greetings import generate_student_documentation_greeting
from data_loader import load_data_pandas, load_csv_data
from Data_retrieval import change_or_main_menu, get_info_by_id, get_user_choice, get_info_by_race, get_info_by_parental_involvement, get_parental_level, get_info_by_studytime
from Analyse import handle_choice, change_or_main_menu
import Visualization



#define a function to displat the main menu
def display_menu():
    # Call the function to get the greeting message
    greeting_message = generate_student_documentation_greeting()
    
#print menu options
    print("1. Retrieve Data")
    print("2. Analyse Data")
    print("3. Visualization")
    print("4. Exit")

#define a main function
def Main():
    #get the file path to the data
    file_path = get_file()
    #load data into pandas data frame 
    df_data = load_data_pandas(file_path)
    #check if the data is loaded successfully
    if df_data is None or df_data.empty:
        print("Error: Data could not be loaded. Please check the file path or file content And Restart the software.")
        return #return if data could not be loaded 
    #entering a loop for handling the user choice 
    while True:
        #display the main menu 
        display_menu()
        #get the user's choice
        choice = input("Please select an option: ")
        #if the user chose "retrieve data
        if choice == '1':
            while True:
                #load data from the csv file
                data = load_csv_data(file_path)
                print("\nWhich of the following would you like to do? Make your selection from the options shown:")
                print("1. Look up the data records using the provided Student ID number")
                print("2. Retrieve data based on Race")
                print("3. Retrieve data on Parental Involvement and Absences where the number of absences is less than 50")
                print("4. Retrieve data based on study time")
                print("5. Exit")
                #get user's sub-choice
                sub_choice = input("Enter your choice: ")
                #handle the user's sub-choice
                if sub_choice == '1':
                    student_id = input("Enter the student ID: ")
                    #get the function 
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
                    get_info_by_studytime(data, studytime)
                elif sub_choice == '5':
                    print("Thank you")
                    break
                else:
                    print("Invalid choice. Please choose a task again.")
        #chose to analyse the data
        elif choice == '2':
            #enter the loop to display student analysis menu 
            while True:
                print("Welcome to the student data analysis tool!")
                print("Please choose an option:")
                print("1. Average absences by parental involvement level")
                print("2. Average math score by race for students with attendance rate over 80%")
                print("3. Average writing score by Health status")
                print("4. Top 3 levels of mother’s education for a specific race of students based on parental involvement levels")
                print("5. Exit")
                #get user's choice 
                sub_choice = input("Enter your choice (1-5): ")
                #handle the users chooice using the function 
                if not handle_choice(sub_choice, df_data):
                    break
        #chose the visualization
        elif choice == '3':
            while True:
                # Load the data using pandas
                data = load_data_pandas(file_path)
                # Call the Visualization main to generate visualizations
                Visualization.Visualization(df_data)

                break # exist the loop after isualization 
           

        #chose to exist    
        elif choice == '4':
            print("Exiting the Application. Thank you!")
            break # Exit the outer loop, ending the program
            
        #Handle invalid main menu choices
        else:
            print("Invalid choice. Please try again.")







