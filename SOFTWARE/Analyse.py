#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import the pandas library and alias it as 'pd' for easier access.
import pandas as pd
from data_loader import load_csv_data

# Load data from a csv to dataframe and set the first row to be column names
df_data = pd.read_csv("students_data.csv", header=0, encoding='utf-8')

# Convert the 'Race' column values to lowercase for consistency.
df_data['Race'] = df_data['Race'].str.lower()

# Convert the 'Parental_involvement' column values to lowercase for consistency.
df_data['Parental_involvement'] = df_data['Parental_involvement'].str.lower()

# Convert the 'Mother_education_level' column values to lowercase for consistency.
df_data['Mother_education_level'] = df_data['Mother_education_level '].str.lower()

# Define a function to calculate and display the average absences based on parental involvement levels.
def b2_avg_absences_by_parental_involvement():
    # Define the valid parental involvement levels.
    valid_levels = ['low', 'medium', 'high']
    
    # Start an infinite loop to repeatedly ask for user input.
    while True:
        
        # Ask the user to input a parental involvement level and convert it to lowercase.
        parental_involvement_level = input("Enter the parental involvement level (low, medium, or high): ").lower()
        
        # Check if the input is not one of the valid levels.
        if parental_involvement_level not in valid_levels:
            
            #if invalid input give the output to the user as invalid and ask for again.
            print("Not valid. Please check again and re-enter the parental involvement level.")
            
            #continue the loop 
            continue
            
        #Filter the DataFrame for rows where 'Parental_involvement' matches the user's input.
        students_with_parental_involvement = df_data[df_data['Parental_involvement'] == parental_involvement_level]
        
        # Calculate the average number of absences for the filtered students.
        avg_absences = students_with_parental_involvement['Absences'].mean()

        # output/display the calculated average absences to the user.
        print(f"The average number of absences for students with {parental_involvement_level.upper()} parental involvement is: {avg_absences:.2f}")

        # Call the 'change_or_main_menu' function to ask the user whether to change input or return to the main menu.
        # If the user chooses not to continue, break the loop.
        if not change_or_main_menu():
            break
            
# Define a function to calculate and display the average math score by race for students with attendance over 80%.
def b3_avg_math_score_by_race_for_attendance_over_80():

    # Create a dictionary assigning numbers to race .
    race_dict = {
        '1': 'Asian',
        '2': 'White',
        '3': 'Hispanic',
        '4': 'African American',
        '5': 'Other'
    }

    # Start an infinite loop to repeatedly ask for user input.
    while True:
        #display the race options to the user.
        print("Choose the race:")
        print("1. Asian")
        print("2. White")
        print("3. Hispanic")
        print("4. African American")
        print("5. Other")
        #Ask the user to enter a choice by selecting the given number .
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

        # Check if the input is a valid choice in the race dictionary.
        if choice in race_dict:

            # Get the race corresponding to the user's choice.
            race = race_dict[choice]
            
            # Filter the DataFrame for students with attendance rate greater than 80%.
            high_attendance = df_data[df_data['Attendance_rate'] > 80]
            
            #Filter the DataFrame for students of the selected race.
            race_data = high_attendance[high_attendance['Race'].str.lower() == race.lower()]
            
            # Calculate the average math score for the filtered students.
            avg_math_score = race_data['Math_score'].mean()

            # Check if the average math score is NaN (i.e., no students were found).
            if pd.isna(avg_math_score):
                print(f"No {race} students with attendance rate above 80% were found.")
            else:
                #Display average math score.
                print(f"The average math score for {race} students with attendance rate above 80% is: {avg_math_score:.2f}")
        else:
            
            # If the input is invalid, notify the user and ask for input again.
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        # Call the 'change_or_main_menu' function to ask the user whether to change input or return to the main menu.
        # If the user chooses not to continue, break the loop.
        if not change_or_main_menu():
            break
            
# Define a function for custom analysis that calculates the average writing score for students in good health.
def b4_avg_writing_score_for_health_analysis():

    #Define the valid  levels.
    valid_levels = ['good', 'poor', 'fair','peak','excellent']

    # Start an infinite loop to repeatedly ask for user input.
    while True:

        # Ask the user to input a Health level and convert it to lowercase.
        Health_level = input("Enter the Health (good, poor,fair,peak or excellent): ").lower()

        # Check if the input is not one of the valid levels.
        if Health_level not in valid_levels:
            print("Not valid. Please check again and re-enter the Health .")
            continue
            
        #Filter the DataFrame for rows where 'Health' matches the user's input.
        students_with_Health = df_data[df_data['Health'] == Health_level]
        
        # Calculate the average writing score  for the filtered students.
        average_writing_scores_health = students_with_Health['Writing_score'].mean()

        # output/display the calculated average writing score  to the user.
        print(f'Average writing score of students : {average_writing_scores_health:.2f}')
        
        # Call the 'change_or_main_menu' function to ask the user whether to change input or return to the main menu.
        # If the user chooses not to continue, break the loop.
        if not change_or_main_menu():
            break


# Define a function to find and display the top 3 mother's education levels by race and parental involvement.
def b5_top_mothers_education_by_race_and_parental_involvement():
    # Define an inner function to filter the DataFrame and get the top 3 education levels.
    def get_top_mother_education_levels(race, parental_involvement):
        
        # Filter the DataFrame based on the race and parental involvement level
        filtered_df_data = df_data[(df_data['Race'] == race) & (df_data['Parental_involvement'] == parental_involvement)]
        
        # Get the counts of each mother's education level
        education_counts = filtered_df_data['Mother_education_level'].value_counts()
        
        # Get the top 3 education levels
        top_3_education_levels = education_counts.head(3)

        #return the three education levels
        return top_3_education_levels

    # Get the unique race categories present in the DataFrame.
    unique_races = df_data['Race'].unique()

    # Start an infinite loop to repeatedly ask for user input.
    while True:
        # Display the unique races available in the dataset.
        print("Unique races in the dataset:")
        
        for race in unique_races:
            print(race.title())

        #Ask the user to enter the race and convert it into lower case
        user_race = input("Enter the specific race to get the top 3 levels of mother's education: ").strip().lower()
        
        # Check if the user's input is a valid race in the dataset.
        if user_race in unique_races:

            # Get the unique parental involvement levels available in the dataset.
            unique_parental_involvement = df_data['Parental_involvement'].unique()

            # Display the unique parental involvement levels.
            print("\nUnique parental involvement levels in the dataset:")
            for involvement in unique_parental_involvement:
                print(involvement.title())
                
            # Ask the user to input a specific parental involvement level and convert it to lowercase.
            user_parental_involvement = input("Enter the specific parental involvement level: ").strip().lower()

            # Check if the user's input is a valid parental involvement level in the dataset.
            if user_parental_involvement in unique_parental_involvement:

                # Get the top 3 mother's education levels for the specified race and parental involvement level.
                top_3_levels = get_top_mother_education_levels(user_race, user_parental_involvement)

                
                # Show the output for  the top 3 mother's education levels to the user.
                print(f"\nTop 3 levels of mother's education for race '{user_race.title()}' and parental involvement '{user_parental_involvement.title()}':")
                print(top_3_levels)
            else:
                
                # If the parental involvement level is invalid, notify the user.
                print(f"Parental involvement level '{user_parental_involvement}' is not found in the dataset.")
        else:
            # If the race is invalid, notify the user.
            print(f"Race '{user_race}' is not found in the dataset.")

        # Call the 'change_or_main_menu' function to ask the user whether to change input or return to the main menu.
        # If the user chooses not to continue, break the loop.

        if not change_or_main_menu():
            break
# Define a function to display the main menu options to the user.
def display_menu():
    # Print a welcome message and menu options.
    print("Welcome to the student data analysis tool!")
    print("Please choose an option:")
    print("1. Average absences by parental involvement level")
    print("2. Average math score by race for students with attendance rate over 80%")
    print("3. Average writing score by Health status")
    print("4. Top 3 levels of mother’s education for a specific race of students based on parental involvement levels")
    print("5. Exit")


# Define a function to prompt the user to change input or return to the main menu.
def change_or_main_menu():
    # Start an infinite loop to repeatedly ask for user input.
    while True:
        # Display the options to the user.
        print("Would you like to:")
        print("1. Change input and get a new output")
        print("2. Go back to the main menu")
        # Ask the user to make a choice.
        choice = input("Enter your choice (1 or 2): ")
        # If the user chooses '1', return True to indicate continuation.
        if choice == '1':
            return True
            
        # If the user chooses '2', return False to indicate returning to the main menu.
        elif choice == '2':
            return False
            
        # If the input is invalid, notify the user and ask for input again.
        else:
            print("Invalid choice. Please try again.")
            
# Define a function to interface the user's menu selection and execute the corresponding function.
def handle_choice(choice):
    # Check if the user selected option '1' for average absences by parental involvement.
    if choice == '1':
        b2_avg_absences_by_parental_involvement()
    # Check if the user selected option '2' for average math score by race for attendance over 80%.
    elif choice == '2':
        b3_avg_math_score_by_race_for_attendance_over_80()
    # Check if the user selected option '3' for Average writing score based on Health.
    elif choice == '3':
        b4_avg_writing_score_for_health_analysis()
    # Check if the user selected option '4' for top 3 mother's education levels by race and parental involvement.
    elif choice == '4':
        b5_top_mothers_education_by_race_and_parental_involvement()
    # Check if the user selected option '5' to exit the program.
    elif choice == '5':
        print("Exiting...")
        return False
    # If the input is invalid, notify the user and ask for input again.
    else:
        print("Invalid choice. Please try again.")
    return True
    
# Define the main function to start the program.
def main():
    # Start an infinite loop to repeatedly display the menu and handle the user's choice.
    while True:
        display_menu()
        # Ask the user to select an option from the menu.
        # operates the user's choice and break the loop if the user chooses to exit.
        choice = input("Enter your choice (1-5): ")
        if not handle_choice(choice):
            break
# Check if the script is being run as the main program.
if __name__ == "__main__":
    # Call the main function to start the program
    main()

