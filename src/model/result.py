from dataclasses import dataclass
from enum import Enum
from typing import Any

class CheckStatus(str, Enum):
    PASSED = "passed"
    FAILED = "failed"
    ERROR = "error"

@dataclass(frozen=True)
class CheckResult:
    checker: str
    target: str | None
    property: str | None
    expected: Any
    actual: Any | None
    status: CheckStatus
    error: str | None = None

@dataclass(frozen=True)
class CommandResilt:
    return_code: int | None
    stdout: str
    stderr: str
    error: str | None = None
