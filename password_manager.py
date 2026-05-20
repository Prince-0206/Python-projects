import random
import string

passwords = {}

try:    
    with open("passwords.txt", "r") as file:
        for line in file:
            service, password = line.strip().split(":")
            passwords[service] = password
except FileNotFoundError:pass
 
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def save_password(service, password):
    passwords[service] = password
    with open("passwords.txt", "a") as file:
        file.write(f"{service}:{password}\n")

def get_password(service):
    return passwords.get(service, "No password found for this service.")
def main(): 
    while True:
        print("\nPassword Manager")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. Get Password")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        
        elif choice == "2":
            service = input("Enter service name: ")
            password = input("Enter password: ")
            save_password(service, password)
            print("Password saved successfully.")
        
        elif choice == "3":
            service = input("Enter service name: ")
            password = get_password(service)
            print(f"Password for {service}: {password}")
        
        elif choice == "4":
            print("Exiting Password Manager.")
            break
        
        else:
            print("Invalid choice. Please try again.")  
if __name__ == "__main__":
    main()