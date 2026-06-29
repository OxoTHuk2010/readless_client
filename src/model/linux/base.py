from pydantic import BaseModel, ConfigDict

class ConfigModel(BaseModel):
    """
    Базовая модель конфигурации.
    
    extra="firbid" запрещает неизвестные поля.
    Это позволит обноружить опечатки в YAML.
    """
    model_config = ConfigDict(extra="forbid")
