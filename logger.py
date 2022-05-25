import add

def log(add):
    with open('file.txt', 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {add[0]}\n')
        data.write(f'Имя: {add[1]}\n')
        data.write(f'Номер: {add[2]}\n')
        data.write(f'Описание: {add[3]}\n')
        data.write(f'\n')

#print(log())
def log_string():
    with open('file.csv', 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {add[0]}; Имя: {add[1]}; Номер: {add[2]}; Описание: {add[3]}\n')

# чтение 
def read():
    with open('file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)


