from students import add_student


def test_add_student():
    assert add_student([], "Asha") == ["Asha"]
