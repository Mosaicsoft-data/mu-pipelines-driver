from typing import Any

from mu_pipelines_interfaces.config_types.destination_config import DestinationConfig
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider
from mu_pipelines_interfaces.destination_module_interface import (
    DestinationModuleInterface,
)


class SaveToTable(DestinationModuleInterface):
    def __init__(
        self, config: DestinationConfig, configuration_provider: ConfigurationProvider
    ):
        super().__init__(config, configuration_provider)

    def save(self, df: Any, context: Any) -> None:
        print(df)
