class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
                return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {_average(self.grades)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
                    
class Lecturer(Mentor):
    grades = {}
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {_average(Lecturer.grades)}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
    
def _average(grades):
    for element in grades.values():
        avgerage = sum(element)/len(element)
    return avgerage
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Python', 9)
 

cool_lecturer = Lecturer('Vasya', 'Pupkin')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 5)

print(best_student)