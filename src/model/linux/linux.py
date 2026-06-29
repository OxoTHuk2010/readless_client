from pydantic import Field
from src.model.linux.base import ConfigModel
from src.model.linux.selinux.selinux import SelinuxRule
from src.model.linux.selinux.services import ServicesRule
from src.model.linux.selinux.kernel_modules import KernelModuleRule

class LinuxConfig(ConfigModel):
    selinux: SelinuxRule | None = None

    services: list[ServicesRule] = Field(
        default_factory=list
    )

    kernel_modules: list[KernelModuleRule] = Field(
        default_factory=list
    )
