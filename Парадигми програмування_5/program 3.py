import json 

people = {
    "Янголь": ["Анна", "Іванівна", 1814],
    "Бакман": ["Олег", "Якович", 1856],
    "Мельник": ["Степан", "Петрович", 1871],
    "Коцюбинський": ["Михайло", "Михайлович", 1864],
    "Скоропадський": ["Павло", "Петро", 1722],
    "Ягідний": ["Михайло", "Савич", 1866],
    "Мінаков": ["Олексій", "Вікторович", 1894],
    "Плохій": ["Сергій", "Миколайович", 1938],
    "Юрасов": ["Стас", "Андрійович", 1935],
    "Кириченко": ["Віктор", "Вікторович", 1930]
}

filename = "people.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(people, file, ensure_ascii=False, indent=4)

print(f"Дані успішно записано у файл {filename}")

with open(filename, "r", encoding="utf-8") as file:
    loaded_people = json.load(file)

print("\nДані, зчитані з JSON-файлу:")

for surname, info in loaded_people.items():
        name, patronymic, birth_year = info
        print(f"Прізвище: {surname}, Ім'я: {name}, По батькові: {patronymic}, Рік народження: {birth_year}")