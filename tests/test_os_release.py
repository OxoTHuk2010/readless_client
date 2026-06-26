from pathlib import Path

from src.checks.os import read_os_release

def test_read_os_release(
        os_release_file: Path,
        expected_os_release: dict[str, str],
) -> None:
    result = read_os_release(os_release_file)

    assert result == expected_os_release
