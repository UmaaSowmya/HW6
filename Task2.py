#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:51:28 2024

@author: puppalaumasowmya
"""

def calculate_effort_hours(sprint_days, pto_days, ceremonies_days, hours_per_day_range):
    try:
        # Calculate total available hours for a team member
        total_hours_per_person = (sprint_days - pto_days - ceremonies_days) * hours_per_day_range

        # Calculate total available hours for the entire team
        total_hours_for_team = total_hours_per_person * team_size # Assuming the entire team has the same availability

        return total_hours_per_person, total_hours_for_team
    except Exception as e:
        print(f"Error: {e}")
        return None, None

# Example usage with your provided values
sprint_days = 10
pto_days = 0
ceremonies_days = 5.5
hours_per_day_range = 8  # Assuming a typical workday is 8 hours
team_size=4

# Calculate effort hours
effort_hours_per_person, effort_hours_for_team = calculate_effort_hours(sprint_days, pto_days, ceremonies_days, hours_per_day_range)

if effort_hours_per_person is not None and effort_hours_for_team is not None:
    print(f"Available Effort-Hours/Person: {effort_hours_per_person} hours")
    print(f"Available Effort-Hours for Entire Team: {effort_hours_for_team} hours")
