import pytest
from my_functions import format_fio, format_phone, has_keywords

# тест форматирования фио
@pytest.mark.parametrize("input_fio, expected", [
    ("Иванов Иван Иванович", ("Иванов", "Иван", "Иванович")), # полный вариант
    ("Петров Петр", ("Петров", "Петр", "")),                  # без отчества
    ("Сидоров", ("Сидоров", "", "")),                         # только фамилия
    ("  Смирнова Анна Сергеевна  ", ("Смирнова", "Анна", "Сергеевна")), # с пробелами
])
def test_format_fio(input_fio, expected):
    assert format_fio(input_fio) == expected

# тест формат телефона
@pytest.mark.parametrize("input_phone, expected", [
    ("+7(916)123-45-67", "+7(916)123-45-67"),                 # уже в правильном формате
    ("8 916 123 45 67", "+7(916)123-45-67"),                  # через пробелы и 8
    ("8(916)123-45-67 доб. 123", "+7(916)123-45-67 доб.123"), # с добавочным номером
    ("89161234567", "+7(916)123-45-67"),                      # сплошной строкой
])
def test_format_phone(input_phone, expected):
    assert format_phone(input_phone) == expected

# тест Проверка ключевых слов
@pytest.mark.parametrize("text, keywords, expected", [
    ("Я учу python и web-дизайн", ["дизайн", "python"], True),      # есть совпадения
    ("Просто текст про котиков", ["дизайн", "web"], False),         # нет совпадений
    ("Люблю PYTHON", ["python"], True),                             # проверка регистра 
    ("", ["python"], False),                                        # пустая строка
])
def test_has_keywords(text, keywords, expected):
    assert has_keywords(text, keywords) == expected