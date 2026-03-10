from googletrans import Translator, LANGUAGES

translator = Translator()


def TransLate(text, lang):
    """
    Перекладає текст на вказану мову.
    text - текст для перекладу
    lang - назва мови або код мови
    """
    try:
        lang_input = lang.strip().lower()
        code = None

        # Якщо введено код мови
        if lang_input in LANGUAGES:
            code = lang_input
        else:
            # Якщо введено назву мови
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
    """
    Визначає мову тексту та confidence.
    """
    try:
        return translator.detect(txt)
    except Exception as e:
        return f"Помилка визначення мови: {e}"


def CodeLang(lang):
    """
    Якщо введено назву мови - повертає код.
    Якщо введено код - повертає назву мови.
    """
    try:
        lang_input = lang.strip().lower()

        if lang_input in LANGUAGES:
            return LANGUAGES[lang_input].title()

        for k, v in LANGUAGES.items():
            if v.lower() == lang_input:
                return k

        return f"Помилка: мову '{lang}' не знайдено."

    except Exception as e:
        return f"Помилка обробки мови: {e}"


txt = input("Введіть текст: ")
lang = input("Введіть мову перекладу (назва або код): ")

print("Введений текст:", txt)
print("Визначення мови:", LangDetect(txt))
print("Переклад:", TransLate(txt, lang))
print("Інформація про мову:", CodeLang(lang))