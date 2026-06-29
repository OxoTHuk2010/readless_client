from pathlib import Path

import yaml
from pydantic import ValidationError

from src.model.linux.state import StateConfig

class ConfigurationError(RuntimeError):
    pass

def load_config(path:str | Path) -> StateConfig:
    config_path = Path(path)

    if not config_path.exists():
        raise ConfigurationError(
            f"Файл не найден: {config_path}"
        )

    if not config_path.is_file():
        raise ConfigurationError(
            f"Файл не найден"
        )
    
    try:
        with config_path.open("r", encoding="utf-8") as file:
            raw_config = yaml.safe_load(file)

    except yaml.YAMLError as e:
        raise ConfigurationError(
            f"Ошибка синтаксиса YAML: {e}"
        ) from e
    
    except OSError as e:
        raise ConfigurationError(
            f"Не удалось прочитать файл: {e}"
        ) from e
    
    if raw_config is None:
        raise ConfigurationError(
            f"Файл конфигурации пуст"
        )
    
    if not isinstance(raw_config, dict):
        raise ConfigurationError(
            "Корневой элемент YAML должен быть словарём"
        )
    
    try:
        config = StateConfig.model_validate(
            raw_config
        )

    except ValidationError as e:
        raise ConfigurationError(
            f"Ошибка валидации конфигурации:\n{e}"
        ) from e
    
    return config
