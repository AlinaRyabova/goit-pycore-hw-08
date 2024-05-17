from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def __str__(self):
        contacts_str = ", ".join(str(record) for record in self.data.values())
        return f"AddressBook: {contacts_str}"    

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]    

    def get_upcoming_birthdays(self, days=7):
        today = datetime.now()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.replace(year=today.year)
                if birthday < today:
                    birthday = birthday.replace(year=today.year + 1)
                if (birthday - today).days <= days:
                    upcoming_birthdays.append((record.name.value, birthday.strftime('%d.%m.%Y')))
        return upcoming_birthdays

    def birthdays(self):
        upcoming_birthdays = self.get_upcoming_birthdays()
        if upcoming_birthdays:
            print("Upcoming birthdays:")
            for name, birthday in upcoming_birthdays:
                birthday_str = birthday.strftime('%d.%m.%Y')
                print(f"{name} birthday: {birthday_str}")
        else:
            print("No upcoming birthdays.")

def add_birthday(self, args):
        if len(args) != 2:
            return "Invalid number of arguments. Usage: add-birthday name date"
        name, date = args
        record = self.find(name)
        if record:
            record.add_birthday(date)  
            return f"Birthday added for {name}" 
        else:
            return f"Contact {name} not found." 

def show_birthday(self, args):
        if len(args) != 1:
            return "Invalid number of arguments. Usage: show-birthday name"
        name = args[0]
        record = self.find(name)
        if record and record.birthday:
            return f"{name} birthday: {record.birthday.value.strftime('%d.%m.%Y')}" 
        else:
            return f"Contact {name} not found or birthday is not set."        