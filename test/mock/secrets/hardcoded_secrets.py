from typing import Any, NotRequired, TypedDict, cast

from mu_pipelines_interfaces.config_types.secrets.secrets_config import (
    SecretsConfigItem,
)
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider
from mu_pipelines_interfaces.modules.secrets_module_interface import (
    SecretsModuleInterface,
)


class AdditionalAttributes(TypedDict):
    value: NotRequired[str]


class HardcodedSecrets(SecretsModuleInterface):
    value: str

    def __init__(
        self, config: SecretsConfigItem, configuration_provider: ConfigurationProvider
    ):
        super().__init__(config, configuration_provider)
        assert "additional_attributes" in config
        additional_attributes = cast(
            AdditionalAttributes, config["additional_attributes"]
        )

        assert "value" in additional_attributes

        if additional_attributes["value"] is not None:
            self.value = additional_attributes["value"]

    def get(self, context: Any) -> Any:
        return self.value
