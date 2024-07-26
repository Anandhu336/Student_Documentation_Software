#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv


def generate_student_documentation_greeting():
    """
    Generates a greeting for the student documentation software.
    """
    greeting = """
............Welcome to the Student Documentation Software!.......

"""
    return greeting




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
  

      

def task_a1(data, student_id):
    if data is None:
        return
    
    found = False
    for row in data[1:]:
        if row[0] == student_id:
            print(f"Sex: {row[1]}\tAge: {row[2]}\t Number of Relatives: {row[21]}\tState: {row[26]}\tRace: {row[27]}")
            return
    print("ID not found.")
    

def task_a2(data, race):
    if data is None:
        
        return
    
    
    found = False
    for row in data[1:]:
        if row[27] == race:
            print(f"Sex: {row[1]}\tSchool Support: {row[14]}\tAccess Internet: {row[19]}\tAttendance Rate: {row[31]}\tParental Involvement: {row[37]}")
            found = True
    if not found:
        print(f"Error: Race {race} not found.")

 

   

def task_a3(data, Parental_involvement):
    if data is None:
        return
    
    found = False  
    for row in data[1:]:
        if row[37] == Parental_involvement and  int(row[25]) < 50 :
            print(f"ID: {row[0]}\tFree Time: {row[22]}\tMath Score: {row[28]}\tReading Score: {row[29]}\tWriting Score: {row[30]}")
            found = True
    if not found:
        print(f"Error: Parental_involvement {Parental_involvement} not found.")
        

def task_a4(data, Studytime):
    if data is None:
        return
    
    found = False
    for row in data[1:]:
        if row[12] == Studytime and int(row[12]) >= 1 :
            print(f"Failures: {row[13]}\tHealth: {row[25]}\tSuspensions: {row[32]}\traveltime: {row[11]}")
            found = True
    
    if not found:
        print(f"Error: Studytime '{Studytime}' not found.")


        
def main():
    file_path = input("Enter the CSV file path: ")
    
    data = load_csv_data(file_path)
    
    if data is None:
        return
    
    
    while True:
        print("\nWhich of the following would you like to do? Make your selection from the options shown:")
        print("1. Look up the data records using the provided Student ID number")
        print("2. Retrieve data based on Race")
        print("3. Retrieve data on Parental Involvement and Absences where the number of absences is less than 50 ")
        print("4. Retrive data based on study time ")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter the student ID: ")
            task_a1(data, student_id)
        elif choice == '2':
            race = input("Enter the race: \n Few of the common Race in the Data are \n 1. Asian \n 2.White \n African American")
            task_a2(data, race)
        elif choice == '3':
    
            Parental_involvement = input("Enter the parental involvement: ")
            task_a3(data, Parental_involvement)
           

        elif choice == "4":
            Studytime = input("Enter the hours of study  ")
            task_a4(data, Studytime)
            
        
        
        elif choice == '5':

        
            print("Thank you")
            break
        else:
            print("Invalid choice. Please Choose a task again.")

 


# In[ ]:




