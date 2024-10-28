import os
import requests

FILE_URL = 'https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt'
FILE_BASE_NAME = 'dictionary.txt'

# TODO: возможно прикрутить нейросеть или NLP-систему
#  для анализа слов, чтобы оставить только существительные


def get_dictionary() -> None:
    """
    Скачивает наиболее полный (1 532 629 слова) словарь русских слов
    в файл full_dictionary.txt в папку скрипта.
    """
    response = requests.get(FILE_URL)
    text = response.content.decode('cp1251')

    if text == '404: Not Found':
        print('Файл не найден или url указан некорректно.')

    else:
        file_name = 'full ' + FILE_BASE_NAME
        with open(file_name, 'wb') as file:
            file.write(text.encode('utf-8'))


def get_line_count(file_path: str) -> int:
    """
    Подсчитывает количество строк (слов) в файле.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for count, line in enumerate(file):
                pass
            return count + 1

    except Exception as ex:
        print(ex)


def get_words_with_length(file_path: str, word_length: int) -> None:
    """
    Создает новый словарь, содержащий слова с заданной длиной.
    """
    file_name = str(word_length) + '-char ' + FILE_BASE_NAME
    try:
        with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
            for line in file:
                if len(line) == word_length + 1:
                    file_new.write(line)

    except Exception as ex:
        print(ex)


def del_words_with_invalid_characters(file_path: str) -> None:
    """
    Удаляет из словаря слова с недопустимыми символами.
    """
    file_name = 'correct ' + FILE_BASE_NAME
    try:
        with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
            for line in file:
                if line.rstrip('\n').isalpha():
                    file_new.write(line)

    except Exception as ex:
        print(ex)


def del_words_with_uppercase_letters(file_path: str) -> None:
    """
    Удаляет из словаря слова с заглавными буквами.
    """
    file_name = 'final ' + FILE_BASE_NAME
    try:
        with open(file_path, 'r', encoding='utf-8') as file, open(file_name, 'w', encoding='utf-8') as file_new:
            for line in file:
                if not sum(1 for ch in line if ch.isupper()):
                    file_new.write(line)

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    get_dictionary()
    print('В словаре:', get_line_count('full dictionary.txt'), 'слов.')

    get_words_with_length('full dictionary.txt', 5)
    print('В словаре:', get_line_count('5-char dictionary.txt'), 'слов.')

    del_words_with_invalid_characters('5-char dictionary.txt')
    print('В словаре:', get_line_count('correct dictionary.txt'), 'слов.')

    del_words_with_uppercase_letters('correct dictionary.txt')
    print('В словаре:', get_line_count('final dictionary.txt'), 'слов.')

    # Чистка папки от промежуточных словарей
    os.remove('full dictionary.txt')
    os.remove('5-char dictionary.txt')
    os.remove('correct dictionary.txt')
