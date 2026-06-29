def escape_prometheus_label(value: str) -> str:
    """
    Экранирует строку для использования
    в label метрики Prometheus
    """

    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace('"', '\\"')
    )

def build_prometheus_metric(os_info: dict[str, str]) -> str:
    """Формирует метрику для OS_INFO в формате Prometheus"""

    labels = {
        "id": os_info.get("ID", "unknown"),
        "pretty_name": os_info.get("PRETTY_NAME", "unknown"),
    }

    labels_string = ",".join(
        '{}="{}"'.format(
            key,
            escape_prometheus_label(value),
        )
        for key, value in labels.items()
    )

    return (
        '# HELP node_os_release_info Information from /etc/os-release.\n'
        '# TYPE node_os_release_info gauge\n'
        'node_os_release_info{{{}}} 1\n'.format(labels_string)
    )


