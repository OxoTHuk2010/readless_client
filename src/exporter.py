from src.collectors.os import check_os_release
from src.metrics.renderer import build_prometheus_os_metric, build_prometheus_metric
from src.metrics.writer import write_metric_atomic
from src.collectors.baseline.selinux import read_selinux_config
from src.evaluators.selinux import validate_selinux_config

from src.config.loader import ConfigurationError, load_config
from src.config.agent import AgentConfig


def main() -> None:
    """Выполняет один цикл сбора ОС и публикации textfile-метрики."""

    try:
        config = load_config(AgentConfig.PROFILE_FILE)
    
    except ConfigurationError as e:
        print(f"Ошибка загрузки конфигурации: {e}")

    selinux = validate_selinux_config(read_selinux_config(), config)
    build_prometheus_metric('baseline_configure', 'gauge', 'selinux', selinux)
    write_metric_atomic(build_prometheus_metric)

    os_info = check_os_release()
    metric = build_prometheus_os_metric(os_info)
    write_metric_atomic(metric)

if __name__ == '__main__':
    main()
