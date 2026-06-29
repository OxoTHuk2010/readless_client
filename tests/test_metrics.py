from src.metrics.renderer import build_prometheus_metric, escape_prometheus_label


def test_escape_prometheus_label() -> None:
    assert escape_prometheus_label('RED "OS"\\test\nline') == 'RED \\"OS\\"\\\\test\\nline'


def test_build_prometheus_metric(expected_os_info: dict[str, str]) -> None:
    metric = build_prometheus_metric(expected_os_info)

    assert "# HELP node_os_release_info Information from /etc/os-release." in metric
    assert "# TYPE node_os_release_info gauge" in metric
    assert 'id="redos"' in metric
    assert 'pretty_name="RED OS MUROM (7.3)"' in metric
    assert metric.endswith(" 1\n")


def test_build_prometheus_metric_uses_unknown_for_missing_values() -> None:
    metric = build_prometheus_metric({})

    assert 'id="unknown"' in metric
    assert 'pretty_name="unknown"' in metric
