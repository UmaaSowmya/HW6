#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:39:54 2024

@author: puppalaumasowmya
"""

import pandas as pd

def calculate_average_velocity_from_csv(csv_file):
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Extract the story point estimates column
        story_points_column = 'Custom field (Story point estimate)'
        previous_sprint_points = df[story_points_column].tolist()

        total_points = sum(previous_sprint_points)
        num_sprints = len(previous_sprint_points)

        if num_sprints == 0:
            print("Error: Cannot calculate average velocity with zero sprints.")
            return None

        average_velocity = total_points / num_sprints
        return average_velocity
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage with your CSV file
csv_file_path = 'jira.csv'
average_velocity = calculate_average_velocity_from_csv(csv_file_path)

if average_velocity is not None:
    print(f"Average Velocity: {average_velocity}")
