from src.model.linux.base import ConfigModel
from typing import Literal

class SelinuxRule(ConfigModel):
    """Ожидаемый runtime-режим SELinux на ВМ."""

    state: Literal[
        "disabled",
        "enforcing",
        "permissive",
        ]
