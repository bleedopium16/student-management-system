def add_student(students, name):
    students.append(name)
    return students


def validate_student(name, age):
    return bool(name.strip()) and 17 <= age <= 30
