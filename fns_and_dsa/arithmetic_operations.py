#!/usr/bin/env python3


def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 != 0:
                return num1 / num2
            elif num2 == 0:
                return "Error - can not divide by zero"

        case _:
            return "Error - unknown operation"
