from src.model.linux.base import ConfigModel
from pydantic import Field
from typing import Literal

class KernelModuleRule(ConfigModel):
    names: list[str] = Field(min_length=1)

    state: Literal[
        "present",
        "absent",
    ]
