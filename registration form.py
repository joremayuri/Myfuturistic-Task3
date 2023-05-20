import csv

def get_registration_data():
    """Get registration data from the user."""
    print("Please enter the following information:")
    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    address = input("Address: ")
    year = input("Year: ")
    branch = input("Branch: ")
    return name, email, phone, address , year,branch

def save_registration_data(name, email, phone, address,year,branch):
    """Save registration data to a local file."""
    with open("registrations.csv", mode="a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, email, phone, address,year , branch])

def main():
    """Main function to manage registration forms."""
    while True:
        print("\nWelcome to the Exam Registration Form!\n")
        choice = input("Do you want to register for the exam? (yes or no): ")
        if choice.lower() == "yes":
            name, email, phone, address , year,branch = get_registration_data()
            save_registration_data(name, email, phone, address,year,branch)
            print("Registration Successful!")
        elif choice.lower() == "no":
            print("Thank you for visiting the Exam Registration Form.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
