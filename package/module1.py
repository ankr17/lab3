import googletrans
from tabulate import tabulate

available_languages = googletrans.LANGUAGES
google_translator = googletrans.Translator()

def TransLate(sourceText: str, targetLanguage: str) -> str:
    '''Функція повертає текст перекладений на задану мову, або повідомлення про помилку.'''
    translationResult = google_translator.translate(sourceText, dest=targetLanguage)
    return translationResult.text

def LangDetect(text: str) -> str:
    '''Функція повертає текст перекладений на задану мову, або повідомлення про помилку.'''
    detectedLanguage = google_translator.detect(text)
    return detectedLanguage.lang

def CodeLang(languageCodeOrName: str) -> str:
    '''Функція повертає код мови (відповідно до таблиці), якщо в параметрі lang міститься назва
    мови, або повертає назву мови, якщо в параметрі lang міститься її код,
    або повідомлення про помилку'''
    for langCode, langName in available_languages.items():
        if languageCodeOrName == langName:
            return f"Language code is - {langCode}"
        elif languageCodeOrName == langCode:
            return f"Language name is - {langName}"
    return "Language not found"

def LanguageList(output: str = "screen", inputText: str = "") -> str:
    '''Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів,
    а також текст, перекладений на цю мову. Повертає ‘Ok’, якщо всі операції виконані,
    або повідомлення про помилку.'''
    tableRows = []
    for index, (langCode, langName) in enumerate(available_languages.items(), start=1):
        translatedText = TransLate(inputText, langCode) if inputText else ""
        tableRows.append([index, langName, langCode, translatedText])

    headers = ["N", "Language", "ISO-639 code"]
    if inputText:
        headers.append("Text")

    table_string = tabulate(tableRows, headers, tablefmt="plain", numalign="left", stralign="left")

    if output == "screen":
        print(table_string)
    elif output == "file":
        with open("languages_list.txt", "w", encoding="utf-8") as fileHandle:
            fileHandle.write(table_string)
    else:
        return "Error: Unsupported output option"

    return "Ok"
