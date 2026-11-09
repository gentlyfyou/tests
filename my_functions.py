import re

# логика из задания 3 форматирование фио
def format_fio(fio_string: str) -> tuple:
    parts = fio_string.strip().split()
    if len(parts) >= 3:
        return parts[0], parts[1], parts[2]
    elif len(parts) == 2:
        return parts[0], parts[1], ""
    elif len(parts) == 1:
        return parts[0], "", ""
    return "", "", ""

# логика из задания 3 форматирование телефона
def format_phone(phone: str) -> str:
    pattern = r"(\+7|8)[\s\(]*(\d{3})[\s\)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s\(]*(?:доб\.?\s*(\d+))?"
    match = re.search(pattern, phone)
    if match:
        new_phone = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"
        if match.group(6):
            new_phone += f" доб.{match.group(6)}"
        return new_phone
    return phone

# логика из задания 1 и 2 проверка ключевых слов
def has_keywords(text: str, keywords: list) -> bool:
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)