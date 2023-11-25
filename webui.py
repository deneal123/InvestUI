import streamlit as st
from library.custom_logging import setup_logging
from library.IndentationHelper import IndentationHelper
from config_file import load_config, is_value_changed, save_config
import pandas as pd
from sklearn.linear_model import LinearRegression  # Импортируем LinearRegression из scikit-learn
import pickle
import os
from io import StringIO

# Назначение переменной логирования
log = setup_logging()

class Webpage:
    def __init__(self):
        # Назначение переменной логирования
        self.log = setup_logging()

        # Загрузка конфигурационного файла
        self.config_data = load_config()

        # Класс функций для отступов
        self.helper = IndentationHelper()

    def load_linear_model(self, weights_folder):
        """
        Загрузка модели LinearRegression из файла.
        """
        weights_files = [f for f in os.listdir(weights_folder) if os.path.isfile(os.path.join(weights_folder, f))]

        if not weights_files:
            st.error("No files found in the 'weights' folder.")
            return None

        weights_path = os.path.join(weights_folder, weights_files[0])  # Выберите первый файл в папке
        try:
            with open(weights_path, 'rb') as file:
                model = pickle.load(file)
            if isinstance(model, LinearRegression):
                return model
            else:
                st.error("The loaded model is not an instance of LinearRegression.")
                return None
        except Exception as e:
            st.error(f"Error loading LinearRegression model: {e}")
            return None

    def run(self):
        """
        Запуск приложения.
        """

        # Используем функцию st.markdown() для отображения текста с выравниванием, увеличением размера шрифта и сменой шрифта
        st.markdown("<h1 style='text-align: center; font-size: 7em; font-family: Comic Sans MS, sans-serif;'>InvestUI</h1>",
                    unsafe_allow_html=True)

        # Загрузка CSV файла
        uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

        # Предварительно определите переменную bytes_data
        bytes_data = None

        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)

        # Проверка наличия данных перед чтением CSV
        if bytes_data is not None:
            # Перебор различных кодировок
            encodings_to_try = ['utf-8', 'Windows-1251']
            df = None

            for encoding in encodings_to_try:
                try:
                    df = pd.read_csv(StringIO(bytes_data.decode(encoding)))
                    break  # Если успешно считано, прерываем цикл
                except UnicodeDecodeError:
                    st.warning(f"Failed to decode using {encoding} encoding. Trying another encoding.")

            if df is not None:
                # Отображение предпросмотра первых 5 строк
                st.write("Preview of the first 5 rows:")
                st.dataframe(df.head())
            else:
                st.error("Unable to decode the CSV file with any of the specified encodings.")
        else:
            st.write("No file uploaded.")

        # Путь к папке с весами
        weights_folder = "weights"

        # Загрузка весов модели LinearRegression
        model = self.load_linear_model('./weights')

        if model is not None:
            st.success("LinearRegression model loaded successfully.")
            # Добавьте дополнительную логику для использования модели, например, прогнозирование на данных из DataFrame
            # predictions = model.predict(df)
            # st.write("Predictions:", predictions)
        else:
            st.warning("No LinearRegression model loaded.")

if __name__ == "__main__":
    # Создаем экземпляр класса Webpage
    webpage_instance = Webpage()
    # Запускаем приложение через экземпляр
    webpage_instance.run()
