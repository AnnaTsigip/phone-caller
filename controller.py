import ui
import add
import logger

def run():
    do_it = ui.hello()
    if do_it == 1:
        print('Давайте внесем данные')
        added = add.added() # внесение контакта
        logger.log(added)
    # if do_it == 2:
    #     print('Кого ищем?')

    #     do = find.find() # поиск
    #     log.reading_file(do)

    # if do_it == 2:
    #     print('Справочник: ') 
    #     log.read_all_file()


