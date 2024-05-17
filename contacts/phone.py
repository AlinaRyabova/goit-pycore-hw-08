from contacts.field import Field

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number")
        super().__init__(value)

    def validate_phone(self, value):
        return len(value) == 10 and value.isdigit() 

    def __str__(self):
        return self.value  