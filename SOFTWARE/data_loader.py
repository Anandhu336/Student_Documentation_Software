#!/usr/bin/env python
# coding: utf-8

# In[1]:


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



# In[2]:


import pandas as pd
import csv
from Greetings import generate_student_documentation_greeting
from data_loader import load_csv_data
from data_loader import load_data_pandas, get_file_path
from student_documentation import change_or_main_menu, task_a1, get_user_choice, task_a2, task_a3, get_parental_level, task_a4
from Analyse import handle_choice, change_or_main_menu

def inspect_columns(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Columns in the CSV file:")
        print(df.columns)
        return df.columns
    except Exception as e:
        print(f"Error inspecting columns in the CSV file: {e}")
        return None



def display_menu():
    # Call the function to get the greeting message
    greeting_message = generate_student_documentation_greeting()
    print(greeting_message)

    print("1. Retrieve Data")
    print("2. Analyse Data")
    print("3. Visualization")
    print("4. Exit")


def Main():
    file_path = get_file_path()
    inspect_columns(file_path)  # Add this line to inspect the columns of the CSV file
    df_data = load_data_pandas(file_path)

    if df_data is None or df_data.empty:
        print("Error: Data could not be loaded. Please check the file path or file content.")
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
                    task_a1(data, student_id)
                elif sub_choice == '2':
                    race = get_user_choice()
                    if race:
                        task_a2(data, race)
                    else:
                        print("Invalid choice. Please select a valid race.")
                elif sub_choice == '3':
                    parental_involvement = get_parental_level()
                    task_a3(data, parental_involvement)
                elif sub_choice == '4':
                    studytime = input("Enter the hours of study: ")
                    task_a4(data, studytime)
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
            Visualization.main()

        elif choice == '4':
            print("Exiting the Application. Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


def b2_avg_absences_by_parental_involvement(df_data):
    if df_data is None or df_data.empty:
        print("No data available for analysis.")
        return
    
    avg_absences_by_involvement = df_data.groupby('Parental_involvement')['Absences'].mean()
    valid_levels = ['low', 'medium', 'high']

    while True:
        parental_involvement_level = input("Enter the parental involvement level (low, medium, or high): ").lower()

        if parental_involvement_level not in valid_levels:
            print("Not valid. Please check again and re-enter the parental involvement level.")
            continue

        avg_absences = avg_absences_by_involvement.get(parental_involvement_level)

        if avg_absences is not None:
            print(f"The average number of absences for students with {parental_involvement_level.upper()} parental involvement is: {avg_absences:.2f}")
        else:
            print(f"No data available for parental involvement level: {parental_involvement_level}")

        if not change_or_main_menu():
            break


def b3_avg_math_score_by_race_for_attendance_over_80(df_data):
    if df_data is None or df_data.empty:
        print("No data available for analysis.")
        return
    
    high_attendance = df_data[df_data['Attendance_rate'] > 80]
    avg_math_scores_by_race = high_attendance.groupby(df_data['Race'].str.lower())['Math_score'].mean()

    race_dict = {
        '1': 'asian',
        '2': 'white',
        '3': 'hispanic',
        '4': 'african american',
        '5': 'other'
    }

    while True:
        print("Choose the race:")
        print("1. Asian")
        print("2. White")
        print("3. Hispanic")
        print("4. African American")
        print("5. Other")

        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

        if choice in race_dict:
            race = race_dict[choice]
            avg_math_score = avg_math_scores_by_race.get(race)

            if avg_math_score is not None:
                print(f"The average math score for {race.title()} students with an attendance rate above 80% is: {avg_math_score:.2f}")
            else:
                print(f"No {race.title()} students with attendance rate above 80% were found.")
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        if not change_or_main_menu():
            break


def b4_avg_writing_score_for_health_analysis(df_data):
    if df_data is None or df_data.empty:
        print("No data available for analysis.")
        return
    
    valid_levels = ['good', 'poor', 'fair', 'peak', 'excellent']
    avg_writing_scores_by_health = df_data.groupby(df_data['Health'].str.lower())['Writing_score'].mean()

    while True:
        health_level = input("Enter the Health (good, poor, fair, peak, or excellent): ").lower()

        if health_level not in valid_levels:
            print("Not valid. Please check again and re-enter the Health.")
            continue

        avg_writing_score = avg_writing_scores_by_health.get(health_level)

        if avg_writing_score is not None:
            print(f"The average writing score for students with {health_level.capitalize()} health is: {avg_writing_score:.2f}")
        else:
            print(f"No students found with {health_level.capitalize()} health.")

        if not change_or_main_menu():
            break


def b5_top_mothers_education_by_race_and_parental_involvement(df_data):
    
    if df_data is None or df_data.empty:
        print("No data available for analysis.")
        return
    
    def get_top_mother_education_levels(race, parental_involvement):
        print("Available columns:", df_data.columns)
        grouped_data = df_data.groupby(['Race', 'Parental_involvement', 'Mother_education_level']).size().reset_index(name='count')
        filtered_group = grouped_data[(grouped_data['Race'].str.lower() == race) & 
                                      (grouped_data['Parental_involvement'].str.lower() == parental_involvement)]
        top_3_education_levels = filtered_group.sort_values(by='count', ascending=False).head(3)
        return top_3_education_levels

    unique_races = df_data['Race'].str.lower().unique()

    while True:
        print("Unique races in the dataset:")
        for race in unique_races:
            print(race.title())

        user_race = input("Enter the specific race to get the top 3 levels of mother's education: ").strip().lower()

        if user_race in unique_races:
            unique_parental_involvement = df_data['Parental_involvement'].str.lower().unique()

            print("\nUnique parental involvement levels in the dataset:")
            for involvement in unique_parental_involvement:
                print(involvement.title())

            user_parental_involvement = input("Enter the specific parental involvement level: ").strip().lower()

            if user_parental_involvement in unique_parental_involvement:
                top_3_levels = get_top_mother_education_levels(user_race, user_parental_involvement)
                print(f"\nTop 3 levels of mother's education for race '{user_race.title()}' and parental involvement '{user_parental_involvement.title()}':")
                print(top_3_levels[['Mother_education_level', 'count']])
            else:
                print(f"Parental involvement level '{user_parental_involvement}' is not found in the dataset.")
        else:
            print(f"Race '{user_race}' is not found in the dataset.")

        if not change_or_main_menu():
            break





def handle_choice(choice, df_data):
    if choice == '1':
        b2_avg_absences_by_parental_involvement(df_data)
    elif choice == '2':
        b3_avg_math_score_by_race_for_attendance_over_80(df_data)
    elif choice == '3':
        b4_avg_writing_score_for_health_analysis(df_data)
    elif choice == '4':
        b5_top_mothers_education_by_race_and_parental_involvement(df_data)
    elif choice == '5':
        print("Thank you!")
        return False
    else:
        print("Invalid choice. Please choose again.")
    return True


if __name__ == "__main__":
    Main()

