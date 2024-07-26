#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd



def b2_avg_absences_by_parental_involvement(data):
    
    
   
    average_absences = df[df['Parental_involvement'] == parental_involvement_level]['Absences'].mean()
    print(f'Average number of absences: {average_absences}')
    
    
    
    

    
    return average_absences

def b3_avg_math_score_by_race_for_attendance_over_80(data):
    
    
    high_attendance = data[data['Attendance_rate'] > 80]
    
    
    avg_math_score = high_attendance.groupby('Race')['Math_score'].mean()
    
    return avg_math_score

def b4_custom_analysis(data):
    average_writing_scores_good_health = df[df['Health'] == 'good']['Writing_score'].mean()
    print(f'Average writing score of students with good health: {average_writing_scores_good_health}')
    
    
    
    return 
def analyse():
    
    data = pd.read_csv('students_data.csv')
    
    print("Welcome to the student data analysis tool!")
    print("Please choose an option:")
    
    print("1. Average absences by parental involvement level")
    print("2. Average math score by race for students with attendance rate over 80%")
    print("3. Custom data analysis")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        Parental_involvement = input("Enter the parental involvement: ")
        b2_avg_absences_by_parental_involvement(data)
        
    elif choice == 2:
        print(b3_avg_math_score_by_race_for_attendance_over_80(data))
    elif choice == 3:
        b4_custom_analysis(data)
    
    else:
        print("Invalid choice. Please try again.")


# In[ ]:




