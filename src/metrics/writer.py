import os
import tempfile
from pathlib import Path

from src.config.agent import AgentConfig


def write_metric_atomic(
    metric_content: str,
    file_path: Path = AgentConfig.EXPORTER_TEXTFILE_FILE,
) -> None:
    """
    Атомарно записывает Prometheus textfile-метрику.

    Safety boundary:
    функция меняет состояние файловой системы. Она пишет только в переданный
    `file_path` и использует временный файл в том же каталоге, чтобы
    `node_exporter` не прочитал частично записанный файл.
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
        # На Linux временный файл должен быть читаем `node_exporter` после
        # replace. В Windows `fchmod` отсутствует, поэтому локальные тесты
        # пропускают этот POSIX-only шаг.
        if hasattr(os, "fchmod"):
            os.fchmod(file_descriptor, 0o644)
        
        with os.fdopen(
            file_descriptor,
            "w",
            encoding="utf-8",
        ) as f:
            f.write(metric_content)
            f.flush()
            os.fsync(f.fileno())

        # replace атомарен внутри одной файловой системы.
        os.replace(temporary_path, target_path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()
