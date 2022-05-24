# import ui

# with open('file.txt', 'a', encoding='utf-8') as data:
#     data.write(f'Фамилия: {first_name()}\n')
#     data.write(f'Имя: {last_name()}\n')
#     data.write(f'Номер: {phone_number()}\n')
#     data.write(f'Описание: {additional_data()}\n')

# with open('file.csv', 'a', encoding='utf-8') as data:
#     data.write(f'Фамилия: {first_name()}\n')
#     data.write(f'Имя: {last_name()}\n')
#     data.write(f'Номер: {phone_number()}\n')
#     data.write(f'Описание: {additional_data()}\n')



#1 введение данных

def first_name():
    first_name = input("Введите фамилию: ").capitalize()
    return first_name

def last_name():
    last_name = input("Введите имя: ").capitalize()
    return last_name

def phone_number():
    phone_number = input("Введите номер телефона: ").capitalize()
    return phone_number

def additional_data():
    additional_data = input("Дополнительные данные: ").capitalize()
    return additional_data

with open('file.txt', 'a', encoding='utf-8') as data:
    data.write(f'Фамилия: {first_name()}\n')
    data.write(f'Имя: {last_name()}\n')
    data.write(f'Номер: {phone_number()}\n')
    data.write(f'Описание: {additional_data()}\n')

# with open('file.csv', 'a', encoding='utf-8') as data:
#     data.write(f'Фамилия: {first_name()}\n')
#     data.write(f'Имя: {last_name()}\n')
#     data.write(f'Номер: {phone_number()}\n')
#     data.write(f'Описание: {additional_data()}\n')

# чтение 
# with open('file.txt', 'r', encoding='utf-8') as data:
#     for i in data:
#         string = data.readline()
#         print(string)

