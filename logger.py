import add

def log(add):
    with open('file.txt', 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {add[0]}\n')
        data.write(f'Имя: {add[1]}\n')
        data.write(f'Номер: {add[2]}\n')
        data.write(f'Описание: {add[3]}\n')
        data.write(f'\n')

#print(log())
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


# a = find.find()
#     if a == 1: