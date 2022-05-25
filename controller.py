import ui
import add
import logger

def run():
    do = ui.hello()
    if do == 1:
        print('Давайте внесем данные')
        user_data = add.add() # внесение контакта
        logger.log(user_data)
    # if do_it == 2:
    #     print('Кого ищем?')

    #     do = find.find() # поиск
    #     log.reading_file(do)

    # if do_it == 2:
    #     print('Справочник: ') 
    #     log.read_all_file()


