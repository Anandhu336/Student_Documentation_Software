#!/usr/bin/env python
# coding: utf-8

# In[1]:


from data_loader import load_csv_data
from get_file_path import get_file

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

def task_a1(data, student_id):
    if data is None:
        return
    
    while True:
        found = False
        for row in data:
            if row[0] == student_id:
                print(f"Sex: {row[1]}\tAge: {row[2]}\tNumber of Relatives: {row[21]}\tState: {row[26]}\tRace: {row[27]}")
                found = True
                break
        if not found:
            print("ID not found.")
        
        if not change_or_main_menu():
            break
        student_id = input("Enter the student ID: ")
    

def get_user_choice():
    print("Select a race from the options below:")
    print("1. Asian")
    print("2. Other")
    print("3. White")
    print("4. Hispanic")
    print("5. African American")
    
    choice = input("Enter the number corresponding to your choice: ").strip()
    
    race_options = {
        "1": "Asian",
        "2": "Other",
        "3": "White",
        "4": "Hispanic",
        "5": "African American"
    }
    
    return race_options.get(choice, None)

def task_a2(data, race):
    if data is None:
        return
    
    while True:
        found = False
        for row in data:
            if row[27] == race:
                print(f"Sex: {row[1]}\tSchool Support: {row[14]}\tAccess Internet: {row[19]}\tAttendance Rate: {row[31]}\tParental Involvement: {row[37]}")
                found = True
        if not found:
            print(f"Error: Race {race} not found.")
        
        if not change_or_main_menu():
            break
        race = get_user_choice()

def task_a3(data, parental_involvement):
    if data is None:
        return
    
    while True:
        found = False
        for row in data:
            if row[37].strip().lower() == parental_involvement.lower() and int(row[25]) < 50:
                print(f"ID: {row[0]}\tFree Time: {row[22]}\tMath Score: {row[28]}\tReading Score: {row[29]}\tWriting Score: {row[30]}")
                found = True
        
        if not found:
            print(f"Error: Parental involvement '{parental_involvement}' not found.")
        
        if not change_or_main_menu():
            break
        parental_involvement = get_parental_level()

def get_parental_level():
    while True:
        level = input("Enter parental involvement level (high, medium, low): ").strip().lower()
        if level in ['high', 'medium', 'low']:
            return level
        else:
            print("Invalid input. Please enter 'high', 'medium', or 'low'.")

def task_a4(data, Studytime):
    if data is None:
        return
    
    while True:
        found = False
        for row in data[1:]:
            if row[12] == Studytime and int(row[12]) >= 1:
                print(f"Failures: {row[13]}\tHealth: {row[25]}\tSuspensions: {row[32]}\tTravel Time: {row[11]}")
                found = True
        if not found:
            print(f"Error: Studytime '{Studytime}' not found.")
        
        if not change_or_main_menu():
            break
        Studytime = input("Enter the hours of study: ")

def main():
    
    
    if data is None:
        return
    
    while True:
        print("\nWhich of the following would you like to do? Make your selection from the options shown:")
        print("1. Look up the data records using the provided Student ID number")
        print("2. Retrieve data based on Race")
        print("3. Retrieve data on Parental Involvement and Absences where the number of absences is less than 50")
        print("4. Retrieve data based on study time")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter the student ID: ")
            task_a1(data, student_id)
    
        elif choice == '2':
            race = get_user_choice()
            task_a2(data, race)
        elif choice == '3':
            Parental_involvement = get_parental_level()
            task_a3(data, Parental_involvement)
        elif choice == '4':
            Studytime = input("Enter the hours of study,(1,2,3..Hours): ")
            task_a4(data, Studytime)
        elif choice == '5':
            print("Thank you")
            break
        else:
            print("Invalid choice. Please choose a task again.")


    

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the program
    main()

