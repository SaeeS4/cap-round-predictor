class College:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        return f"College(name={self.name}, departments={[dept.name for dept in self.departments]})"
