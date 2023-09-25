from lib.diary_entry import *

# Given a title and contents
# Initializes with self.title and self.contents values stored
def test_initializes_with_title_and_contents_stored():
    entry = Entry('Title1', 'Contents1')
    assert entry.title == 'Title1'
    assert entry.contents == 'Contents1'

# Given an entry 
# Returns the correct number of words in the entry
def test_returns_no_of_words_for_entry():
    entry = Entry('Test Title', 'These are the contents')
    assert entry.count_words() == 4

# Given a wpm value and some contents
# Returns the number of minutes require dto read the entry
def test_returns_reading_time_in_minutes():
    entry = Entry('Test Title', 'These are the contents')
    assert entry.reading_time(2) == 2