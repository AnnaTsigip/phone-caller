# first.name = input("Введите имя: ").capitalize()
# last_name = input("Введите фамилию: ").capitalize()
# phone_number = input("Введите номер телефона: ").capitalize()
# additional_data = input("Дополнительные данные: ").capitalize()
"""
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

# print(first_name())
# print(last_name())
# print(phone_number())
# print(additional_data())

with open('file.txt', 'a', encoding='utf-8') as data:
    data.write(f'Фамилия: {first_name()}\n')
    data.write(f'Имя: {last_name()}\n')
    data.write(f'Номер: {phone_number()}\n')
    data.write(f'Описание: {additional_data()}\n')
    data.write(f'\n')

"""


# def name_init(first_name,last_name, phone_number,additional_data):
#     first_name = input("Введите фамилию: ").capitalize()
#     last_name = input("Введите имя: ").capitalize()
#     phone_number = input("Введите номер телефона: ").capitalize()
#     additional_data = input("Дополнительные данные: ").capitalize()
#     return [first_name,last_name, phone_number,additional_data]

# print(name_init())
# # with open('file.txt', 'a', encoding='utf-8') as data:
# #     data.write(f'Фамилия: {name_init()}\n Имя: {name_init()}\n Номер: {name_init()}\n Описание:{name_init()}\n' )

# print(name_init())

# f = open('data.txt', 'a')
# f.write('{0:10} | {1:10} | {2}'.format(first_name(), last_name(), phone_number(),additional_data()) + '\n')
# print('\nКонтакт {lastName} {name} успешно добавлен\n'.format(lastName=m.last_name, name=m.name))
# f.close()



# with open('file.txt', 'a', encoding='utf-8') as data:
#     data.write(last_name())
# with open('file.txt', 'a', encoding='utf-8') as data:
#     data.write(phone_number())
# with open('file.txt', 'a', encoding='utf-8') as data:
#     data.write(additional_data())