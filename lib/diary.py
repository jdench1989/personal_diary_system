from lib.diary_entry import *
import re

class Diary():

    def __init__(self):
        self.entry_list = []

    def add(self, entry):
        self.entry_list.append(entry)

    def list_entries(self):
        return [(entry.title, entry.contents) for entry in self.entry_list]
    
    def list_todos(self):
        if self.entry_list == []:
            raise Exception("No entries added yet")
        else:
            return [(entry.title, entry.contents) for entry in self.entry_list if "#TODO" in entry.contents]
        
    def list_phone_numbers(self):
        if self.entry_list == []:
            raise Exception("No entries added yet")
        else:
            phone_numbers = []
            for entry in self.entry_list:
                phone_numbers += re.findall(r'\b0[0-9]{10}\b', entry.contents)
            return phone_numbers
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self.entry_list == []:
            raise Exception("No entries added yet")
        else:
            return max([(entry.title, entry.contents) for entry in self.entry_list if (entry.reading_time(wpm) <= minutes)])
        
    