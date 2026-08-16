
# main.py

from assignment import Homework, Exam
from tracker import GradeTracker


# Create the grade tracker
tracker = GradeTracker()


# Getting a valid score

def get_score():
    while True:
        try:
            score = float(input("Enter score: "))

            if score < 0:
                print("Score cannot be negative.")
            else:
                return score

        except ValueError:
            print("Invalid score. Please enter a number.")


# Getting a valid maximum score

def get_max_score():
    while True:
        try:
            max_score = float(input("Enter maximum score: "))

            if max_score <= 0:

                print("Maximum score must be greater than 0.")
            else:
                return max_score

        except ValueError:
            print("Invalid maximum score. Please enter a number.")



# Make sure the score does not exceed the maximum score

def get_valid_scores():
    while True:

        score = get_score()

        max_score = get_max_score()

        if score > max_score:

            print("Score cannot be greater than the maximum score.")

        else:
            return score, max_score



#  the main program loop

while True:

    print("\n===== STUDENT GRADE TRACKER =====")

    print("1) Add homework")

    print("2) Add exam")

    print("3) List assignments")

    print("4) Filter assignments")

    print("5) Show summary")

    print("0) Exit")

    choice = input("\nEnter your choice: ")



    # Adding homework

    if choice == "1":

        print("\n===== ADD HOMEWORK =====")

        subject = input("Enter subject: ")

        title = input("Enter assignment title: ")

        score, max_score = get_valid_scores()

        due_date = input("Enter due date (YYYY-MM-DD): ")

        homework = Homework(
            subject,
            title,
            score,
            max_score,
            due_date
        )

        tracker.add_assignment(homework)

        print("Homework added successfully!")



    # Adding exam
    elif choice == "2":

        print("\n===== ADD EXAM =====")

        subject = input("Enter subject: ")

        title = input("Enter exam title: ")

        score, max_score = get_valid_scores()

        due_date = input("Enter due date (YYYY-MM-DD): ")

        exam = Exam(
            subject,
            title,
            score,
            max_score,
            due_date
        )

        tracker.add_assignment(exam)

        print("Exam added successfully!")




    # Listing assignments

    elif choice == "3":

        tracker.list_assignments()



    # Filtering assignments

    elif choice == "4":

        print("\n===== FILTER ASSIGNMENTS =====")

        print("1) Filter by type")

        print("2) Filter by subject")

        print("3) Filter by month")

        filter_choice = input("\nChoose a filter: ")




        # Filter by type

        if filter_choice == "1":

            value = input("Enter type (homework/exam): ")

            tracker.filter_assignments(
                "type",
                value
            )


        # Filter by subject

        elif filter_choice == "2":

            value = input("Enter subject: ")

            tracker.filter_assignments(
                "subject",
                value
            )


        # Filter by month

        elif filter_choice == "3":

            value = input("Enter month (YYYY-MM): ")

            tracker.filter_assignments(
                "month",
                value
            )


        else:

            print("Invalid filter choice.")



    # Show grade summary
    elif choice == "5":

        tracker.show_summary()




    # Exit program

    elif choice == "0":

        print("\nThank you for using the Student Grade Tracker!")
        break


    # Invalid main menu choice

    else:

        print("\nInvalid choice. Please choose a number from 0 to 5.")
        