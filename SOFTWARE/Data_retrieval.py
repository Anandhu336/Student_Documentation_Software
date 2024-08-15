#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

def get_info_by_id(data, student_id):
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

def get_info_by_race(data, race):
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

def get_info_by_parental_involvement(data, parental_involvement):
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

def get_info_by_studytime(data, Studytime):
    if data is None:
        return
    
    while True:
        found = False
        for row in data[1:]:
            if row[12] == Studytime and int(row[12]) > 1:
                print(f"Failures: {row[13]}\tHealth: {row[25]}\tSuspensions: {row[32]}\tTravel Time: {row[11]}")
                found = True
        if not found:
            print(f"Error: Studytime '{Studytime}' not found.")
        
        if not change_or_main_menu():
            break
        Studytime = input("Enter the hours of study(1,2,3..Hours): ")
        

