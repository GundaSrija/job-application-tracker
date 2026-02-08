# Job Application Tracker - Day 1

applications = []

def add_application():
    company = input("Enter company name: ")
    role = input("Enter role: ")
    location = input("Enter location: ")

    application = {
        "company": company,
        "role": role,
        "location": location,
        "status": "Applied"
    }

    applications.append(application)
    print("✅ Application added successfully!")


def view_applications():
    if not applications:
        print("📭 No applications found.")
        return

    print("\n--- Your Applications ---")
    for index, app in enumerate(applications, start=1):
        print(f"\nApplication {index}")
        print(f"Company : {app['company']}")
        print(f"Role    : {app['role']}")
        print(f"Location: {app['location']}")
        print(f"Status  : {app['status']}")


def main_menu():
    while True:
        print("\n===== Job Application Tracker =====")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            print("👋 Exiting program. Good luck!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


main_menu()
