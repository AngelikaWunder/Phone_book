main_menu = ''' Главное меню
1.Открыть файл
2.Сохранить файл
3.Показать все контакты
4.Создать новый контакт
5.Найти контакт
6.Изменить контакт
7.Удалить контакт
8.Выход
'''
menu_choice='Выберите пунтк меню: '
input_error = 'Некорректный ввод. Введите от 1 до 8'
book_error = 'Телефонная книга пуста или файл не открыт'
open_successful = 'Телефонная книга успешно открыта'
input_new_contact = 'Введите данные нового контакта'
new_contact =['Введите имя контакта:', 'Введите номер телефона:', 'Введите комментарий: ']
search_word = 'Введите искомый элемет: '
input_index = 'Введите индекс изменяемого контакта: '
input_change_contact = 'Введите данные изменяемого контакта или Enter, чтобы оставить без изменений: '
input_deleted_index = 'Введите индекс контакта, который хотите удалить: '
file_is_saved = 'Файл успешно сохранен'

def contact_saved(name: str):
    return  f'Контакт {name} успешно сохранен'

def contact_changed(name: str):
    return f'Контакт {name} успешно изменен'

def contact_deleted(name: str):
    return f'Контакт {name} успешно удален'


# 1:Панкратов Алексей:89213456687:однокурсник Политех
# 2:Шишенко Максим:8123335647:друг Алексея
# 3:Алексей:9113454545:ИТинжиниринг 
