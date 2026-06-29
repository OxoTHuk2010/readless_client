from pydantic import Field
from typing import Literal
from src.model.linux.base import ConfigModel
from src.model.linux.linux import LinuxConfig

class StateConfig(ConfigModel):
    schema_version: Literal[1]
    linux: LinuxConfig
