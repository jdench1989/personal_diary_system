Diary System Multi-Class Planned Design Recipe

1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com


  ┌───────────────────────────────────────────┐
  │ Diary()                                   │
  │                                           │
  │ entries_list [property]                   │
  │                                           │
  │ add_entry(title, contents)                │
  │                                           │
  │ list_entries()                            │
  │                                           │
  │ best_entry_for_reading_time(wpm, minutes) │
  │                                           │
  │ list_todos()                              │
  │                                           │
  │ list_phone_numbers()                      │
  └─────┬─────────────────────────────────────┘
        │
        │  Diary() calls on and stores multiple instances of Entry()
        │
        ▼
  ┌───────────────────────────────┐
  │Entry(title, contents)         │
  │                               │
  │count_words()                  │
  │                               │
  │reading_time()                 │
  │                               │
  └───────────────────────────────┘

Also design the interface of each class in more detail.

class Diary():
    #User-facing properties
    # entries = a list of instances of Entry(), each including a title and contents

    def __init__(self):
        pass

    def add(self, title, contents):
        Parameters:
            title: title of the entry (string)
            contents: contents of the entry (string)
        Effects:
            Creates an isntance of the Entry() class and stores it in the entries list

    def list_entries(self):
        Parameters:
            None
        Effects:
            List all entries in entries list

    def best_entry_for_reading_time(wpm, minutes):
        Parameters:
            wpm: number of words the user can read in a minute (int)
            minutes: number of minutes the user has available to read (int)

    def list_todos():
        Parameters:
            None
        Effect:
        returns a list of all diary entries containing the phrase "#TODO"

    def list_phone_numbers():
        Parameters:
            None
        Effect:
            Creates and returns a list of phone numbers found in the entries list


class Entry():
    #User-facing properties
        title: title of the entry
        contents: contents of the entry

    def count_words():
        parameters: 
            None
        effect:
            Returns the number of words in the diary entry

    def reading_time(wpm):
        parameters:
            wpm: number of words per minute the user can read (int)
        effect:
            calls the count_words method and returns the number of minutes it would take for the user to read this entry (int)


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

"""
Given a Diary
When we add an entry
We see that entry listed in the entry list
"""
diary = Diary()
entry1 = Entry("Title 1", "Contents 1")
diary.add(entry1)
diary.list_entries() => [(Title 1, Contents1)]

"""
Given a Diary
When we add multiple entries
We see all entries listed in the entry list
"""
diary = Diary()
entry1 = Entry("Title 1", "Contents 1")
entry2 = Entry("Title 2", "Contents 2")
diary.add(entry1)
diary.add(entry2)
diary.list_entries() => [("Title 1", "Contents1"), ("Title 2", "Contents 2")]

"""
Given multiple entries
When given a number of words per minute and a number of minutes
Can select an entry that can be read in the given time
"""
diary = Diary()
entry1 = Entry("Title 1", "Contents 1")
entry2 = Entry("Title 2", "Contents 2 which are longer")
entry3 = Entry("Title 3", "Contents 3 which are even longer still")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.best_entry_for_reading_time(wpm, minutes) => the longest entry that can be read in the given time

"""
Given multiple entries
Can select and return entires containing the phrase "#TODO"
"""
diary = Diary()
entry1 = Entry("Title 1", "Contents 1")
entry2 = Entry("Title 2", "Contents 2 which are longer")
entry3 = Entry("Title 3", "#TODO. Contents 3 which are even longer still")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.list_todos() => ("Title 3", "#TODO. Contents 3 which are even longer still")

"""
Given multiple entries
Can select and return a list of all phone numbers found across all entries
"""
diary = Diary()
entry1 = Entry("Title 1", "Contents 1 contains the number 07802000000")
entry2 = Entry("Title 2", "Contents 2 contains no number")
entry3 = Entry("Title 3", "Contents 3 07802000001 <- contains this number")
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.list_phone_numbers() => ['07802000000', '07802000001']


5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.