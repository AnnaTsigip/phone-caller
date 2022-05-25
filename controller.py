import ui
import add
import logger

def run():
    do = ui.hello()
    if do == 1:
        print('Давайте внесем данные')

        user_data = add.add() # внесение контакта столбиком
        logger.log(user_data)

    if do == 2:
        print('Давайте внесем данные')
        user_data = add.add() # внесение контакта строкой
        logger.log_string(user_data)

    if do == 3:
        print('Справочник: ') 
        logger.read()


