# from .text import*
import text
import model

def menu()-> int:
    print (text.main_menu)
    while True:
        choice = input(text.menu_choice)
        if choice.isdigit() and 0 < int(choice)< 9:
            return int(choice)
        print (text.input_error)

def show_contacts(book: list[dict[str, str]]):
    if book:
        print('\n' + '='*67)  
        for contact in book:
            # uid, name, phone, comment = contact.values()
            uid=contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')    
            print(f'{uid:>3}. {name: <20} {phone:<20} {comment: <20}')
        print('='*67 + '\n')
    else:
        print(text.book_error)  

def print_message(message: str):
    length=len(message)
    print('\n' + '='*length)
    print(message)
    print('='*length + '\n')

def input_contact(message: str) -> dict[str, str]:
    print(message)
    name = input(text.new_contact[0])
    phone = input(text.new_contact[1])  
    comment = input(text.new_contact[2])
    index = model.check_id()
    index = str(index)
    return {'id': index, 'name': name, 'phone':phone, 'comment': comment}

def input_changed_contact(message: str) -> dict[str, str]:
    print(message)
    name = input(text.new_contact[0])
    phone = input(text.new_contact[1])  
    comment = input(text.new_contact[2])
    return {'name': name, 'phone':phone, 'comment': comment}
  
def input_return (message: str) ->str:
    return input(message)

