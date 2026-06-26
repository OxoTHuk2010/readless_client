from pathlib import Path
import pytest

@pytest.fixture
def os_release_content() -> str:
    """Стандартное содержимое файла /etc/os-release"""

    return """
NAME="RED OS"
VERSION="MUROM (7.3)"
PLATFORM_ID="platform:el7"
ID="redos"
ID_LIKE="rhel centos fedora"
VERSION_ID="7.3"
PRETTY_NAME="RED OS MUROM (7.3)"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:redos:redos:7"
HOME_URL="https://redos.red-soft.ru/"
BUG_REPORT_URL="https://support.red-soft.ru/"
EDITION="Certified"
""".lstrip()


@pytest.fixture
def os_release_file(
    tmp_path: Path,
    os_release_content: str,
) -> Path:
    """Файл /etc/os-release с заданным содержимым"""

    file_path = tmp_path / "os-release"
    file_path.write_text(
        os_release_content,
        encoding="utf-8",
        )

    return file_path

@pytest.fixture
def metric_file(tmp_path: Path) -> Path:
    """Файл с метрикой"""

    file_path = tmp_path / "metric.prom"
    return file_path

@pytest.fixture
def expected_os_info() -> dict[str, str]:
    """Ожидаемый словарь с информацией о системе"""

    return {
        "NAME": "RED OS",
        "VERSION": "MUROM (7.3)",
        "PLATFORM_ID": "platform:el7",
        "ID": "redos",
        "ID_LIKE": "rhel centos fedora",
        "VERSION_ID": "7.3",
        "PRETTY_NAME": "RED OS MUROM (7.3)",
        "ANSI_COLOR": "0;31",
        "CPE_NAME": "cpe:/o:redos:redos:7",
        "HOME_URL": "https://redos.red-soft.ru/",
        "BUG_REPORT_URL": "https://support.red-soft.ru/",
        "EDITION": "Certified",
    }


@pytest.fixture
def expected_os_release(expected_os_info: dict[str, str]) -> dict[str, str]:
    """Ожидаемый результат парсинга /etc/os-release."""

    return expected_os_info
