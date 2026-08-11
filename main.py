
print("Student Grade/Assignment Tracker")

subject = input("Enter subject: ")

title = input("Enter assignment title: ")

score = float(input("Enter score: "))

max_score = float(input("Enter maximum score: "))

due_date = input("Enter due date: ")

print()

print("Assignment Information")

print("Subject:", subject)

print("Title:", title)

print("Score:", score)

print("Maximum Score:", max_score)

print("Due Date:", due_date)

if score > max_score:
    print("Error: Score cannot be greater than maximum score.")

else:
    percentage = (score / max_score) * 100

    print("Percentage:", percentage, "%")