from students import add_student, validate_student, validate_email


def test_add_student():
    assert add_student([], "Asha") == ["Asha"]


def test_validate_student_valid():
    assert validate_student("Asha", 20) is True


def test_validate_student_invalid():
    assert validate_student("", 20) is False
    assert validate_student("Asha", 5) is False


def test_validate_email_valid():
    assert validate_email("asha@example.com") is True


def test_validate_email_invalid():
    assert validate_email("asha.example.com") is False
    assert validate_email("asha@example") is False
