import sys
import xml.etree.ElementTree as ET
from ebooklib import epub

def parse_epub(file):
    """
    Функция для парсинга EPUB файла и получения информации о книге.

    Аргументы:
    - file: строка с путем к EPUB файлу.

    Возвращает:
    - Список с информацией о книге: [Название книги, Имя автора, Название издательства, Год издания].
    - В случае ошибки при парсинге, возвращает None.
    """
    try:
        book = epub.read_epub(file)
        metadata = book.get_metadata('', 'dc')

        title = metadata['title'][0][0]
        author = metadata['creator'][0][0]
        publisher = metadata['publisher'][0][0]
        year = metadata['date'][0][0][:4]

        return [title, author, publisher, year]
    except Exception as e:
        print('Ошибка при парсинге EPUB файла:', str(e))
        return None


def parse_fb2(file):
    """
    Функция для парсинга FB2 файла и получения информации о книге.

    Аргументы:
    - file: строка с путем к FB2 файлу.

    Возвращает:
    - Список с информацией о книге: [Название книги, Имя автора, Название издательства, Год издания].
    - В случае ошибки при парсинге, возвращает None.
    """
    namespaces = {'fb2': 'http://www.gribuser.ru/xml/fictionbook/2.0'}

    try:
        tree = ET.parse(file)
        root = tree.getroot()

        title = root.find('.//fb2:book-title', namespaces).text.strip()
        author = root.find('.//fb2:first-name', namespaces).text.strip()
        publisher = root.find('.//fb2:publisher', namespaces).text.strip()
        year = root.find('.//fb2:year', namespaces).text.strip()

        return [title, author, publisher, year]
    except Exception as e:
        print('Ошибка при парсинге FB2 файла:', str(e))
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python parser.py [путь_к_файлу]")
        sys.exit(1)

    file_path = sys.argv[1]
    file_extension = file_path.split('.')[-1].lower()

    if file_extension == 'epub':
        parsed_data = parse_epub(file_path)
    elif file_extension == 'fb2':
        parsed_data = parse_fb2(file_path)
    else:
        print("Неподдерживаемый формат файла")
        sys.exit(1)

    if parsed_data is not None:
        print("Название книги:", parsed_data[0])
        print("Имя автора:", parsed_data[1])
        print("Название издательства:", parsed_data[2])
        print("Год издания:", parsed_data[3])