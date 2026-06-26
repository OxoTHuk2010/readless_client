import os
from pathlib import Path


class AgentConfig:
    """
    Класс для хранения дефолтной конфигурации агента.
    """

    OS_RELEASE_FILE = Path("/etc/os-release")
    EXPORTER_TEXTFILE_DIR = "/etc/node_exporter/"
    EXPORTER_TEXTFILE_FILE = Path(
        os.path.join(
        EXPORTER_TEXTFILE_DIR,
        "os_release.prom",
        )
    )
