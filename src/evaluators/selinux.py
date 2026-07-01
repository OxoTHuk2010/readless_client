from src.config.loader import StateConfig
from src.model.result import CheckResult, CheckStatus

def validate_selinux_config(selinux_state:str, config:StateConfig) -> CheckResult:
    selinux_state = selinux_state
    
    selinux_config = config.get('selinux')

    result = CheckResult

    result.checker = "selinux"
    result.expected = selinux_config
    result.actual = selinux_state

    
    if selinux_state == selinux_config['state']:
        result.status = CheckStatus.PASSED

    return result

