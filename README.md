Название проекта: Операции по счетам
Описание проекта: Проект "Операции по счетам" разработан для предоставления возможности просмотра последних выполненных операций клиентами банка. Основная цель проекта - реализация функции, которая выводит на экран список из 5 последних успешных банковских операций клиента в удобном формате.

Установка:

Склонируйте репозиторий с проектом: git clone https://github.com/EllisDzen/CW3_Dzen.git
Перейдите в каталог проекта: cd your_project
Создайте виртуальное окружение: python -m venv venv
Активируйте виртуальное окружение:
На Windows: venv\Scripts\activate
На macOS и Linux: source venv/bin/activate
Установите зависимости: pip install -r requirements.txt
Запустите проект: python main.py
Использование:
После установки и запуска проекта, данные о последних операциях будут автоматически загружены из файла operations.json.
Результаты будут выведены на экран в удобном формате, содержащем дату, описание операции, источник и получатель, а также сумму и валюту перевода.

Структура проекта:

diff
Copy code
- main.py
- operations.json
- README.md
- requirements.txt
- tests/
    - test_main.py
- venv/ (виртуальное окружение)
Примеры кода:
python
Copy code
import json

def load_operations(filename='operations.json'):
    with open(filename, 'r') as file:
        operations = json.load(file)
    return operations

def display_last_operations(operations):
    # Реализация функции вывода последних операций
    pass

# Загрузка данных о последних операциях
operations_data = load_operations()

# Вывод последних операций на экран
display_last_operations(operations_data)
