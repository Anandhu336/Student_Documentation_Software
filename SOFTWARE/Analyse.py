#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
  


# In[2]:


def avg_absences_by_parental_involvement(df_data):
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


def avg_math_score_by_race_for_attendance_over_80(df_data):
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


def avg_writing_score_for_health_analysis(df_data):
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


def top_mothers_education_by_race_and_parental_involvement(df_data):
    
    if df_data is None or df_data.empty:
        print("No data available for analysis.")
        return
    
    def get_top_mother_education_levels(race, parental_involvement):
        print("Available columns:", df_data.columns)
        grouped_data = df_data.groupby(['Race', 'Parental_involvement', 'Mother_education_level ']).size().reset_index(name='count')
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
                print(top_3_levels[['Mother_education_level ', 'count']])
            else:
                print(f"Parental involvement level '{user_parental_involvement}' is not found in the dataset.")
        else:
            print(f"Race '{user_race}' is not found in the dataset.")

        if not change_or_main_menu():
            break





def handle_choice(choice, df_data):
    if choice == '1':
        avg_absences_by_parental_involvement(df_data)
    elif choice == '2':
        avg_math_score_by_race_for_attendance_over_80(df_data)
    elif choice == '3':
        avg_writing_score_for_health_analysis(df_data)
    elif choice == '4':
        top_mothers_education_by_race_and_parental_involvement(df_data)
    elif choice == '5':
        print("Thank you!")
        return False
    else:
        print("Invalid choice. Please choose again.")
    return True

