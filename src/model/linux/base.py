from pydantic import BaseModel, ConfigDict

class ConfigModel(BaseModel):
    """
    Базовый класс для всех моделей конфигурации.

    `extra="forbid"` запрещает неизвестные поля. Это важно для YAML/JSON
    конфигурации: опечатка в ключе должна падать при валидации, а не тихо
    игнорироваться.
    """
    model_config = ConfigDict(extra="forbid")
