import pytest
from schedule import SCHEDULE, hours_in_day, is_correct_types, get_subjects

@pytest.fixture
def account():
    return SCHEDULE

def 