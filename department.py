class Department:
    def __init__(self, name, min_percentage, min_test_score):
        self.name = name
        self.min_percentage = min_percentage
        self.min_test_score = min_test_score

    def __str__(self):
        return f"Department(name={self.name}, min_percentage={self.min_percentage}, min_test_score={self.min_test_score})"
