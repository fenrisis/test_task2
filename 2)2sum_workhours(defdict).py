from collections import defaultdict
# defaultdict автоматом присваеивает значение ключам


def calculate_hours(data):
    hours_dict = defaultdict(list)

    for record in data:
        name, hours = record.rsplit(' ', 1)
        hours_dict[name].append(int(hours))

    for name, hours_list in hours_dict.items():
        print(f"{name}: {', '.join(map(str, hours_list))}; sum: {sum(hours_list)}")


data = [
    "Андрей 9",
    "Василий 11",
    "Роман 7",
    "X Æ A-12 45",
    "Иван Петров 3",
    "Андрей 6",
    "Роман 11"
]

calculate_hours(data)