# решение перебором в списке
def calculate_hours(data):
    hours_dict = {}

    for record in data:
        name, hours = record.rsplit(' ', 1)
        hours = int(hours)

        if name in hours_dict:
            hours_dict[name].append(hours)
        else:
            hours_dict[name] = [hours]

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
