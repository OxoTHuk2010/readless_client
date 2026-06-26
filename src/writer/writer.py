import os
import tempfile
from pathlib import Path

from src.config.agent import AgentConfig


def write_metric_atomic(
    metric_content: str,
    file_path: Path = AgentConfig.EXPORTER_TEXTFILE_FILE,
) -> None:
    """
    Записывает метрику в файл атомарно
    """

    target_path = Path(file_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    file_descriptor, temporary_file = tempfile.mkstemp(
        prefix=".os_release_",
        suffix=".prom",
        dir=target_path.parent,
        text=True,
    )
    temporary_path = Path(temporary_file)

    try:
        with os.fdopen(
            file_descriptor,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(metric_content)
            f.flush()
            os.fsync(f.fileno())

        os.replace(temporary_path, target_path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()
