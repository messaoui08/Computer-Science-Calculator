import hashlib
import os

USER_FILE = os.path.join("data", "users.txt")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user():
    print("1. Login\n2. Register")
    choice = input("Select an option: ")
    if choice == "1":
        return login()
    elif choice == "2":
        return register()
    else:
        print("Invalid choice!")
        return False

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    with open(USER_FILE, "r") as f:
        users = f.readlines()
    for user in users:
        stored_username, stored_password = user.strip().split(":")
        if username == stored_username and hashed_password == stored_password:
            print("Login successful!")
            return True
    print("Invalid username or password!")
    return False

def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    hashed_password = hash_password(password)
    with open(USER_FILE, "a") as f:
        f.write(f"{username}:{hashed_password}\n")
    print("Registration successful!")
    return True
