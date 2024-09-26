from deep_translator import GoogleTranslator
from langdetect import detect
from tabulate import tabulate

trans = GoogleTranslator(source='auto', target='en')
supported_languages = trans.get_supported_languages(as_dict=True)

def TransLate(sourceText: str, targetLanguage: str) -> str:
    translationResult = GoogleTranslator(source='auto', target=targetLanguage).translate(sourceText)
    return translationResult

def LangDetect(text: str) -> str:
    detectedLanguage = detect(text)
    return detectedLanguage

def CodeLang(languageCodeOrName: str) -> str:
    for langCode, langName in supported_languages.items():
        if languageCodeOrName == langName:
            return f"Language code is - {langCode}"
        elif languageCodeOrName == langCode:
            return f"Language name is - {langName}"
    return "Language not found"

def LanguageList(output: str = "screen", inputText: str = "") -> str:
    tableRows = []
    for index, (langCode, langName) in enumerate(supported_languages.items(), start=1):
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
