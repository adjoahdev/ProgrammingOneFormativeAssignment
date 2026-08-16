#tracking assignment


class GradeTracker:

    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):

        self.assignments.append(assignment)

    def list_assignments(self):

        if not self.assignments:

            print("No assignments found.")
            return

        print("\n===== ASSIGNMENTS =====")

        for number, assignment in enumerate(self.assignments, start=1):

            print(f"\n{number}. {assignment.subject.title()} - {assignment.title}")

            print(f"   Score: {assignment.score}/{assignment.max_score}")

            print(f"   Due Date: {assignment.due_date}")

            print(f"   Type: {assignment.type.title()}")




#filter assignment 

    def filter_assignments(self, filter_type, value):
        results = []

        for assignment in self.assignments:

            if filter_type == "type":

                if assignment.type.lower() == value.lower():

                    results.append(assignment)

            elif filter_type == "subject":

                if assignment.subject.lower() == value.lower():

                    results.append(assignment)

            elif filter_type == "month":

                if assignment.due_date.startswith(value):

                    results.append(assignment)

        if not results:

            print("No matching assignments found.")
            return

        print("\n===== FILTERED ASSIGNMENTS =====")

        for number, assignment in enumerate(results, start=1):

            print(f"\n{number}. {assignment.subject.title()} - {assignment.title}")

            print(f"   Score: {assignment.score}/{assignment.max_score}")

            print(f"   Due Date: {assignment.due_date}")

            print(f"   Type: {assignment.type.title()}")





 # Showing the summary of grades.

    def show_summary(self):

        if not self.assignments:

            print("No assignments available.")
            return


        # Calculating the overall average

        total_score = 0

        total_max_score = 0

        for assignment in self.assignments:

            total_score = total_score + assignment.score

            total_max_score = total_max_score + assignment.max_score

        overall_average = (total_score / total_max_score) * 100

        print("\n===== GRADE SUMMARY =====")

        print(f"Overall Average: {overall_average:.2f}%")





        # Calculating the average for each subject

        subjects = {}

        for assignment in self.assignments:

            subject = assignment.subject

            if subject not in subjects:

                subjects[subject] = [0, 0]

            subjects[subject][0] = subjects[subject][0] + assignment.score

            subjects[subject][1] = subjects[subject][1] + assignment.max_score

        print("\nPer-Subject Averages:")

        for subject in subjects:

            score = subjects[subject][0]

            max_score = subjects[subject][1]

            average = (score / max_score) * 100

            print(f"{subject.title()}: {average:.2f}%")
            



        # Find highest and lowest scoring assignments
        
        highest = self.assignments[0]

        lowest = self.assignments[0]

        for assignment in self.assignments:

            current_percentage = (assignment.score / assignment.max_score) * 100

            highest_percentage = (highest.score / highest.max_score) * 100

            lowest_percentage = (lowest.score / lowest.max_score) * 100

            if current_percentage > highest_percentage:
                highest = assignment

            if current_percentage < lowest_percentage:
                lowest = assignment

        print("\nHighest Scoring Assignment:")

        print(f"{highest.title}: {(highest.score / highest.max_score) * 100:.2f}%")

        print("\nLowest Scoring Assignment:")

        print(f"{lowest.title}: {(lowest.score / lowest.max_score) * 100:.2f}%")


