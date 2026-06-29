from src.model.linux.base import ConfigModel
from pydantic import Field
from typing import Literal

class KernelModuleRule(ConfigModel):
    """Ожидания по наличию или отсутствию kernel modules."""

    names: list[str] = Field(min_length=1)
    """Имена kernel modules, к которым применяется одно ожидание."""

    state: Literal[
        "present",
        "absent",
    ]
    """Ожидаемое состояние модулей: загружены или отсутствуют."""
