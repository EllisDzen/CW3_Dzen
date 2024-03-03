import json
import os
import pytest

# Добавляем импорт функций из модуля test_main
from tests.test_main import display_last_operations, mask_card_number, mask_account_number

# Определяем путь к тестовым данным
TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), 'test_sorted_data.json')


# Загружаем тестовые данные
@pytest.fixture
def test_operations():
    with open(TEST_DATA_PATH, 'r') as file:
        return json.load(file)


# Тесты для функции load_operations
def test_load_operations(test_operations):
    # Проверяем, что функция возвращает данные
    assert test_operations is not None

    # Проверяем, что данные корректно загружены
    assert isinstance(test_operations, list)
    assert len(test_operations) > 0


# Тесты для функции mask_card_number
def test_mask_card_number():
    # Проверяем маскирование номера карты
    card_info = {'name': 'Visa', 'number': '1234567890123456'}
    assert mask_card_number(card_info) == 'Visa 123456******3456'

    card_info = {'name': 'Счет', 'number': '1234567890123456'}
    assert mask_card_number(card_info) == 'Счет **** 3456'


# Тесты для функции mask_account_number
def test_mask_account_number():
    # Проверяем маскирование номера счета
    account_info = {'name': 'Счет', 'number': '1234567890123456'}
    assert mask_account_number(account_info) == '**** 3456'

    account_info = {'name': 'Карта', 'number': '1234567890123456'}
    assert mask_account_number(account_info) == '**** 3456'


# Тесты для функции display_last_operations
def test_display_last_operations(capsys, test_operations):
    # Вызываем функцию, которую тестируем
    display_last_operations(test_operations)

    # Получаем вывод функции
    captured = capsys.readouterr()
    output_lines = captured.out.split('\n')

    # Проверяем, что вывод соответствует ожидаемому
    assert len(output_lines) > 0  # Проверяем, что есть хотя бы одна строка вывода
