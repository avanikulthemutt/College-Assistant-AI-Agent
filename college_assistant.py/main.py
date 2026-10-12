
# College Assistant AI Agent

def show_subjects():
    print("\nAvailable Subjects:")
    print("1. Python Programming")
    print("2. Database Management Systems")
    print("3. Computer Networks")
    print("4. Operating Systems")
    print("5. Data Structures and Algorithms")


def study_tips():
    print("\nStudy Tips:")
    print("1. Study in small sessions.")
    print("2. Practice previous question papers.")
    print("3. Revise important topics daily.")
    print("4. Take short breaks while studying.")


def create_study_plan():
    subject = input("Enter the subject: ")
    hours = int(input("Hours available per day: "))

    if hours <= 0:
        print("Please enter a positive number of hours.")
        return

    print(f"\nStudy Plan for {subject}:")
    print(f"1. Learn concepts - {hours // 2} hour(s)")
    print("2. Practice questions")
    print("3. Revise important topics")
    print("4. Take a short break between sessions")


def show_timetable():
    print("\nSample College Timetable:")
    print("09:00 AM - Python Programming")
    print("10:00 AM - Database Management")
    print("11:00 AM - Computer Networks")
    print("12:00 PM - Lunch Break")
    print("01:00 PM - Operating Systems")
    print("02:00 PM - Data Structures")


def main():
    print("===================================")
    print("      COLLEGE ASSISTANT AGENT")
    print("===================================")

    name = input("Enter your name: ")

    while True:
        print(f"\nHello, {name}! How can I help you?")
        print("1. View Subjects")
        print("2. Get Study Tips")
        print("3. Create Study Plan")
        print("4. View Timetable")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_subjects()
        elif choice == "2":
            study_tips()
        elif choice == "3":
            create_study_plan()
        elif choice == "4":
            show_timetable()
        elif choice == "5":
            print("Good luck with your studies!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
