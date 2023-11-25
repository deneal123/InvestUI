import os
import re
import sys
import shutil
import argparse
import setup_common

# Получить абсолютный путь к каталогу текущего файла (каталог проекта InvestUI)
project_directory = os.path.dirname(os.path.abspath(__file__))

# Проверка, присутствует ли каталог «setup» в каталоге проекта.
if "setup" in project_directory:
    # Если каталог «setup» присутствует, переместитесь на один уровень выше в родительский каталог.
    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Добавление каталога проекта в начало пути поиска Python.
sys.path.insert(0, project_directory)

from library.custom_logging import setup_logging

# Настройка ведения журнала
log = setup_logging()

def check_torch():
    # Проверка nVidia toolkit or AMD toolkit
    if shutil.which('nvidia-smi') is not None or os.path.exists(
        os.path.join(
            os.environ.get('SystemRoot') or r'C:\Windows',
            'System32',
            'nvidia-smi.exe',
        )
    ):
        log.info('nVidia toolkit обнаружен')
    elif shutil.which('rocminfo') is not None or os.path.exists(
        '/opt/rocm/bin/rocminfo'
    ):
        log.info('AMD toolkit обнаружен')
    else:
        log.info('Подключение только CPU Torch')


def main():
    setup_common.check_repo_version()
    # Разобрать аргументы командной строки
    parser = argparse.ArgumentParser(
        description='Validate that requirements are satisfied.'
    )
    parser.add_argument(
        '-r',
        '--requirements',
        type=str,
        help='Path to the requirements file.',
    )
    parser.add_argument('--debug', action='store_true', help='Debug on')
    args = parser.parse_args()

    torch_ver = check_torch()
    
    if args.requirements:
        setup_common.install_requirements(args.requirements, check_no_verify_flag=True)
    else:
        if torch_ver == 1:
            setup_common.install_requirements('requirements_low.txt', check_no_verify_flag=True)
        else:
            setup_common.install_requirements('requirements_high.txt', check_no_verify_flag=True)



if __name__ == '__main__':
    main()
