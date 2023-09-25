from lib.diary import *
import pytest

# Initially returns empty entry list
def test_initially_returns_empty_list():
    diary = Diary()
    assert diary.list_entries() == []

# Initially find_best_entry_for_reading_time raises error
def test_initially_find_best_entry_for_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.find_best_entry_for_reading_time(3, 5)
    assert str(e.value) == "No entries added yet"

# Initially list_todos() raises error
def test_list_todos_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.list_todos()
    assert str(e.value) == "No entries added yet"

# Initially list_phone_numbers raises error
def test_list_phone_numbers_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as e:
        diary.list_phone_numbers()
    assert str(e.value) == "No entries added yet"