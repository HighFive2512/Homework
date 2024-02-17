class Class:
    __students_count = 22
    def __init__(self,name):
        self.students,self.grades = [],[]
        self.name = name
    def add_student(self,name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)
    def get_average_grade(self) -> str:
        return float("{:.2f}".format(sum(self.grades) / len(self.students)))
    def __repr__(self):
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {average_grade}"