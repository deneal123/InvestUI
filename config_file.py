from library.custom_logging import setup_logging
import json

# Назначение переменной логирования
log = setup_logging()


# Создание стандартных настроек конфигурационного файла
def save_default_config():
    """
    Создает и сохраняет стандартные настройки конфигурационного файла.

    :param: None.
    :return: None.
    """

    config_data = {

    }

    with open('config.json', 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

    log.info('Применение стандартных настроек конфигурационного файла')


# Глобальная переменная для хранения предыдущих параметров
previous_config_data = None


def load_config():
    """
    Загружает данные конфигурационного файла и сохраняет их в глобальную переменную.

    :param previous_config_file: глобальная переменная хранящая список.
    :return config_data: список данных выгруженных из конфигурационного файла.
    """

    global previous_config_data

    # Загрузка конфигурационных параметров из файла
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)

    # Сохраняем текущие параметры в глобальной переменной
    previous_config_data = config_data

    return config_data


def is_value_changed(key, new_value):
    """
    Создает и сохраняет стандартные настройки конфигурационного файла.

    :param previous_config_file: глобальная переменная хранящая список.
    :return previous_config_data[key] != new_value: возвращает в глобальную переменную...
    новое значение для соответствующего ключа, если это значение ключа...
    было измененно.
    :return True: возвращает true, если значение ключа не изменилось.
    """

    global previous_config_data

    # Проверяем, изменилось ли значение параметра
    if previous_config_data is not None and key in previous_config_data:
        return previous_config_data[key] != new_value
    else:
        # Если предыдущих данных нет, считаем, что значение изменилось
        return True


def save_config(config_data):
    """
    Сохраняет параметры в конфигурационный файл.

    :param: None.
    :return: None.
    """

    # Сохранение конфигурационных параметров в файл
    with open('config.json', 'w') as config_file:
        json.dump(config_data, config_file, indent=4)


if __name__ == '__main__':
    save_default_config()
