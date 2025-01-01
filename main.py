from student import Student
from department import Department
from College import College
from predictor import CollegeAdmissionPredictor

def get_student_details():
    print("Enter the following details to predict your college admission chances.")
    try:
        name = input("Name: ")
        percentage = float(input("Percentage: "))
        test_score = float(input("Test Score (out of 1600): "))
        return Student(name, percentage, test_score)
    except ValueError:
        print("Invalid input. Please enter numeric values for percentage and test score.")
        return get_student_details()

def main():
    student = get_student_details()

    # Example departments
    departments = {
        "Computer Engineering": Department("Computer Engineering", 80, 1300),
        "Mechanical Engineering": Department("Mechanical Engineering", 75, 1200),
        "Civil Engineering": Department("Civil Engineering", 70, 1100),
        "Electrical Engineering": Department("Electrical Engineering", 78, 1250),
        "Chemical Engineering": Department("Chemical Engineering", 82, 1350),
        "Aerospace Engineering": Department("Aerospace Engineering", 85, 1400),
        "Biomedical Engineering": Department("Biomedical Engineering", 88, 1450),
        "Industrial Engineering": Department("Industrial Engineering", 77, 1220),
        "Environmental Engineering": Department("Environmental Engineering", 80, 1280),
        "Materials Science Engineering": Department("Materials Science Engineering", 83, 1320),
        "Nuclear Engineering": Department("Nuclear Engineering", 84, 1330),
        "Software Engineering": Department("Software Engineering", 81, 1290),
        "Information Technology": Department("Information Technology", 79, 1260),
        "Automobile Engineering": Department("Automobile Engineering", 76, 1230),
        "Instrumentation Engineering": Department("Instrumentation Engineering", 80, 1250),
        "Production Engineering": Department("Production Engineering", 78, 1240),
        "Biotechnology Engineering": Department("Biotechnology Engineering", 83, 1340)
    }

    # Example colleges and their departments
    colleges = [
        College("IIT Bombay", [departments["Computer Engineering"], departments["Electrical Engineering"], departments["Mechanical Engineering"], departments["Materials Science Engineering"], departments["Nuclear Engineering"], departments["Biotechnology Engineering"]]),
        College("VNIT", [departments["Chemical Engineering"], departments["Computer Engineering"], departments["Software Engineering"], departments["Civil Engineering"], departments["Mechanical Engineering"]]),
        College("COEP", [departments["Civil Engineering"], departments["Aerospace Engineering"], departments["Environmental Engineering"], departments["Mechanical Engineering"], departments["Automobile Engineering"]]),
        College("MIT-WPU", [departments["Electrical Engineering"], departments["Mechanical Engineering"], departments["Biomedical Engineering"], departments["Production Engineering"], departments["Computer Engineering"]]),
        College("VIT", [departments["Chemical Engineering"], departments["Biomedical Engineering"], departments["Industrial Engineering"], departments["Information Technology"], departments["Mechanical Engineering"]]),
        College("DY Patil", [departments["Aerospace Engineering"], departments["Mechanical Engineering"], departments["Industrial Engineering"], departments["Computer Engineering"], departments["Instrumentation Engineering"]]),
        College("PCCOE", [departments["Biomedical Engineering"], departments["Computer Engineering"], departments["Environmental Engineering"], departments["Civil Engineering"], departments["Information Technology"]]),
        College("AVCOE", [departments["Biomedical Engineering"], departments["Computer Engineering"], departments["Environmental Engineering"], departments["Mechanical Engineering"], departments["Automobile Engineering"]]),
        College("Sanjivani", [departments["Biomedical Engineering"], departments["Computer Engineering"], departments["Environmental Engineering"], departments["Electrical Engineering"], departments["Civil Engineering"]]),
        College("Pravara Institute", [departments["Biomedical Engineering"], departments["Computer Engineering"], departments["Environmental Engineering"], departments["Mechanical Engineering"], departments["Chemical Engineering"]])
    ]

    try:
        print("Choose a college:")
        for i, college in enumerate(colleges, 1):
            print(f"{i}. {college.name}")

        college_choice = int(input("Enter the number corresponding to your choice: "))
        chosen_college = colleges[college_choice - 1]

        print("Choose a department:")
        for i, dept in enumerate(chosen_college.departments, 1):
            print(f"{i}. {dept.name}")

        dept_choice = int(input("Enter the number corresponding to your choice: "))
        chosen_department = chosen_college.departments[dept_choice - 1]

        predictor = CollegeAdmissionPredictor(student, chosen_college, chosen_department)
        predictor.display_prediction()

    except IndexError:
        print("Invalid choice. Please try again.")
        main()
    except ValueError:
        print("Invalid input. Please enter a number.")
        main()

if __name__ == "__main__":
    main()

