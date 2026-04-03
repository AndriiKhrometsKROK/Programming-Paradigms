import os
import json
import re
import asyncio


def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())


async def detect_language(module_name, text):
    if module_name == "module_deep":
        from translator_package.module_deep import LangDetect
        return LangDetect(text, "lang")

    if module_name == "module_gtrans3":
        from translator_package.module_gtrans3 import LangDetect
        return LangDetect(text, "lang")

    if module_name == "module_gtrans4":
        from translator_package.module_gtrans4 import LangDetect
        return await LangDetect(text, "lang")

    return "Невідомо"


async def translate_text(module_name, text, target_lang):
    if module_name == "module_deep":
        from translator_package.module_deep import TransLate, CodeLang
        translated = TransLate(text, "auto", target_lang)
        lang_name = CodeLang(target_lang)
        return translated, lang_name

    if module_name == "module_gtrans3":
        from translator_package.module_gtrans3 import TransLate, CodeLang
        translated = TransLate(text, "auto", target_lang)
        lang_name = CodeLang(target_lang)
        return translated, lang_name

    if module_name == "module_gtrans4":
        from translator_package.module_gtrans4 import TransLate, CodeLang
        translated = await TransLate(text, "auto", target_lang)
        lang_name = await CodeLang(target_lang)
        return translated, lang_name

    return "Помилка: невідомий модуль.", ""


async def main():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
    except:
        print("Помилка: не вдалося прочитати config.json")
        return

    file_name = config["file_name"]
    target_lang = config["target_lang"]
    module_name = config["module"]
    output_mode = config["output"]
    sentence_limit = config["sentences"]

    if not os.path.exists(file_name):
        print("Помилка: файл не знайдено")
        return

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read()
    except:
        print("Помилка: не вдалося прочитати текстовий файл")
        return

    file_size = os.path.getsize(file_name)
    char_count = len(text)
    sentences = split_sentences(text)
    sentence_count = len(sentences)
    selected_text = " ".join(sentences[:sentence_limit])

    language = await detect_language(module_name, text)

    print("Назва файлу:", file_name)
    print("Розмір файлу:", file_size, "байт")
    print("Кількість символів:", char_count)
    print("Кількість речень:", sentence_count)
    print("Мова тексту:", language)

    translated_text, lang_name = await translate_text(module_name, selected_text, target_lang)

    if output_mode == "screen":
        print("\nМова перекладу:", lang_name)
        print("Модуль перекладу:", module_name)
        print("Перекладений текст:")
        print(translated_text)

    elif output_mode == "file":
        new_file = file_name.split(".")[0] + "_" + target_lang + ".txt"
        with open(new_file, "w", encoding="utf-8") as f:
            f.write(translated_text)
        print("Ok")

    else:
        print("Помилка: неправильний режим виводу")


if __name__ == "__main__":
    asyncio.run(main())