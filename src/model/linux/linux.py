from typing import Any
from pydantic import Field, field_validator
from src.model.linux.base import ConfigModel
from src.model.linux.selinux.selinux import SelinuxRule
from src.model.linux.selinux.services import ServicesRule
from src.model.linux.selinux.kernel_modules import KernelModuleRule

class LinuxConfig(ConfigModel):
    """Набор правил, которые описывают ожидаемое состояние Linux-хоста."""

    selinux: SelinuxRule | None = None
    """Ожидаемый режим SELinux; `None` означает, что проверка не задана."""

    services: list[ServicesRule] = Field(
        default_factory=list
    )
    """Ожидания по systemd-сервисам в рамках текущего профиля проверки."""

    kernel_modules: list[KernelModuleRule] = Field(
        default_factory=list
    )
    """Ожидания по загруженным или отсутствующим kernel modules."""

    @field_validator("services", "kernel_modules", mode="before")
    @classmethod
    def normalize_rule_list(cls, value: Any) -> Any:
        if value is None:
            return []
        if isinstance(value, dict):
            return [value]
        return value
