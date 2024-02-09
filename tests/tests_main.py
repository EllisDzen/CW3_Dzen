import os
import json
import pytest
from main import load_operations, mask_card_number, mask_account_number, display_last_operations

# Путь к файлу с тестовыми данными
TEST_DATA_FILE = os.path.join(os.path.dirname(__file__), 'operations.json')

@pytest.fixture
def sample_operations_data():
    # Загружаем тестовые данные из файла operations.json
    with open(TEST_DATA_FILE, 'r') as file:
        operations_data = json.load(file)
    return operations_data

def test_load_operations(sample_operations_data):
    # Проверяем, что функция load_operations корректно загружает данные из файла
    operations_data = load_operations(TEST_DATA_FILE)
    assert operations_data == sample_operations_data

def test_mask_card_number():
    # Проверяем, что функция mask_card_number корректно маскирует номер карты
    assert mask_card_number("1234567890123456") == "from: 1234 56 **** 3456"
    assert mask_card_number("") == "from: NULL"

def test_mask_account_number():
    # Проверяем, что функция mask_account_number корректно маскирует номер счета
    assert mask_account_number("9876543210") == "to: **3210"
    assert mask_account_number("") == "to: NULL"

# Тестирование функции display_last_operations требует захвата вывода, для этого можно использовать capsys
def test_display_last_operations(capsys, sample_operations_data):
    # Проверяем, что функция display_last_operations выводит последние операции корректно
    display_last_operations(sample_operations_data)
    captured = capsys.readouterr()
    assert "Перевод организации" in captured.out
    assert "from: Maes tr **** 5568" in captured.out
    assert "to: **2869" in captured.out
    assert "2019.11.19 09:22:25.899614" in captured.out
    assert "30153.72 руб." in captured.out
    assert "Перевод со счета на счет" in captured.out
    assert "from: Счет  3 **** 9794" in captured.out
    assert "to: **8125" in captured.out
    assert "2019.11.13 17:38:04.800051" in captured.out
    assert "62814.53 руб." in captured.out
    assert "Открытие вклада" in captured.out
    assert "from: NULL" in captured.out
    assert "to: **8381" in captured.out
    assert "2019.11.05 12:04:13.781725" in captured.out
    assert "21344.35 руб." in captured.out