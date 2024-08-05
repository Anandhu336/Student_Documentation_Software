#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
#For reading CSV file
from data_loader import load_csv_data

## For creating visualizations
import matplotlib.pyplot as plt

# For handling default dictionary initialization
from collections import defaultdict

# For calculating average values
from statistics import mean

file_path = 'students_data.csv'


    
# Load the CSV file named 'students_data.csv' into the 'data' variable
data = load_csv_data(file_path)


# Function to create a pie chart for the proportion of students based on their race
def c1_students_proportion_by_race():
    # Initialize a default dictionary to count occurrences of each race
    race_counts = defaultdict(int)
    # Get the header row to determine the index of 'Race' column
    header = data[0]
    race_index = header.index('Race')
    # Iterate over each student record, starting from the second row to skip the header
    for row in data[1:]:
        # Increment the count for the student's race using the index
        race_counts[row[race_index]] += 1  
    # Extract race labels
    labels = list(race_counts.keys())
    
    # Extract the corresponding counts
    sizes = list(race_counts.values())
    
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
def c2_avg_writing_scores_by_race():
    # Initialize a default dictionary to store writing scores for each race
    race_scores = defaultdict(list)
    # Get the header row to determine column indices
    header = data[0]
    race_index = header.index('Race')
    writing_index = header.index('Writing_score')
    # Iterate over each student record, starting from the second row to skip the header
    for row in data[1:]:
        # Append the writing score to the appropriate race using the indices
        race_scores[row[race_index]].append(float(row[writing_index]))

    # Calculate the average writing score for each race
    avg_writing_scores = {race: mean(scores) for race, scores in race_scores.items()}
    # Set the size of the figure
    plt.figure(figsize=(10, 6))
    # Create a bar chart with race labels and their corresponding average writing scores
    plt.bar(avg_writing_scores.keys(), avg_writing_scores.values(), color='skyblue')
    #Provide the title of the chart
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
def c3_relationship_reading_writing_scores():
  reading_scores = [int(float(row[29])) for row in data[1:]]  
  writing_scores = [int(float(row[30])) for row in data[1:]]

  

  # Set the size of the figure
  plt.figure(figsize=(10, 6))
  # Create a scatter plot with reading scores on the x-axis and writing scores on the y-axis
  plt.scatter(reading_scores, writing_scores, alpha=0.5)
    
    # # Provide the title for the plot
  plt.title('Relationship Between Reading and Writing Scores')
    
    # Give the label for the x-axis
  plt.xlabel('Reading Score')

    # Give the label for the y-axis
  plt.ylabel('Writing Score')

    # Enable the grid for the plot
  plt.grid(True)

    # Display the scatter plot
  plt.show()
    
    
  

# Function to create a Health visualisation to showcase information related to student performance
def c4_Health_visualization():

     # Initialize a default dictionary to store math scores for each health status
    health_scores = defaultdict(list)
    # Get the header row to determine column indices
    header = data[0]
    health_index = header.index('Health')
    math_index = header.index('Math_score')
    # Iterate over each student record (starting from the second row to skip the header)
    for row in data[1:]:
        # Append the math score to the appropriate health status using the indices
        health_scores[row[health_index]].append(float(row[math_index]))

    
    # Calculate the average math score for each health status
    avg_math_scores_health = {health: mean(scores) for health, scores in health_scores.items()}
    
    # Set the size of the figure
    plt.figure(figsize=(10, 6))
    # Create a bar chart with health statuses and their corresponding average math scores
    plt.bar(avg_math_scores_health.keys(), avg_math_scores_health.values(), color='orange')
    # Provide the title of the chart
    plt.title('Average Math Scores by Health Status')
    # Give the label for the x-axis
    plt.xlabel('Health Status')
    # Give the label for the y-axis
    plt.ylabel('Average Math Score')
    # Set the rotation of the x-axis labels
    plt.xticks(rotation=0)
    #show the plot
    plt.show()
    
# Main function to display the visualization menu and operate user input
def main():
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
            c1_students_proportion_by_race()
        elif choice == '2':
            c2_avg_writing_scores_by_race()
        elif choice == '3':
            c3_relationship_reading_writing_scores()
        elif choice == '4':
            c4_Health_visualization()
        elif choice == '5':
            # Print a message indicating the program is exiting
            print("Exiting visualization menu...")
            # Exit the loop, which ends the program
            break
        else:
            # Notify the user of an invalid choice
            print("Invalid choice. Please try again.")


# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the program
    main()
    

