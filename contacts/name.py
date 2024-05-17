from contacts.field import Field

class Name(Field):

    def __init__(self, name):
        self.value = name

    def __str__(self):
        return f"Name: {self.value}"    