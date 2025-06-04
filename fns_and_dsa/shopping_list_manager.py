#!/usr/bin/env python3


def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list")
    print("-" * 15)


def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item not in shopping_list:
        print(f"{item} not found in the shopping list")
    else:
        shopping_list.remove(item)
        print(f"{item} is removed from the shopping list")
    print("-" * 15)


def view_list(shopping_list):
    print("Items\n" + "*" * 15)
    for item in shopping_list:
        print(item)
    print("-" * 15)


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
