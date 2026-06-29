from src.model.linux.base import ConfigModel
from typing import Literal

class SelinuxRule(ConfigModel):
    """Модель параметров Selinux"""
    state: Literal[
        "disabled",
        "enforcing",
        "permissive",
        ]
