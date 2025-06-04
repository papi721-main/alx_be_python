#!/usr/bin/env python3

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


if __name__ == "__main__":
    temperature = input("Enter the temperature to convert: ")
    if not temperature.isnumeric():
        print("Invalid temperature. Please enter a numeric value.")
        exit()

    conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    temperature = float(temperature)
    if conversion == "C":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    elif conversion == "F":
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
    else:
        print("Unknown conversion")
