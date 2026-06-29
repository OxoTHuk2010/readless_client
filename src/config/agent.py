import os
from pathlib import Path


class AgentConfig:
    """
    Дефолтные пути агента для ручного запуска без внешней конфигурации.

    Позже эти значения стоит читать из конфигурационного файла, но сейчас
    класс оставлен простым, чтобы не усложнять первый сбор `/etc/os-release`.
    """

    OS_RELEASE_FILE = Path("/etc/os-release")
    EXPORTER_TEXTFILE_DIR = "/etc/node_exporter/"
    EXPORTER_TEXTFILE_FILE = Path(
        os.path.join(
        EXPORTER_TEXTFILE_DIR,
        "os_release.prom",
        )
    )
    PROFILE_FILE = Path("profile/baseline.yaml")
