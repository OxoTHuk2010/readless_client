from pathlib import Path

from src.config.agent import AgentConfig


def read_os_release(file_path: Path = AgentConfig.OS_RELEASE_FILE) -> dict[str, str]:
    """
    Читает `/etc/os-release` и возвращает пары `KEY=VALUE` в виде словаря.

    Args:
        file_path: Путь к файлу формата os-release.

    Returns:
        Словарь с ключами из файла os-release.
    """

    os_info: dict[str, str] = {}

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Пустые строки и комментарии не являются фактами ОС.
            if not line or line.startswith("#"):
                continue
            
            # Значения вроде URL могут содержать "=" после первого разделителя.
            key, separator, value = line.partition("=")

            if not separator:
                continue

            if (
                len(value) >= 2
                and value[0] == value[-1]
                and value[0] in ('"', "'")
            ):
                # os-release обычно хранит значения в кавычках; в метрики и
                # проверки передаём уже нормализованное значение.
                value = value[1:-1]

            os_info[key] = value

    return os_info


def check_os_release(file_path: Path = AgentConfig.OS_RELEASE_FILE) -> dict[str, str]:
    """
    Возвращает сведения об ОС для основного сценария сбора.

    Обёртка оставлена отдельно от parser-функции, чтобы дальнейшие проверки
    могли добавлять обработку ошибок, статусы сбора и диагностику.
    """

    return read_os_release(file_path)

