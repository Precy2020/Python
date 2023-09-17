class Entry:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.identity = 0

    def findEntryById(self, identity):
        if identity == self.identity:
            return self
        else:
            return None

    def updateEntry(self, identity, title, body):
        if self.identity == identity:
            self.title = title
            self.body = body

    
