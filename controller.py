# from view import menu, show_contacts, print_message, input_contact, input_return
# import model 
# from view import text
import console
import text
import model

def start():
    while True:
        choice = console.menu()
        # model.open_file()
        match choice:
            case 1:
                model.open_file()
                print(model.phone_book)
                console.print_message(text.open_successful)
            case 2:
                # pass
                model.change_file(model.phone_book)
                console.print_message(text.file_is_saved)
            case 3:
                # pass
                console.show_contacts(model.phone_book)               
            case 4:
                # pass
                new = console.input_contact (text.input_new_contact)
                model.add_contact(new)
                console.print_message(text.contact_saved(new.get('name')))
            case 5:
                # pass
                word = console.input_return(text.search_word)
                result = model.search(word)
                console.show_contacts(result)
            case 6:
                pass
                word = console.input_return(text.search_word)
                result = model.search(word)
                console.show_contacts(result)
                index = console.input_return(text.input_index)
                new = console.input_changed_contact(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.phone_book[int(index)-1].get('name')
                console.print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))              
            case 7:
                # pass
                word = console.input_return(text.search_word)
                result = model.search(word)
                console.show_contacts(result)        
                index = console.input_return(text.input_deleted_index)
                deleted_name=model.phone_book[int(index)-1].get('name')
                model.delete_contact(int(index))
                console.print_message(text.contact_deleted(deleted_name))
            case 8:
                break


    
