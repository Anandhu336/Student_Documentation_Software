#!/usr/bin/env python
# coding: utf-8

# In[1]:


# For creating visualizations
import matplotlib.pyplot as plt

# For handling default dictionary initialization
from collections import defaultdict

# For calculating average values
from statistics import mean

# Function to create a pie chart for the proportion of students based on their race
def c1_students_proportion_by_race(df_data):
    # Count occurrences of each race
    race_counts = df_data['Race'].value_counts()

    # Extract race labels and their corresponding counts
    labels = race_counts.index
    sizes = race_counts.values
    
    # Set the size of the figure
    plt.figure(figsize=(10, 6))
    # Create a pie chart with the race labels and their proportions
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    # Provide the title of the chart
    plt.title('Proportion of Students by Race')
    # Ensure the pie chart is circular
    plt.axis('equal')
    # Display the pie chart
    plt.show()

# Function to create a bar chart to compare average writing scores among students in each race group
def c2_avg_writing_scores_by_race(df_data):
    # Calculate the average writing score for each race
    avg_writing_scores = df_data.groupby('Race')['Writing_score'].mean()
    
    # Set the size of the figure
    plt.figure(figsize=(10, 6))
    # Create a bar chart with race labels and their corresponding average writing scores
    plt.bar(avg_writing_scores.index, avg_writing_scores.values, color='skyblue')
    # Provide the title of the chart
    plt.title('Average Writing Scores by Race')
    # Give the label for the x-axis
    plt.xlabel('Race')
    # Give the label for the y-axis
    plt.ylabel('Average Writing Score')
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)
    # Display the bar chart
    plt.show()

# Function to create a scatter plot to illustrate the relationship between reading and writing scores
def c3_relationship_reading_writing_scores(df_data):
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

    # Enable the grid for the plot
    plt.grid(True)

    # Display the scatter plot
    plt.show()

# Function to create a Health visualization to showcase information related to student performance
def c4_Health_visualization(df_data):
    # Calculate the average math score for each health status
    avg_math_scores_health = df_data.groupby('Health')['Math_score'].mean()
    
    # Set the size of the figure
    plt.figure(figsize=(10, 6))
    # Create a bar chart with health statuses and their corresponding average math scores
    plt.bar(avg_math_scores_health.index, avg_math_scores_health.values, color='orange')
    # Provide the title of the chart
    plt.title('Average Math Scores by Health Status')
    # Give the label for the x-axis
    plt.xlabel('Health Status')
    # Give the label for the y-axis
    plt.ylabel('Average Math Score')
    # Set the rotation of the x-axis labels
    plt.xticks(rotation=0)
    # Show the plot
    plt.show()

# Main function to display the visualization menu and operate user input
def Visualization(df_data):
    # Start an infinite loop to display the menu until the user exits
    while True:
        print("Visualization Menu:")
        print("1. Proportion of students by race")
        print("2. Average writing scores by race")
        print("3. Relationship between reading and writing scores")
        print("4. Custom visualization related to student performance")
        print("5. Exit visualization menu")
        
        # Prompt the user to choose an option from the menu
        choice = input("Enter your choice (1-5): ")

        # Operates the user's choice by calling the appropriate function
        if choice == '1':
            c1_students_proportion_by_race(df_data)
        elif choice == '2':
            c2_avg_writing_scores_by_race(df_data)
        elif choice == '3':
            c3_relationship_reading_writing_scores(df_data)
        elif choice == '4':
            c4_Health_visualization(df_data)
        elif choice == '5':
            # Print a message indicating the program is exiting
            print("Exiting visualization menu...")
            # Exit the loop, which ends the program
            break
        else:
            # Notify the user of an invalid choice
            print("Invalid choice. Please try again.")

