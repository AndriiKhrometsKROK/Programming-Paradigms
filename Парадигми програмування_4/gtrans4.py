import asyncio
from translator_package.module_gtrans4 import TransLate, LangDetect, CodeLang, LanguageList


async def main():
    text = "Добрий день, як ваші справи?"

    print("=== Демонстрація module_gtrans4 ===")

    print("\n1. Переклад тексту:")
    result = await TransLate(text, "uk", "en")
    print(result)

    print("\n2. Визначення мови:")
    result = await LangDetect(text, "all")
    print(result)

    print("\n3. Код мови / назва мови:")
    print(await CodeLang("ukrainian"))
    print(await CodeLang("en"))

    print("\n4. Список мов на екран:")
    result = await LanguageList("screen", "Добрий день")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())