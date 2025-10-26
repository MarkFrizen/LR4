import csv
from io import StringIO
csv_data = """name,age
Alice,25
Bob,35
Charlie,40
Diana,28
Eve,31
"""
def read_csv(data):
    try:
        return list(csv.DictReader(StringIO(data)))
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        return []
def is_adult(user):
    return int(user.get('age', 0)) > 30
def to_uppercase(user):
    user['name'] = user.get('name', '').upper()
    return user
def process_users(data):
    users = read_csv(data)
    filtered_users = list(filter(is_adult, users))
    transformed_users = list(map(to_uppercase, filtered_users))
    return transformed_users
if __name__ == "__main__":
    result = process_users(csv_data)
    for user in result:
        print(user)