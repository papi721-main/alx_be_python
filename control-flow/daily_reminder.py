#!/usr/bin/env python3
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

message = f"Note: '{task}' is a {priority} task. Consider completing it when you have free time."

match priority:
    case "high":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a {priority} task that requires immediate attention today!"
            )
    case "medium":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a {priority} task that requires immediate attention today!"
            )
    case "low":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a {priority} task that requires immediate attention today!"
            )
    case _:
        print("Non-valid priority: use high, medium, or low")
