import sys
from googletrans import Translator, LANGUAGES


def _check_version():
    if sys.version_info >= (3, 13):
        raise RuntimeError("Цей модуль не підтримує Python 3.13 і вище.")


def _normalize_lang(lang: str) -> str:
    if not isinstance(lang, str) or not lang.strip():
        raise ValueError("Мова не задана.")

    lang = lang.strip().lower()

    if lang == "auto":
        return "auto"

    if lang in LANGUAGES:
        return lang

    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code

    raise ValueError(f"Невідома мова: {lang}")


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        _check_version()

        if not text or not text.strip():
            return "Помилка: порожній текст."

        src_code = _normalize_lang(scr)
        dest_code = _normalize_lang(dest)

        translator = Translator()
        result = translator.translate(text, src=src_code, dest=dest_code)
        return result.text

    except Exception as e:
        return f"Помилка: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        _check_version()

        if not text or not text.strip():
            return "Помилка: порожній текст."

        translator = Translator()
        result = translator.detect(text)

        lang_code = result.lang
        confidence = getattr(result, "confidence", None)
        lang_name = LANGUAGES.get(lang_code, lang_code)

        set = set.lower()

        if set == "lang":
            return lang_name
        elif set == "confidence":
            if confidence is None:
                return "Немає даних про коефіцієнт довіри."
            return str(confidence)
        elif set == "all":
            if confidence is None:
                return f"Мова: {lang_name}"
            return f"Мова: {lang_name}, коефіцієнт довіри: {confidence}"
        else:
            return "Помилка: неправильне значення параметра set."

    except Exception as e:
        return f"Помилка: {e}"


def CodeLang(lang: str) -> str:
    try:
        _check_version()

        if not lang or not lang.strip():
            return "Помилка: мова не задана."

        lang = lang.strip().lower()

        if lang in LANGUAGES:
            return LANGUAGES[lang]

        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                return code

        return "Помилка: мову не знайдено."

    except Exception as e:
        return f"Помилка: {e}"


def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        _check_version()

        out = out.lower()
        translator = Translator()

        rows = []
        header = f"{'Код':<10}{'Мова':<25}"
        if text:
            header += "Переклад"

        rows.append(header)
        rows.append("-" * 80)

        for code, name in sorted(LANGUAGES.items(), key=lambda x: x[1]):
            line = f"{code:<10}{name:<25}"

            if text:
                try:
                    translated = translator.translate(text, src="auto", dest=code).text
                except Exception:
                    translated = "Помилка перекладу"

                line += translated

            rows.append(line)

        content = "\n".join(rows)

        if out == "screen":
            print(content)
        elif out == "file":
            with open("languages_gtrans3.txt", "w", encoding="utf-8") as f:
                f.write(content)
        else:
            return "Помилка: параметр out повинен бути screen або file."

        return "Ok"

    except Exception as e:
        return f"Помилка: {e}"