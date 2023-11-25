import streamlit as st
from library.custom_logging import setup_logging
from library.IndentationHelper import IndentationHelper
from config_file import load_config, is_value_changed, save_config
import numpy as np
import pandas as pd
import json

# Назначение переменной логирования
log = setup_logging()


class Webpage:
    def __init__(self):
        # Это используется для скрытия предупреждения о кодировании при загрузке файла.
        st.set_option('deprecation.showfileUploaderEncoding', False)

        # Назначение переменной логирования
        self.log = setup_logging()

        # Загрузка конфигурационного файла
        self.config_data = load_config()

        # Класс функций для отступов
        self.helper = IndentationHelper()

    def run(self):
        """
        Запуск приложения.
        """

        st.write("ПРИВЕТ")


if __name__ == "__main__":
    # Создаем экземпляр класса Webpage
    webpage_instance = Webpage()
    # Запускаем приложение через экземпляр
    webpage_instance.run()
