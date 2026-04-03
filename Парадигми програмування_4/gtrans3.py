import sys


def main():
    if sys.version_info >= (3, 13):
        print("Помилка: модуль module_gtrans3 не підтримує Python 3.13 і вище.")
        return

    from translator_package.module_gtrans3 import TransLate, LangDetect, CodeLang, LanguageList

    text = "Добрий день, як ваші справи?"

    print("=== Демонстрація module_gtrans3 ===")

    print("\n1. Переклад тексту:")
    print(TransLate(text, "uk", "en"))

    print("\n2. Визначення мови:")
    print(LangDetect(text, "all"))

    print("\n3. Код мови / назва мови:")
    print(CodeLang("ukrainian"))
    print(CodeLang("en"))

    print("\n4. Список мов на екран:")
    print(LanguageList("screen", "Добрий день"))


if __name__ == "__main__":
    main()