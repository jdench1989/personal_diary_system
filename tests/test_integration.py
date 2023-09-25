from lib.diary import*
from lib.diary_entry import *

"""
Given a Diary
When we add an entry
We see that entry listed in the entry list
"""
def test_entry_added_to_entry_list():
    diary = Diary()
    entry1 = Entry("Title 1", "Contents 1")
    diary.add(entry1)
    assert diary.list_entries() == [("Title 1", "Contents 1")]

"""
Given a Diary
When we add multiple entries
We see all entries listed in the entry list
"""
def test_entry_added_to_entry_list():
    diary = Diary()
    entry1 = Entry("Title 1", "Contents 1")
    entry2 = Entry("Title 2", "Contents 2")
    diary.add(entry1)
    diary.add(entry2)
    assert diary.list_entries() == [("Title 1", "Contents 1"), ("Title 2", "Contents 2")]

"""
Given multiple entries
When given a number of words per minute and a number of minutes
Can select an entry that can be read in the given time
"""
def test_returns_best_entry_to_read_given_wpm_and_minutes():
    diary = Diary()
    entry_1 = Entry('Title1', 'These are the contents of entry one') #7
    entry_2 = Entry('Title2', 'These are the contents of entry two which are slightly longer than entry one')#14
    entry_3 = Entry('Title3', 'These are the contents of entry three which are even longer still compared to both entry one and two')#19
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(7,1) == ('Title1', 'These are the contents of entry one')
    assert diary.find_best_entry_for_reading_time(7,2) == ('Title2', 'These are the contents of entry two which are slightly longer than entry one')
    assert diary.find_best_entry_for_reading_time(7,3) == ('Title3', 'These are the contents of entry three which are even longer still compared to both entry one and two')

"""
Given multiple entries
Can select and return entires containing the phrase "#TODO"
"""
def test_returns_todo_list():
    diary = Diary()
    entry1 = Entry("Title 1", "Contents 1")
    entry2 = Entry("Title 2", "Contents 2 which are longer")
    entry3 = Entry("Title 3", "#TODO. Contents 3 which are even longer still")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.list_todos() == [(
        "Title 3", "#TODO. Contents 3 which are even longer still")]

"""
Given multiple entries
Can select and return a list of all phone numbers found across all entries
"""
def test_list_phone_numbers_returns_correctly():
    diary = Diary()
    entry1 = Entry("Title 1", "07802000000")
    entry2 = Entry("Title 2", "contains no number")
    entry3 = Entry("Title 3", "Contains the number 07802000001")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.list_phone_numbers() == ['07802000000', '07802000001']

"""
given multiple entires
list_phone_numbers selects and lists only phone numbers and ignores other numbers
i.e. must start with a 0 and be 11 digits long
"""
def list_phone_numbers_ignores_non_phone_number_numbers():
    diary = Diary()
    entry1 = Entry("Title 1", "07802000000")
    entry2 = Entry("Title 2", "0780200000000")
    entry3 = Entry("Title 3", "34567890123")
    entry4 = Entry("Title 4", "0 7 8 0 2 0 0 0 0 0 3")
    entry5 = Entry("Title 5", "0 563 word 1232 07802000001 another word")
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.list_phone_numbers() == ['07802000000', '07802000001']