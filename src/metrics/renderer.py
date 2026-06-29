def escape_prometheus_label(value: str) -> str:
    """
    Экранирует строку для безопасного использования в label Prometheus.

    Prometheus требует экранировать обратный слеш, перевод строки и двойную
    кавычку внутри label value.
    """

    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace('"', '\\"')
    )

def build_prometheus_metric(os_info: dict[str, str]) -> str:
    """
    Формирует минимальную info-метрику по данным `/etc/os-release`.

    Args:
        os_info: Словарь, полученный из `read_os_release`.

    Returns:
        Строка в формате Prometheus text exposition.
    """

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


