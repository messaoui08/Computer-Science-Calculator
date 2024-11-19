import sys
from auth import register_user, authenticate_user
from conversions import *
from ip_planning import calculate_ip_details

def display_menu():
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Convert Number Systems")
    print("4. IP Planning")
    print("5. Exit")

def number_conversion():
    print("\nNumber Conversion:")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Octal")
    print("4. Octal to Decimal")
    print("5. Decimal to Hexadecimal")
    print("6. Hexadecimal to Decimal")
    choice = input("Choose an option: ")

    if choice == '1':
        num = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(num)}")
    elif choice == '2':
        num = input("Enter a binary number: ")
        print(f"Decimal: {binary_to_decimal(num)}")
    elif choice == '3':
        num = int(input("Enter a decimal number: "))
        print(f"Octal: {decimal_to_octal(num)}")
    elif choice == '4':
        num = input("Enter an octal number: ")
       