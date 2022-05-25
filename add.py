def add(added):
    added = []
    first_name = input("Введите фамилию: ").capitalize()
    added.append(first_name)
    last_name = input("Введите имя: ").capitalize() 
    added.append(last_name)  
    phone_number = input("Введите номер телефона: ").capitalize()
    added.append(phone_number)
    additional_data = input("Дополнительные данные: ").capitalize()
    added.append(additional_data)
    print('Добавлен контакт: added')
    return added
#print(f'{first_name};{last_name};{phone_number};{dditional_data}') 
#print(add())







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