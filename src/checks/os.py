from pathlib import Path

from src.config.agent import AgentConfig


def read_os_release(file_path: Path = AgentConfig.OS_RELEASE_FILE) -> dict[str, str]:
    """
    Читает файл OS_RELEASE_FILE и возвращает его содержимое
    в виде словаря.
    """

    os_info: dict[str, str] = {}

    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Пропускаем пустые строки и коментарии
            if not line or line.startswith("#"):
                continue
            
            # Разделяем строку только по первому символу =
            key, separator, value = line.partition("=")

            if not separator:
                continue

            if (
                len(value) >= 2
                and value[0] == value[-1]
                and value[0] in ('"', "'")
            ):
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

