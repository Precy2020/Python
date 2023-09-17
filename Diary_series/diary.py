from Diary_series.custom_exception import IncorrectPassword
from Diary_series.entry import Entry


class Diary:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isLocked = True
        self.entries = []

    def unlockDiary(self, password):
        if self.password == password:
            self.isLocked = False
            return self.isLocked
        return self.isLocked

    def locked(self):
        return self.isLocked

    def createEntry(self, title, body):
        entry = Entry(title, body)
        self.entries.append(entry)

    def deleteEntry(self, identity):
        entry = self.findEntryById(identity)
        if entry is not None:
            self.entries.remove(entry)
        else:
            raise ValueError("There's nothing here")

    def findEntryById(self, identity):
        for entry in self.entries:
            found_entry = entry.findEntryById(identity)
            if found_entry is not None:
                return found_entry
        raise ValueError("There's nothing here!")

    def updateEntry(self, identity, title, body):
        for entry in self.entries:
            entry.updateEntry(identity, title, body)

