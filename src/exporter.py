from checks import check_os_release
from export import build_prometheus_metric
from writer import write_metric
def main():
    os_info = check_os_release()
    metric = build_prometheus_metric(os_info)
    write_metric(metric)

if __name__ == '__main__':
    main()