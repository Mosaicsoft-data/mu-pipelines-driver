from typing import Any, cast

from mu_pipelines_interfaces.config_types.execute_config import ExecuteConfig
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider
from mu_pipelines_interfaces.execute_module_interface import ExecuteModuleInterface


class MockLoadCSVConfig(ExecuteConfig):
    data: dict


class LoadCSV(ExecuteModuleInterface):
    def __init__(
        self, config: MockLoadCSVConfig, configuration_provider: ConfigurationProvider
    ):
        super().__init__(config, configuration_provider)
        if "data" not in config:
            raise KeyError("[data] not found in LoasCSV config")

    def execute(self, context: Any) -> Any:
        return cast(MockLoadCSVConfig, self._config)["data"]
