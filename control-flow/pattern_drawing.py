#!/usr/bin/env python3
length = int(input("Enter the size of the pattern: "))
i = 0
while i < length:
    j = 0
    while j < length:
        print("*", end="")
        j += 1
    i += 1
    print()
