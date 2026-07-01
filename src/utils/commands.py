import subprocess
from src.model.result import CommandResilt

def run_command(
        command: list[str],
        timeout: int = 5,
) -> CommandResilt:
    try:
        complited = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout,
        )

    except FileNotFoundError:
        return CommandResilt(
            return_code=None,
            stdout="",
            stderr="",
            error=f"Команда не найдена: {command[0]}",
        )
    
    except subprocess.TimeoutExpired:
        return CommandResilt(
            return_code=None,
            stdout="",
            stderr="",
            error=f"Превышено время ожидания: {command[0]}",
        )
    
    except OSError as e:
        return CommandResilt(
            return_code=None,
            stdout="",
            stderr="",
            error=str(e),            
        )
    
    return CommandResilt(
        return_code=complited.returncode,
        stdout=complited.stdout.strip(),
        stderr=complited.stderr.strip(),
    )
