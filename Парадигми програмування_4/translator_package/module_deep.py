from deep_translator import GoogleTranslator
from langdetect import detect_langs

LANGUAGES = {
    "af": "afrikaans",
    "ar": "arabic",
    "bg": "bulgarian",
    "bn": "bengali",
    "bs": "bosnian",
    "ca": "catalan",
    "cs": "czech",
    "cy": "welsh",
    "da": "danish",
    "de": "german",
    "el": "greek",
    "en": "english",
    "eo": "esperanto",
    "es": "spanish",
    "et": "estonian",
    "fa": "persian",
    "fi": "finnish",
    "fr": "french",
    "gu": "gujarati",
    "he": "hebrew",
    "hi": "hindi",
    "hr": "croatian",
    "hu": "hungarian",
    "id": "indonesian",
    "it": "italian",
    "ja": "japanese",
    "kn": "kannada",
    "ko": "korean",
    "lt": "lithuanian",
    "lv": "latvian",
    "mk": "macedonian",
    "ml": "malayalam",
    "mr": "marathi",
    "ne": "nepali",
    "nl": "dutch",
    "no": "norwegian",
    "pa": "punjabi",
    "pl": "polish",
    "pt": "portuguese",
    "ro": "romanian",
    "ru": "russian",
    "sk": "slovak",
    "sl": "slovenian",
    "so": "somali",
    "sq": "albanian",
    "sv": "swedish",
    "sw": "swahili",
    "ta": "tamil",
    "te": "telugu",
    "th": "thai",
    "tl": "tagalog",
    "tr": "turkish",
    "uk": "ukrainian",
    "ur": "urdu",
    "vi": "vietnamese",
    "zh-cn": "chinese (simplified)",
    "zh-tw": "chinese (traditional)"
}


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
        if not text or not text.strip():
            return "Помилка: порожній текст."

        src_code = _normalize_lang(scr)
        dest_code = _normalize_lang(dest)

        translator = GoogleTranslator(source=src_code, target=dest_code)
        return translator.translate(text)

    except Exception as e:
        return f"Помилка: {e}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        if not text or not text.strip():
            return "Помилка: порожній текст."

        variants = detect_langs(text)
        if not variants:
            return "Помилка: не вдалося визначити мову."

        best = variants[0]
        lang_code = best.lang
        confidence = best.prob
        lang_name = LANGUAGES.get(lang_code, lang_code)

        set = set.lower()

        if set == "lang":
            return lang_name
        elif set == "confidence":
            return str(confidence)
        elif set == "all":
            return f"Мова: {lang_name}, коефіцієнт довіри: {confidence}"
        else:
            return "Помилка: неправильне значення параметра set."

    except Exception as e:
        return f"Помилка: {e}"


def CodeLang(lang: str) -> str:
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


def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        out = out.lower()

        rows = []
        header = f"{'Код':<10}{'Мова':<30}"
        if text:
            header += "Переклад"

        rows.append(header)
        rows.append("-" * 100)

        for code, name in sorted(LANGUAGES.items(), key=lambda x: x[1]):
            line = f"{code:<10}{name:<30}"

            if text:
                try:
                    translated = GoogleTranslator(source="auto", target=code).translate(text)
                except Exception:
                    translated = "Помилка перекладу"

                line += translated

            rows.append(line)

        content = "\n".join(rows)

        if out == "screen":
            print(content)
        elif out == "file":
            with open("languages_deep.txt", "w", encoding="utf-8") as f:
                f.write(content)
        else:
            return "Помилка: параметр out повинен бути screen або file."

        return "Ok"

    except Exception as e:
        return f"Помилка: {e}"