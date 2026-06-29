from src.model.linux.base import ConfigModel
from pydantic import Field, model_validator
from typing import Literal

class ServicesRule(ConfigModel):
    """Модель параметров systemd"""
    names: list[str] = Field(min_length=1)

    state: Literal[
        "started",
        "stopped",
    ] | None = None

    enabled: bool | None = None

    @model_validator(mode="after")
    def validate_expected_state(self) -> "ServicesRule":
        if self.state is None and self.enabled is None:
            raise ValueError(
                "Для services необходимо указать "
                "хотя бы state или enabled"
            )

        return self
