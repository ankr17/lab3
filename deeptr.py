from package.module2 import TransLate, LangDetect, LanguageList, CodeLang

text = input("Write a text for translation: ")
lang = input("Specify the language you want to translate into: ")
code = input("Write the name or the code of the language: ")

print("The program is working (module 2)")
print(TransLate(text, lang))
print(LangDetect(text))
print(CodeLang(code))
print(LanguageList("screen", text))
