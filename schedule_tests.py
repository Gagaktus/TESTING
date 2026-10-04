import pytest
from schedule import SCHEDULE, hours_in_day, is_correct_types, get_subjects


@pytest.fixture
def schedule():
    return SCHEDULE


class TestHoursInDay:
    @pytest.mark.parametrize(
        "day, expected",
        [
            ("понедельник", 3.5),
            ("вторник", 2),
            ("среда", 2),
            ("четверг", 0),
            ("пятница", 0),
            ("суббота", 0),
            ("воскресенье", 1),
        ],
    )
    def test_hours_in_day(self, schedule, day, expected):
        assert hours_in_day(schedule, day) == expected


class TestCorrectTypes:
    @pytest.mark.parametrize(
        "day, expected",
        [
            ("понедельник", True),
            ("вторник", True),
            ("среда", True),
            ("четверг", True),
            ("пятница", True),
            ("воскресенье", True),
        ],
    )
    def test_is_correct_types(self, schedule, day, expected):
        assert is_correct_types(schedule, day) == expected

    def test_saturday_skip(self, schedule):
        pytest.skip("Для субботы правила не заданы в спецификации")


class TestGetSubjects:
    @pytest.mark.parametrize(
        "day, expected",
        [
            ("понедельник", ["Математика", "Программирование", "История"]),
            ("вторник", ["Физика"]),
            ("среда", ["Базы данных"]),
            ("четверг", ["Английский язык"]),
            ("пятница", ["Программирование", "Математика"]),
            ("суббота", ["Проектная деятельность"]),
            ("воскресенье", ["День открытых дверей", "Математика"]),
        ],
    )
    def test_get_subjects(self, schedule, day, expected):
        assert get_subjects(schedule, day) == expected
