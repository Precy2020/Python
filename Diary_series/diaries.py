from Diary_series.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def findByUsername(self, username):
        for search in self.diaries:
            if search.getUsername() == username:
                return search
        return None

    def deleteDiary(self, username, password):
        self.diaries = [diary for diary in self.diaries if not (diary.getUsername() == username and diary.getPassword() == password)]
