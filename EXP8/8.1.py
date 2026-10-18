class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


class UgStudent(Student):
    def __init__(self, name, age, course, semester):
        super().__init__(name, age, course)
        self.semester = semester

    def display_info(self):
        super().display_info()
        print("Semester:", self.semester)


class PgStudent(Student):
    def __init__(self, name, age, course, thesis_topic):
        super().__init__(name, age, course)
        self.thesis = thesis_topic

    def display_info(self):
        super().display_info()
        print("Thesis Topic:", self.thesis)


student1 = UgStudent(
    "Shinchan",
    20,
    "B.Tech Data Science",
    4
)

student2 = PgStudent(
    "Nobita",
    21,
    "B.Tech Computer Engineering",
    "Artificial Intelligence"
)


print("Undergraduate students:")
student1.display_info()

print("\nPostgraduate Student:")
student2.display_info()

