import random
import string


password_database = []

while True:
    print("\n========================")
    print("    PASSWORD MANAGER    ")
    print("========================")
    print("1. Add a Password")
    print("2. View Passwords")
    print("3. Exit")
    print("========================")
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        website = input("Enter Website: ").strip()
        username = input("Enter Username: ").strip()
        password = input("Enter Password (leave blank to auto-generate): ").strip()
        
        if not password:
            pool = string.ascii_letters + string.digits + "!@#$"
            password = "".join(random.choice(pool) for i in range(12))
            print(f"Generated Password: {password}")
            
        if website and username:
            
            record = {"website": website, "username": username, "password": password}
            password_database.append(record)
            print("Successfully saved!")
        else:
            print("Error: Website and Username cannot be empty.")
            
    elif choice == "2":
        print("\n" + "-"*50)
        print(f"{'WEBSITE':<15}{'USERNAME':<20}{'PASSWORD':<15}")
        print("-"*50)
        
        if not password_database:
            print("No passwords saved yet.")
        else:
            
            for record in password_database:
                print(f"{record['website']:<15}{record['username']:<20}{record['password']:<15}")
        print("-"*50)
        
    elif choice == "3":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice, please try again.")
      
