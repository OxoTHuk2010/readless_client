from pathlib import Path
from src.utils.commands import run_command
from src.utils.validate_path import validate_path_file
from src.model.result import CheckResult, CheckStatus, CommandResilt

def read_selinux_config(
        path: Path = Path("/etc/selinux/config"),
) -> tuple[str | None, str | None]:
    path = validate_path_file(path)

    try:
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith('#'):
                    continue
                if 'SELINUX' in line:
                    value = line.split('=')

                    return value[1], None

    
    except OSError as e:
        return None, f"Не удалось прочитать {path}: {e}"
    
    return None, f"в {path} не найден параметр SELINUX"
