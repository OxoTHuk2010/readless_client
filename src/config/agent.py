from pathlib import Path
import os

class AgentConfig():
    """
    Класс для хранения конфигурации агента
    """
    OS_RELEASE_FILE = Path("/etc/os-release")
    EXPORTER_TEXTFILE_DIR = "/var/lib/node_exporter/"
    
    EXPORTER_TEXTFILE_FILE= os.path.join(
    EXPORTER_TEXTFILE_DIR,
    'os_release.prom',
    )
