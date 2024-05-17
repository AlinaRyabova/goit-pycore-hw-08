from contacts.decorators import input_error
from contacts.address_book import AddressBook
from contacts.record import Record

@input_error
def add_contact(args, book: AddressBook) -> str:
    if len(args) == 0:
        name = input("Enter the name for the contact: ")
        phone = input("Enter the phone number for the contact: ")
    elif len(args) == 1:
        name = args[0]
        phone = input("Enter the phone number for the contact: ")
    elif len(args) == 2:
        name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    else:
        message = "Contact's phone updated"
    record.add_phone(phone)
    return message


def change_contact(args, book: AddressBook):
    if len(args) != 3:
        return "Invalid number of arguments. Usage: change name old_number new_number"
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "Contact does not exist, you can add it"
    if record.find_phone(old_phone) is None:
        return "Old phone not found"
    record.edit_phone(old_phone, new_phone)
    return "Phone changed"
 
@input_error
def show_phone(args, book: AddressBook):
    if len(args) != 1:
        return "Invalid phone of arguments. Usage: phone name"
    name = args[0]
    record = book.find(name)
    if record is None:
        return "No contact, please add it"
    return [p.value for p in record.phones]   



