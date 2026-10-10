import random
import string
password ={}

try:
 with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            password[website] = pwd
except :
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n---PASSWORD MANAGER---")
    print("1. Generate new password")
    print("2. Save password")
    print("3. Retrieve password")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "2":
        website = input("Enter the website name: ")
        pwd = input("Enter the password: ")
        password[website] = pwd
        with open("password.txt", "a") as file:
            file.write(f"{website}:{pwd}\n")
        print(f"Password for {website} saved.")

    elif choice == "3":
        if not password:
            print("No passwords saved yet.")
        else:
            print("Saved passwords:")
            for website, pwd in password.items():
                print(f"{website}: {pwd}")

    elif choice == "1":
        print("Generated password:", generate_password())

    elif choice == "4":
        print("Exiting the password manager.")
        break

    else:
        print("Invalid choice. Please try again.")


