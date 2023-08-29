"""Генератор приветствий."""


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя

    Returns:
        str: Текст приветствия
    """
    capitalized_name = ' '.join(word.capitalize() for word in name.split())
    return 'Привет, {0}'.format(capitalized_name)
