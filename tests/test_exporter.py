from pathlib import Path

from src import exporter
from src.config.agent import AgentConfig


def test_exporter_main_writes_metric(
    monkeypatch,
    os_release_file: Path,
    metric_file: Path,
) -> None:
    monkeypatch.setattr(AgentConfig, "OS_RELEASE_FILE", os_release_file)
    monkeypatch.setattr(AgentConfig, "EXPORTER_TEXTFILE_FILE", metric_file)
    monkeypatch.setattr(exporter, "check_os_release", lambda: {"ID": "redos", "PRETTY_NAME": "RED OS"})
    monkeypatch.setattr(exporter, "write_metric_atomic", lambda metric: metric_file.write_text(metric, encoding="utf-8"))

    exporter.main()

    content = metric_file.read_text(encoding="utf-8")
    assert "node_os_release_info" in content
    assert 'id="redos"' in content
