#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import matplotlib.pyplot as plt
from collections import defaultdict
from statistics import mean

# Function to load CSV data
def load_csv(filename):
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Load the CSV file
data = load_csv('students_data.csv')

# Function to create a pie chart for the proportion of students based on their race
def c1_students_proportion_by_race():
    race_counts = defaultdict(int)
    for row in data:
        race_counts[row['Race']] += 1

    labels = list(race_counts.keys())
    sizes = list(race_counts.values())

    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Proportion of Students by Race')
    plt.axis('equal')
    plt.show()

# Function to create a bar chart to compare average writing scores among students in each race group
def c2_avg_writing_scores_by_race():
    race_scores = defaultdict(list)
    for row in data:
        race_scores[row['Race']].append(float(row['Writing_score']))

    avg_writing_scores = {race: mean(scores) for race, scores in race_scores.items()}

    plt.figure(figsize=(10, 6))
    plt.bar(avg_writing_scores.keys(), avg_writing_scores.values(), color='skyblue')
    plt.title('Average Writing Scores by Race')
    plt.xlabel('Race')
    plt.ylabel('Average Writing Score')
    plt.xticks(rotation=45)
    plt.show()

# Function to create a scatter plot to illustrate the relationship between reading and writing scores
def c3_relationship_reading_writing_scores():
    reading_scores = [float(row['Reading_score']) for row in data]
    writing_scores = [float(row['Writing_score']) for row in data]

    plt.figure(figsize=(10, 6))
    plt.scatter(reading_scores, writing_scores, alpha=0.5)
    plt.title('Relationship Between Reading and Writing Scores')
    plt.xlabel('Reading Score')
    plt.ylabel('Writing Score')
    plt.grid(True)
    plt.show()

# Function to create a custom visualisation to showcase information related to student performance
def c4_custom_visualization():
    health_scores = defaultdict(list)
    for row in data:
        health_scores[row['Health']].append(float(row['Math_score']))

    avg_math_scores_health = {health: mean(scores) for health, scores in health_scores.items()}

    plt.figure(figsize=(10, 6))
    plt.bar(avg_math_scores_health.keys(), avg_math_scores_health.values(), color='orange')
    plt.title('Average Math Scores by Health Status')
    plt.xlabel('Health Status')
    plt.ylabel('Average Math Score')
    plt.xticks(rotation=0)
    plt.show()

def main():
    while True:
        print("Visualization Menu:")
        print("1. Proportion of students by race")
        print("2. Average writing scores by race")
        print("3. Relationship between reading and writing scores")
        print("4. Custom visualization related to student performance")
        print("5. Exit visualization menu")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            c1_students_proportion_by_race()
        elif choice == '2':
            c2_avg_writing_scores_by_race()
        elif choice == '3':
            c3_relationship_reading_writing_scores()
        elif choice == '4':
            c4_custom_visualization()
        elif choice == '5':
            print("Exiting visualization menu...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    

