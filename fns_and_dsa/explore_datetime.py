#!/usr/bin/env python3
from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(
        f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}'
    )


def calculate_future_date():
    current_date = datetime.now()
    num_of_days = int(
        input("Enter the number of days to add to the current date: ")
    )
    future_date = current_date + timedelta(days=num_of_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
