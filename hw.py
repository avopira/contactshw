# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник 
# с внешним хранилищем информации, и чтоб был реализован основной функционал - просмотр, 
# сохранение, импорт, поиск, удаление, изменение данных.

import json

phonebook = { 
}

try:
    with open('phonebook.json','r',encoding='utf-8') as phones:
        phonebook = json.load(phones)
except:
    phonebook = {
    "дядя Ваня": {'phones': [1231654,45646644],
                    'birthday': '01.01.1960',
                    'email': "vanya@mail.ru" },
    "дядя Вася": {'phones' : [12121244444]}
}
    
def save():
    with open('phonebook.json','w',encoding='utf-8') as phones:
        phones.write(json.dumps(phonebook,ensure_ascii=False))

def load():
    with open('phonebook.json','r',encoding='utf-8') as phones:
        phonebook = json.load(phones)

def add():
    contact_name = input("Enter contact name: ")
    contact_number = input("Enter phone number: ")
    contact_birthday = input("Enter birth date of contact in MM.DD.YYYY format")
    contact_email = input("Enter mail address: ")
    newcontact = {'phones': contact_number, 'birthday': contact_birthday, 'email': contact_email}
    phonebook[contact_name] = newcontact
    print('Contact has been added')

def search():
    key = input("Enter name: ")
    if key in phonebook:
        print(phonebook[key])
    else:
        print("Entered contact was not found in phonebook")

def delete():
    f = input("Enter contact name to be deleted: ")
    if f in phonebook:
        del phonebook[f]
        print("Contact has been deleted")
    else:
        print("There is no contact with enetered contact name")

def edit():
    while True:
        print("What do you want to edit?")
        print("\
1 - Contact name\n\
2 - Phone number \n\
0 - finish editing")
        user_choice = input("Enter number: ")
        if user_choice == '1':
            contact_name = input("Enter contact name: ")
            new_contact_name = input("Enter edited contact name: ")
            phonebook[new_contact_name] = phonebook.pop(contact_name)
        elif user_choice == '2':
            contact_name = input("Enter contact name: ")
            phonebook[contact_name] = {'phones': input("Enter phone number: ")}
        elif user_choice == '0':
            break
        else:
            print("Entered number is out of scope. Please try again")
            break
        print("Contact has been edited")

while True:
    print("How can I help you? ")
    print("\
1 - Show contacts list\n\
2 - Save contacts list\n\
3 - Import contacts list\n\
4 - Seacrh\n\
5 - Delete contact\n\
6 - Edit contact\n\
7 - Add new contact\n\
0 - Exit")
    command = input("Enter number: ")
    if command == '1':
        print(phonebook)
    elif command == '2':
        save()
        print('Contacts list has been saved')
    elif command == '3':
        # load()
        with open('phonebook.json','r',encoding='utf-8') as phones:
            phonebook = json.load(phones)
        print("Contacts list has been imported")
    elif command == '4':
        search()
    elif command == '5':
        delete()
    elif command == '6':
        edit()
    elif command == '7':
        add()
    elif command == '0':
        break
    else:
        print("Entered number is out of scope. Please try again")
        break