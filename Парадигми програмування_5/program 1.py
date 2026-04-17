import re

UKR_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
LAT_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def get_word_group(word):

    for char in word.lower():
        if char in UKR_ALPHABET:
            return 0
        elif char in LAT_ALPHABET:
            return 1
    return 2


def char_order(char):

    char = char.lower()

    if char in UKR_ALPHABET:
        return (0, UKR_ALPHABET.index(char))
    elif char in LAT_ALPHABET:
        return (1, LAT_ALPHABET.index(char))
    else:
        return (2, ord(char))


def word_sort_key(word):

    group = get_word_group(word)
    chars = [char_order(c) for c in word]
    return (group, chars)


def main():
    file_name = "text.txt"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл", file_name, "не знайдено.")
        return

    print("Початковий текст:\n")
    print(text)

    words = re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ_’']+", text)

    sorted_words = sorted(words, key=word_sort_key)

    print("\nВідсортовані слова:\n")
    print(sorted_words)


if __name__ == "__main__":
    main()