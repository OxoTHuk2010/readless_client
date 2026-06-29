from src.collectors.os import check_os_release
from src.metrics.renderer import build_prometheus_metric
from src.metrics.writer import write_metric_atomic


def main() -> None:
    os_info = check_os_release()
    metric = build_prometheus_metric(os_info)
    write_metric_atomic(metric)

if __name__ == '__main__':
    main()
