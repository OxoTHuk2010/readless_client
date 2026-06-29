from src.model.linux.base import ConfigModel
from pydantic import Field, model_validator
from typing import Literal

class ServicesRule(ConfigModel):
    """Ожидания по одному или нескольким systemd-сервисам."""

    names: list[str] = Field(min_length=1)
    """Имена сервисов, к которым применяется одно ожидание."""

    state: Literal[
        "started",
        "stopped",
    ] | None = None
    """Ожидаемое runtime-состояние сервиса; можно не задавать."""

    enabled: bool | None = None
    """Ожидаемый автозапуск сервиса; можно не задавать."""

    @model_validator(mode="after")
    def validate_expected_state(self) -> "ServicesRule":
        """
        Проверяет, что правило действительно содержит хотя бы одно ожидание.

        Без `state` и `enabled` правило ничего не проверяет, поэтому такая
        конфигурация считается ошибкой профиля.
        """
        if self.state is None and self.enabled is None:
            raise ValueError(
                "Для services необходимо указать "
                "хотя бы state или enabled"
            )

        return self
