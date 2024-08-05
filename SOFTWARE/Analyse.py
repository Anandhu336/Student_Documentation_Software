#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Read the CSV file
df_data = pd.read_csv("students_data.csv", header=0, encoding='utf-8')
df_data['Race'] = df_data['Race'].str.lower()
df_data['Parental_involvement'] = df_data['Parental_involvement'].str.lower()
df_data['Mother_education_level'] = df_data['Mother_education_level '].str.lower()



def b2_avg_absences_by_parental_involvement():
    valid_levels = ['low', 'medium', 'high']
    while True:
        parental_involvement_level = input("Enter the parental involvement level (low, medium, or high): ").lower()
        if parental_involvement_level not in valid_levels:
            print("Not valid. Please check again and re-enter the parental involvement level.")
            continue
        students_with_parental_involvement = df_data[df_data['Parental_involvement'] == parental_involvement_level]
        avg_absences = students_with_parental_involvement['Absences'].mean()
        print(f"The average number of absences for students with {parental_involvement_level.upper()} parental involvement is: {avg_absences:.2f}")
        
        if not change_or_main_menu():
            break

def b3_avg_math_score_by_race_for_attendance_over_80():
    race_dict = {
        '1': 'Asian',
        '2': 'White',
        '3': 'Hispanic',
        '4': 'African American',
        '5': 'Other'
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
            high_attendance = df_data[df_data['Attendance_rate'] > 80]
            race_data = high_attendance[high_attendance['Race'].str.lower() == race.lower()]
            avg_math_score = race_data['Math_score'].mean()
            if pd.isna(avg_math_score):
                print(f"No {race} students with attendance rate above 80% were found.")
            else:
                print(f"The average math score for {race} students with attendance rate above 80% is: {avg_math_score:.2f}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        
        if not change_or_main_menu():
            break

def b4_custom_analysis():
    while True:
        average_writing_scores_good_health = df_data[df_data['Health'] == 'good']['Writing_score'].mean()
        print(f'Average writing score of students with good health: {average_writing_scores_good_health:.2f}')
        
        if not change_or_main_menu():
            break

def b5_top_mothers_education_by_race_and_parental_involvement():
    def get_top_mother_education_levels(race, parental_involvement):
        # Filter the DataFrame based on the specified race and parental involvement level
        filtered_df_data = df_data[(df_data['Race'] == race) & (df_data['Parental_involvement'] == parental_involvement)]
        
        # Get the counts of each mother's education level
        education_counts = filtered_df_data['Mother_education_level'].value_counts()
        
        # Get the top 3 education levels
        top_3_education_levels = education_counts.head(3)
        
        return top_3_education_levels

    unique_races = df_data['Race'].unique()

    while True:
        print("Unique races in the dataset:")
        for race in unique_races:
            print(race.title())

        user_race = input("Enter the specific race to get the top 3 levels of mother's education: ").strip().lower()

        if user_race in unique_races:
            unique_parental_involvement = df_data['Parental_involvement'].unique()

            print("\nUnique parental involvement levels in the dataset:")
            for involvement in unique_parental_involvement:
                print(involvement.title())
            
            user_parental_involvement = input("Enter the specific parental involvement level: ").strip().lower()

            if user_parental_involvement in unique_parental_involvement:
                top_3_levels = get_top_mother_education_levels(user_race, user_parental_involvement)
                print(f"\nTop 3 levels of mother's education for race '{user_race.title()}' and parental involvement '{user_parental_involvement.title()}':")
                print(top_3_levels)
            else:
                print(f"Parental involvement level '{user_parental_involvement}' is not found in the dataset.")
        else:
            print(f"Race '{user_race}' is not found in the dataset.")

        if not change_or_main_menu():
            break

def display_menu():
    print("Welcome to the student data analysis tool!")
    print("Please choose an option:")
    print("1. Average absences by parental involvement level")
    print("2. Average math score by race for students with attendance rate over 80%")
    print("3. Custom data analysis")
    print("4. Top 3 levels of mother’s education for a specific race of students based on parental involvement levels")
    print("5. Exit")

def change_or_main_menu():
    while True:
        print("Would you like to:")
        print("1. Change input and get a new output")
        print("2. Go back to the main menu")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            return True
        elif choice == '2':
            return False
        else:
            print("Invalid choice. Please try again.")

def handle_choice(choice):
    if choice == '1':
        b2_avg_absences_by_parental_involvement()
    elif choice == '2':
        b3_avg_math_score_by_race_for_attendance_over_80()
    elif choice == '3':
        b4_custom_analysis()
    elif choice == '4':
        b5_top_mothers_education_by_race_and_parental_involvement()
    elif choice == '5':
        print("Exiting...")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if not handle_choice(choice):
            break

if __name__ == "__main__":
    main()

