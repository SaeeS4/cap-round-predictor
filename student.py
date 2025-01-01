class Student:
    def __init__(self, name, percentage, test_score):
        self.name = name
        self.percentage = percentage
        self.test_score = test_score

    def __str__(self):
        return f"Student(name={self.name}, percentage={self.percentage}, test_score={self.test_score})"
