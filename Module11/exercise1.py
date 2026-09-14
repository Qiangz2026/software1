class Publication:#define baseclass
    def __init__(self, name):
        self.name = name

class Book(Publication):#define subclass and initialize it
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):#Print all information of a book
        print(f"Name: {self.name}\nAuthor: {self.author}\nPage_count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"Name: {self.name}\nChief_editor: {self.chief_editor}")