
#Student Grade/Assignment Tracker

#Project Overview

This project is a simple command-line Student Grade/Assignment Tracker built using Python 3.

The purpose of the program is to help students keep track of their homework and exam results in one place. Users can add assignments, view all their assignments, filter them based on different options, and see a summary of their grades.

All information is stored temporarily while the program is running. The program does not save the assignments to a file or database.

#it's Features

The Student Grade Tracker allows the user to:

- Add homework assignments
- Add exam assignments
- Enter the subject, title, score, maximum score, and due date
- View all recorded assignments
- Filter assignments by subject
- Filter assignments by assignment type
- Filter assignments by month
- View the overall grade average
- View the average grade for each subject
- See the highest-scoring assignment
- See the lowest-scoring assignment
- Handle invalid inputs and menu choices

#Project Structure

The project is divided into three main Python files:

- `main.py` - Contains the main menu and controls the interaction with the user.
- `assignment.py` - Contains the Assignment class and the Homework and Exam subclasses.
- `tracker.py` - Contains the GradeTracker class, which manages assignments, filtering, listing, and grade summaries.

#Object-Oriented Programming

The project uses Object-Oriented Programming (OOP).

The main `Assignment` class stores common information such as:

- Subject
- Title
- Score
- Maximum score
- Due date
- Assignment type

Two subclasses were created:

- `Homework`
- `Exam`

Both subclasses inherit from the `Assignment` class using inheritance and `super()`.

The `GradeTracker` class is responsible for managing the assignments and performing operations such as adding, listing, filtering, and calculating grade summaries.

#How to Run the Program

#the Requirements

- Python 3
- Visual Studio Code or another Python-compatible editor
- Git (if cloning the project from GitHub)

#Running the Program

1. Clone the repository from GitHub.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Make sure you are inside the project folder.
5. Run the following command:

```bash
python main.py

#The Student Grade Tracker menu will appear in the terminal.
#Menu Structure

#The program contains the following menu options:

===== STUDENT GRADE TRACKER =====
1) Add homework
2) Add exam
3) List assignments
4) Filter assignments
5) Show summary
0) Exit

#The user can choose an option by entering the corresponding number.

#Sample Interaction

#Example of adding a homework assignment:

===== STUDENT GRADE TRACKER =====
1) Add homework
2) Add exam
3) List assignments
4) Filter assignments
5) Show summary
0) Exit

Enter your choice: 1

Enter subject: Python
Enter title: Inheritance Assignment
Enter score: 40
Enter maximum score: 70
Enter due date: 2026-08-16

Homework added successfully!

#Example of the grade summary

===== GRADE SUMMARY =====

Overall Average: 68.33%

Per-Subject Averages:
Python: 57.14%
Cybersecurity: 84.00%

Highest Scoring Assignment:
SIEM Test: 84.00%

Lowest Scoring Assignment:
Inheritance Assignment: 57.14%

#Input Validation

#The program checks user input to reduce errors. For example, it checks that:

#Menu choices are valid.
#Scores are entered as numbers.
#The score does not exceed the maximum score.
#The maximum score is greater than zero.
#Assignment types are valid.
#The program handles cases where there are no assignments to display.
#Testing

#The program was tested by:

Adding homework assignments
Adding exam assignments
Listing assignments
Filtering assignments by type
Filtering assignments by subject
Filtering assignments by month
Displaying the grade summary
Testing invalid inputs

#The program was run several times during development to identify and fix errors.

#Conclusion
#This project helped me practise Python programming in a practical way. I was able to apply concepts such as classes, objects, inheritance, functions, loops, lists, conditionals, and input validation.

#It also helped me understand how different Python files can work together as one program. Building and testing the project gave me more confidence in writing and debugging Python code

#Thank you.