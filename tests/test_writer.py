from pathlib import Path

from src.writer.writer import write_metric_atomic


def test_write_metric_atomic_creates_file(metric_file: Path) -> None:
    write_metric_atomic("metric 1\n", metric_file)

    assert metric_file.read_text(encoding="utf-8") == "metric 1\n"


def test_write_metric_atomic_replaces_existing_file(metric_file: Path) -> None:
    write_metric_atomic("old 1\n", metric_file)
    write_metric_atomic("new 1\n", metric_file)

    assert metric_file.read_text(encoding="utf-8") == "new 1\n"
    assert not list(metric_file.parent.glob(".os_release_*.prom"))
