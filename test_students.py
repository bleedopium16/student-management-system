from students import add_student, validate_student


def test_add_student():
    assert add_student([], "Asha") == ["Asha"]


def test_validate_student_valid():
    assert validate_student("Asha", 20) is True


def test_validate_student_invalid():
    assert validate_student("", 20) is False
    assert validate_student("Asha", 5) is False
