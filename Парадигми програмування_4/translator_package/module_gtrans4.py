from googletrans import Translator, LANGUAGES


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


async def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        if not text or not text.strip():
            return "Помилка: порожній текст."

        src_code = _normalize_lang(scr)
        dest_code = _normalize_lang(dest)

        translator = Translator()
        result = await translator.translate(text, src=src_code, dest=dest_code)
        return result.text

    except Exception as e:
        return f"Помилка: {e}"


async def LangDetect(text: str, set: str = "all") -> str:
    try:
        if not text or not text.strip():
            return "Помилка: порожній текст."

        translator = Translator()
        result = await translator.detect(text)

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


async def CodeLang(lang: str) -> str:
    try:
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


async def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        out = out.lower()
        translator = Translator()

        rows = []
        header = f"{'Код':<10}{'Мова':<25}"
        if text:
            header += "Переклад"

        rows.append(header)
        rows.append("-" * 90)

        count = 0
        for code, name in sorted(LANGUAGES.items(), key=lambda x: x[1]):
            line = f"{code:<10}{name:<25}"

            if text:
                try:
                    result = await translator.translate(text, src="auto", dest=code)
                    translated = result.text
                except Exception:
                    translated = "Помилка перекладу"

                line += translated

            rows.append(line)
            count += 1

            # щоб вивід не був занадто гігантський
            if count >= 20 and out == "screen":
                break

        content = "\n".join(rows)

        if out == "screen":
            print(content)
        elif out == "file":
            with open("languages_gtrans4.txt", "w", encoding="utf-8") as f:
                f.write(content)
        else:
            return "Помилка: параметр out повинен бути screen або file."

        return "Ok"

    except Exception as e:
        return f"Помилка: {e}"