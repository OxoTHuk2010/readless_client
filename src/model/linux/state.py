from typing import Literal

from src.model.linux.base import ConfigModel
from src.model.linux.linux import LinuxConfig

class StateConfig(ConfigModel):
    """Корневая модель файла с ожидаемым состоянием ВМ."""

    schema_version: Literal[1]
    """Версия схемы конфигурации; меняется только при breaking change."""

    linux: LinuxConfig
    """Ожидаемое состояние Linux-слоя."""
