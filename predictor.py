class CollegeAdmissionPredictor:
    def __init__(self, student, college, department):
        self.student = student
        self.college = college
        self.department = department
        self.score = 0

    def calculate_score(self):
        # Percentage contribution
        if self.student.percentage >= 90:
            self.score += 50
        elif self.student.percentage >= 80:
            self.score += 40
        elif self.student.percentage >= 70:
            self.score += 30
        else:
            self.score += 20

        # Test score contribution
        if self.student.test_score >= 1400:
            self.score += 50
        elif self.student.test_score >= 1200:
            self.score += 40
        elif self.student.test_score >= 1000:
            self.score += 30
        else:
            self.score += 20

    def predict_admission(self):
        self.calculate_score()
        if self.student.percentage >= self.department.min_percentage and self.student.test_score >= self.department.min_test_score:
            if self.score >= 90:
                return "High"
            elif self.score >= 70:
                return "Medium"
            else:
                return "Low"
        else:
            return "Low"

    def display_prediction(self):
        admission_chances = self.predict_admission()
        print(f"Hello {self.student.name}, your chances of college admission to the {self.department.name} department at {self.college.name} are: {admission_chances}")
