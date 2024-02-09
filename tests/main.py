import json
import os

# Устанавливаем текущую директорию в директорию скрипта
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def load_operations(filename='operations.json'):
    with open(filename, 'r') as file:
        operations = json.load(file)
    return operations


def mask_card_number(card_number):
    if card_number:
        masked_number = f"{card_number[:4]} {card_number[4:6]} **** {card_number[-4:]}"
        return f"from: {masked_number}"
    else:
        return "from: NULL"


def mask_account_number(account_number):
    return f"to: **{account_number[-4:]}" if account_number else "to: NULL"


def display_last_operations(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    last_executed_operations = sorted(executed_operations, key=lambda op: op.get('date', ''), reverse=True)[:5]

    for operation in last_executed_operations:
        date_parts = operation.get('date', '').split('T')
        date = date_parts[0]
        time = date_parts[1]

        print(f"{operation.get('description', '')}")

        # Маскирование номера карты
        masked_card_number = mask_card_number(operation.get('from', ''))
        print(f"{masked_card_number}")

        # Маскирование номера счета
        masked_account_number = mask_account_number(operation.get('to', ''))
        print(f"{masked_account_number}")

        print(
            f"{date.replace('-', '.')} {time}\n{operation.get('operationAmount', {}).get('amount', '')} {operation.get('operationAmount', {}).get('currency', {}).get('name', '')}")
        print("\n")


if __name__ == "__main__":
    operations_data = load_operations()
    display_last_operations(operations_data)