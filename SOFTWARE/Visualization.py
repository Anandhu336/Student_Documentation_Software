#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import necessary libraries




# For creating visualizations
import matplotlib.pyplot as plt

# For handling default dictionary initialization
from collections import defaultdict

# For calculating average values
from statistics import mean

# Function to create a pie chart for the proportion of students based on their race
def students_proportion_by_race(df_data):
    # Count occurrences of each race
    race_counts = df_data['Race'].value_counts()

    # Extract race labels and their corresponding counts
    labels = race_counts.index
    sizes = race_counts.values
    
    # Set the size of the figure
    plt.figure(figsize=(10, 6))
    # Create a pie chart with the race labels 
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    #  the title of the chart
    plt.title('Proportion of Students by Race')
    
    # Display the pie chart
    plt.show()

# Function to create a bar chart to compare average writing scores among students in each race group
def avg_writing_scores_by_race(df_data):
    # Initialize a defaultdict to collect writing scores by race
    race_scores = defaultdict(list)
    # Iterate over each race and writing score from the DataFrame
    for race, writing_score in zip(df_data['Race'], df_data['Writing_score']):
        #race name to lower case 
        race = race.strip().lower()
        # Convert writing score to float
        writing_score = float(writing_score)
        race_scores[race].append(writing_score)
    
    # Calculating average writing score for each race
    avg_scores = {race: sum(scores)/len(scores) for race, scores in race_scores.items()}
    
    # Plotting the data
    plt.figure(figsize=(10, 6))
    # Create a bar plot
    plt.bar(avg_scores.keys(), avg_scores.values(), color='skyblue')
    # Label for the x-axis
    plt.xlabel('Race')
    # Label for the y-axis
    plt.ylabel('Average Writing Score')
    #title
    plt.title('Average Writing Scores by Race')
    
    # Display the plot
    plt.show()
   

# Function to create a scatter plot to illustrate the relationship between reading and writing scores
def relationship_reading_writing_scores(df_data):
    # Extract reading and writing scores
    reading_scores = df_data['Reading_score']
    writing_scores = df_data['Writing_score']

    # Set the size of the figure
    plt.figure(figsize=(10, 6))
    # Create a scatter plot with reading scores on the x-axis and writing scores on the y-axis
    plt.scatter(reading_scores, writing_scores, alpha=0.5)
    
    # Provide the title for the plot
    plt.title('Relationship Between Reading and Writing Scores')
    
    # Give the label for the x-axis
    plt.xlabel('Reading Score')

    # Give the label for the y-axis
    plt.ylabel('Writing Score')

    

    # Display the scatter plot
    plt.show()

def Health_visualization(df_data):
    # Calculate the average math score for each health status
    avg_math_scores_health = defaultdict(list)
    
    # Iterate over the DataFrame rows
    for health, math_score in zip(df_data['Health'], df_data['Math_score']):
        health = health.strip().lower()  # Normalize health status string
        math_score = float(math_score)   # Ensure the math score is a float
        # append the math score to the list  corresponding to the health
        avg_math_scores_health[health].append(math_score)
    
    # Calculate the average scores
    avg_scores = {health: sum(scores) / len(scores) for health, scores in avg_math_scores_health.items()}
    
    # Plotting
    plt.figure(figsize=(10, 6))
    #plot the bar chart 
    plt.bar(avg_scores.keys(), avg_scores.values(), color='red')
    plt.xlabel('Health')
    plt.ylabel('Average Math Score')
    plt.title('Average Math Scores by Health')
   
    plt.show()





    



# Main function to display the visualization menu and operate user input
def Visualization(df_data):
    # Start an infinite loop to display the menu until the user exits
    while True:
        print("Visualization Menu:")
        print("1. Proportion of students by race")
        print("2. Average writing scores by race")
        print("3. Relationship between reading and writing scores")
        print("4. Average Math scores by Health")
        print("5. Exit visualization menu")
        
        # Prompt the user to choose an option from the menu
        choice = input("Enter your choice (1-5): ")

        # Operates the user's choice by calling the appropriate function
        if choice == '1':
            students_proportion_by_race(df_data)
        elif choice == '2':
            avg_writing_scores_by_race(df_data)
        elif choice == '3':
            relationship_reading_writing_scores(df_data)
        elif choice == '4':
            Health_visualization(df_data)
        elif choice == '5':
            # Print a message indicating the program is exiting
            print("Exiting visualization menu...")
            # Exit the loop, which ends the program
            break
        else:
            # Notify the user of an invalid choice
            print("Invalid choice. Please try again.")





