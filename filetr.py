import os
from package.module2 import TransLate
import re

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    return len(sentences) if sentences[-1] else len(sentences) - 1

def count_words(text):
    words = text.split()
    return len(words)

def read_config(file_path='config.txt'):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    return config

def main():
    config = read_config()

    # Читання налаштувань із конфігураційного файлу
    text_file = config.get('text_file', 'text.txt')
    target_language_code = config.get('target_language', 'en')
    output_mode = config.get('output_type', 'screen')
    max_characters = int(config.get('max_chars', 1000))
    max_words = int(config.get('max_words', 200))
    max_sentences = int(config.get('max_sentences', 10))

    if not os.path.exists(text_file):
        print(f"Error: File {text_file} not found.")
        return

    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    file_size = os.path.getsize(text_file)
    char_count = len(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)

    print(f"File: {text_file}")
    print(f"Size: {file_size} bytes")
    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")

    if char_count > max_characters:
        text = text[:max_characters]
    elif word_count > max_words:
        words = text.split()[:max_words]
        text = ' '.join(words)
    elif sentence_count > max_sentences:
        sentences = re.split(r'(?<=[.!?]) ', text)[:max_sentences]
        text = ' '.join(sentences)

    # Переклад тексту
    translated_text = TransLate(text, target_language_code)

    # Виведення результату на екран або у файл
    if output_mode == 'screen':
        print(f"Translated to {target_language_code}:")
        print(translated_text)
    elif output_mode == 'file':
        output_file = f"{os.path.splitext(text_file)[0]}_{target_language_code}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        print("Ok")

if __name__ == "__main__":
    main()