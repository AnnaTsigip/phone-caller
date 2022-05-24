import ui

def run():
    do_it = ui.hello()
    if do_it == 1:
        print('Давайте внесем данные')

        do = add.added() # внесение контакта
        log.log_to_file(do)
    if do_it == 2:
        print('Кого ищем?')

        do = find.find() # поиск
        log.reading_file(do)

    if do_it == 3:
        print('Справочник: ') 
        log.read_all_file()


