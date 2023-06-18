phone_book=[]
# path = 'phones.txt'
path = r"C:\Users\Angelika\Documents\Docum_2022\Geekbrain\Course_2\Python\Phone_book\phones.txt"

def open_file():
    if not phone_book:
        with open (path, 'r', encoding='UTF-8') as file:
            data = file.readlines()     
            for contact in data:
                user_id, name, phone, comment, *_ = contact.strip().split(':')
                phone_book.append({'id':user_id, 'name':name, 'phone':phone, 'comment':comment})
        # data.close()
    return phone_book
    # print(phone_book)
    
def check_id():
    uid_list = [] 
    for contact in phone_book:
        uid_list.append(int(contact.get('id'))) 
    return max(uid_list)+1

def add_contact(new:dict):
    # new.update(check_id())
    phone_book.append(new)

def search(word: str) ->list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result       

def change (index: int, new:dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index-1][key] = field

def delete_contact(index: int):
    phone_book.pop(index-1)

def change_file(book: list[dict[str, str]]):
    with open(path, 'w', encoding='UTF-8') as file:
        stroka=''
        for contact in book:
            for key, value in contact.items():
                stroka = stroka+str(value)+':'
            
            stroka=stroka + '\n'    

        data = file.write(stroka) 
    # data.close()

