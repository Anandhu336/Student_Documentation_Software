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
            
#function to retrieve the data by student ID
def get_info_by_id(data, student_id):
    #check if the dat is loaded or not 
    if data is None:
        return
    #starting the loop 
    while True:
        found = False #intialize the flag for student's ID if found 
        for row in data:
            # Check if the current row's first element (ID) matches the input student ID
            if row[0] == student_id:
                # Print the relevant information for students of the specified ID
                print(f"Sex: {row[1]}\tAge: {row[2]}\tNumber of Relatives: {row[21]}\tState: {row[26]}\tRace: {row[27]}")
                found = True # Set the flag to True to indicate the ID was found
                break
        # If the ID was not found, inform the user
        if not found:
            print("ID not found ,Try to start with ID-(NUMBER).")
        
        if not change_or_main_menu():
            break
        # Prompt the user to enter a new student ID for the next iteration
        student_id = input("Enter the student ID: ")
    
#function to handle the user choice for race  
def get_user_choice():
    #display the race options
    print("Select a race from the options below:")
    print("1. Asian")
    print("2. Other")
    print("3. White")
    print("4. Hispanic")
    print("5. African American")
    
    choice = input("Enter the number corresponding to your choice: ").strip()
    # dictionary to map the user's choice to the corresponding race name
    race_options = {
        "1": "Asian",
        "2": "Other",
        "3": "White",
        "4": "Hispanic",
        "5": "African American"
    }
    
    return race_options.get(choice, None)
# function to retrieve data of  students for specific race
def get_info_by_race(data, race):
    if data is None:
        return
    
    while True:
        found = False
        # Iterate over each row in the data
        for row in data:
            # Check if the current row's race  matches the input race
            if row[27] == race:
                # Print the relevant information for students of the specified race
                print(f"Sex: {row[1]}\tSchool Support: {row[14]}\tAccess Internet: {row[19]}\tAttendance Rate: {row[31]}\tParental Involvement: {row[37]}")
                found = True
        if not found:
            print(f"Error: Race {race} not found.")
        # Check if the user wants to continue or return to the main menu
        if not change_or_main_menu():
            break
        # ask the user to select a new race using the get_user_choice() function
        race = get_user_choice()


#function to retrieve data by parental involvement level whose absenses are less than 50 
def get_info_by_parental_involvement(data, parental_involvement):
    if data is None:
        return
    
    while True:
        found = False
        #iterate over each row in the data
        for row in data:
            if row[37].strip().lower() == parental_involvement.lower() and int(row[25]) < 50:
                #print the relevant student information 
                print(f"ID: {row[0]}\tFree Time: {row[22]}\tMath Score: {row[28]}\tReading Score: {row[29]}\tWriting Score: {row[30]}")
                found = True
        # If no students with the specified parental involvement level were found, inform the user
        if not found:
            print(f"Error: Parental involvement '{parental_involvement}' not found.")
        
        if not change_or_main_menu():
            break
        # Prompt the user to select a new parental involvement level using the get_parental_level() function   
        parental_involvement = get_parental_level()

#function to enter the specified valid parental involvement level from the user 
def get_parental_level():
    while True:
        #ask the user to enter the parental involvement level 
        level = input("Enter parental involvement level (high, medium, low): ").strip().lower()
        #check if the input is valid or not 
        if level in ['high', 'medium', 'low']:
            return level#return the valid level
        else:
            #inform the user the input is invalid 
            print("Invalid input. Please enter 'high', 'medium', or 'low'.")
            
#function to retrieve the data  by student study time  
def get_info_by_studytime(data, Studytime):
    if data is None:
        return
    
    while True:
        found = False
        # Iterate over each row in the data starting from the second row 
        for row in data[1:]:
            # Check if the study time matches and is greater than 1 hour
            if row[12] == Studytime and int(row[12]) > 1:
                #print the relevant information of the student 
                print(f"Failures: {row[13]}\tHealth: {row[25]}\tSuspensions: {row[32]}\tTravel Time: {row[11]}")
                found = True
        if not found:
            print(f"Error: Studytime '{Studytime}' not found.")
        
        if not change_or_main_menu():
            break
        # ask the user to enter a new study time in hours
        Studytime = input("Enter the hours of study(1,2,3..Hours): ")
        

