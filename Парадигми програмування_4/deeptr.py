
from translator_package.module_deep import TransLate, LangDetect, CodeLang, LanguageList


def main():
    text = "Добрий день, як ваші справи?"

    print("=== Демонстрація module_deep ===")

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