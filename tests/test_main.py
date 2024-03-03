import json
import os

# Устанавливаем текущую директорию в директорию скрипта
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def load_operations(filename='sorted_data.json'):
    with open(filename, 'r') as file:
        operations = json.load(file)
    return operations


def mask_card_number(card_info):
    if card_info:
        card_name = card_info.get('name', '')
        card_number = card_info.get('number', '')

        if card_name == 'Счет':
            masked_number = f"**** {card_number[-4:]}"
        else:
            masked_number = f"{card_number[:6]}{'*' * (len(card_number) - 10)}{card_number[-4:]}"  # Убран лишний пробел

        return f"{card_name} {masked_number}"
    else:
        return "NULL"


def mask_account_number(account_info):
    if account_info:
        account_name = account_info.get('name', '')
        account_number = account_info.get('number', '')

        if account_name == 'Счет':
            masked_number = f"**** {account_number[-4:]}"
        else:
            masked_number = f"**** {account_number[-4:]}"

        return f"{masked_number}"
    else:
        return "to: NULL"


def display_last_operations(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    last_executed_operations = sorted(executed_operations, key=lambda op: op.get('date', ''), reverse=True)[:5]

    for operation in last_executed_operations:
        date_parts = operation.get('date', '').split('T')
        date = date_parts[0]
        time = date_parts[1]

        print(f"ID - {operation.get('id', '')}")
        print(f"Статус - {operation.get('state', '')}")
        print(f"Дата - {date} {time}")
        print(f"Сумма - {operation.get('operationAmount', {}).get('amount', '')}, {operation.get('operationAmount', {}).get('currency', {}).get('name', '')}")
        print(f"Операция - {operation.get('description', '')}")
        print(f"Откуда - {operation.get('from', {}).get('name', '')} ")
        print(f"Номер - {mask_account_number(operation.get('from', {}))}")
        print(f"Куда - {operation.get('to', {}).get('name', '')} ")
        print(f"Номер - {mask_account_number(operation.get('to', {}))}\n")


if __name__ == "__main__":
    operations_data = load_operations()
    display_last_operations(operations_data)
