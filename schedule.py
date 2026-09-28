SCHEDULE = [
    {
        "day": "понедельник",
        "time": "09:00",
        "hours": 2,
        "subject": "Математика",
        "type": "лекция",
    },
    {
        "day": "понедельник",
        "time": "11:00",
        "hours": 2,
        "subject": "Программирование",
        "type": "практика",
    },
    {
        "day": "понедельник",
        "time": "13:30",
        "hours": 1.5,
        "subject": "История",
        "type": "лекция",
    },
    {
        "day": "вторник",
        "time": "09:00",
        "hours": 2,
        "subject": "Физика",
        "type": "лекция",
    },
    {
        "day": "вторник",
        "time": "11:00",
        "hours": 2,
        "subject": "Физика",
        "type": "практика",
    },
    {
        "day": "среда",
        "time": "09:00",
        "hours": 2,
        "subject": "Базы данных",
        "type": "лекция",
    },
    {
        "day": "четверг",
        "time": "10:00",
        "hours": 3,
        "subject": "Английский язык",
        "type": "практика",
    },
    {
        "day": "пятница",
        "time": "09:00",
        "hours": 2,
        "subject": "Программирование",
        "type": "лабораторная",
    },
    {
        "day": "пятница",
        "time": "11:00",
        "hours": 2,
        "subject": "Математика",
        "type": "практика",
    },
    {
        "day": "суббота",
        "time": "10:00",
        "hours": 2,
        "subject": "Проектная деятельность",
        "type": "мероприятие",
    },
    {
        "day": "воскресенье",
        "time": "12:00",
        "hours": 3,
        "subject": "День открытых дверей",
        "type": "мероприятие",
    },
    {
        "day": "воскресенье",
        "time": "16:00",
        "hours": 1,
        "subject": "Математика",
        "type": "лекция",
    },
]


def hours_in_day(schedule, day):
    total = 0
    for lesson in schedule:
        if lesson["day"] == day and lesson["type"] == "лекция":
            total += lesson["hours"]
    return total


def is_correct_types(schedule, day):
    weekdays = ("понедельник", "вторник", "среда", "четверг")
    if day in weekdays:
        allowed = ("лекция", "практика")
    elif day == "воскресенье":
        allowed = ("мероприятие", "лекция")
    else:
        return True

    for lesson in schedule:
        if lesson["day"] == day and lesson["type"] not in allowed:
            return False
    return True


def get_subjects(schedule, day):
    subjects = []
    for lesson in schedule:
        if lesson["day"] == day and lesson["subject"] not in subjects:
            subjects.append(lesson["subject"])
    return subjects
