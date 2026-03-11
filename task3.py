from googletrans import Translator, LANGUAGES

translator = Translator()


def TransLate(text, lang):
    try:
        code = None
        lang_input = lang.strip().lower()

        if lang_input in LANGUAGES:
            code = lang_input
        else:

            for k, v in LANGUAGES.items():
                if v.lower() == lang_input:
                    code = k
                    break

        if code is None:
            return f"Помилка: мову '{lang}' не знайдено."

        result = translator.translate(text, dest=code)
        return result.text

    except Exception as e:
        return f"Помилка перекладу: {e}"


def LangDetect(txt):
    try:
        result = translator.detect(txt)
        return result

    except Exception as e:
        return f"Помилка визначення мови: {e}"


def CodeLang(lang):
    try:
        lang_input = lang.strip().lower()

        # якщо це код мови
        if lang_input in LANGUAGES:
            return LANGUAGES[lang_input].title()

        # якщо це назва мови
        for k, v in LANGUAGES.items():
            if v.lower() == lang_input:
                return k

        return f"Помилка: мову '{lang}' не знайдено."

    except Exception as e:
        return f"Помилка обробки мови: {e}"

txt = "Текст із Парадигм Програмування"
lang = input("Введіть мову перекладу (код або назву): ")

print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang(lang))