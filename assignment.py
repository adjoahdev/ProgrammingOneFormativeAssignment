#adding assignnment

class Assignment:

    def __init__(self, subject, title, score, max_score, due_date, atype):

        self.subject = subject.lower().strip()

        self.title = title

        self.score = float(score)

        self.max_score = float(max_score)

        self.due_date = due_date

        self.type = atype


class Homework(Assignment):

    def __init__(self, subject, title, score, max_score, due_date):

        super().__init__(
            subject,
            title,
            score,
            max_score,
            due_date,
            "homework"
        )


class Exam(Assignment):

    def __init__(self, subject, title, score, max_score, due_date):
        super().__init__(
            subject,
            title,
            score,
            max_score,
            due_date,
            "exam"
        )


# Testing objects
homework1 = Homework(
    "Python",
    "Inheritance Assignment",
    40,
    70,
    "2026-08-15"
)

exam1 = Exam(
    "Cybersecurity",
    "SIEM Test",
    42,
    50,
    "2026-08-20"
)


# Test output
print(homework1.subject)

print(homework1.title)

print(homework1.score)

print(homework1.type)

print()

print(exam1.subject)

print(exam1.title)

print(exam1.score)

print(exam1.type)