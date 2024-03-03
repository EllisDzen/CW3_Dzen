import json
import re

# Загрузка данных из файла JSON
with open('test_operations.json', 'r') as file:
    data = json.load(file)


# Функция для изменения формата вывода полей "from" и "to"
def format_account_info(account):
    match = re.match(r'(\D+)\s(.+)', account)
    if match:
        name = match.group(1).strip()
        number = match.group(2).strip()
        return {
            "name": name,
            "number": number,
            "full": account
        }
    else:
        return {
            "number": account,
            "full": account
        }


# Сортировка данных по полю "id"
sorted_data = sorted(data, key=lambda x: x.get("id", 0))

# Применение изменений к данным
for entry in sorted_data:
    entry['from'] = format_account_info(entry.get('from', ''))
    entry['to'] = format_account_info(entry.get('to', ''))

# Сохранение отсортированных и отформатированных данных в файл JSON
with open('test_sorted_data.json', 'w') as file:
    json.dump(sorted_data, file, indent=4, ensure_ascii=False)

print("Данные были успешно отсортированы и сохранены в файл 'test_sorted_data.json'.")
