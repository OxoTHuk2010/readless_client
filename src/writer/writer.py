from config.agent import AgentConfig
from pathlib import Path
import tempfile
import os

def write_metric_atomic(metric_content:str = None, file_path:Path = AgentConfig.EXPORTER_TEXTFILE_FILE) -> None:
    """
    Записывает метрику в файл атомарно
    """

    file_descriptor, temporary_file = tempfile.mkstemp(
        prefix=".os_release_",
        suffix=".prom",
        dir=AgentConfig.EXPORTER_TEXTFILE_DIR,
        text=True,
    )

    try:
        with os.fdopen(
            file_descriptor,
            "w",
            encoding="utf-8",
            ) as f:
            f.write(metric_content)
            f.flush()
            os.fsync(f.fileno())

        os.replace(temporary_file, file_path)
    except Exception as e:
        print(e)
    finally:
        os.remove(temporary_file)