def add():
    user_data = []
    first_name = input("Введите фамилию: ").capitalize()
    user_data.append(first_name)
    last_name = input("Введите имя: ").capitalize() 
    user_data.append(last_name)  
    phone_number = input("Введите номер телефона: ").capitalize()
    user_data.append(phone_number)
    additional_data = input("Дополнительные данные: ").capitalize()
    user_data.append(additional_data)
    print('Добавлен контакт: ', *user_data)
    return user_data
#print(f'{first_name};{last_name};{phone_number};{dditional_data}') 
#print(add())




