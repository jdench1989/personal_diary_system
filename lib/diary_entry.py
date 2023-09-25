class Entry():

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def count_words(self):
        words = self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        word_count = self.count_words()
        return word_count/wpm