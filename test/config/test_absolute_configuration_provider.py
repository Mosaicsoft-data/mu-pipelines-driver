from mu_pipelines_interfaces.config_types.global_properties.global_properties import (
    GlobalProperties,
)
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider

from mu_pipelines_driver.config.absolute_configuration_provider import (
    AbsoluteConfigurationProvider,
)


def test_AbsoluteConfigurationProvider():
    config_provider: ConfigurationProvider = AbsoluteConfigurationProvider(
        job_config_path="test/config/test_job_config.json",
        global_properties_path="test/config/test_global_properties.json",
        connection_config_path="test/config/test_connection_properties.json",
    )

    assert config_provider.job_config[0]["execution"][0]["type"] == "CSVReadCommand"
    assert config_provider.job_config[0]["destination"][0]["type"] == "jdbc"

    assert config_provider.global_properties["library"] == "Mock"

    assert config_provider.connection_config["connections"][0]["type"] == "postgres"


def test_AbsoluteConfigurationProvider_load_supporting_artifact():
    config_provider: ConfigurationProvider = AbsoluteConfigurationProvider(
        job_config_path="test/config/test_job_config.json",
        global_properties_path="test/config/test_global_properties.json",
        connection_config_path="test/config/test_connection_properties.json",
    )

    supporting_artifact: GlobalProperties | None = (
        config_provider.load_job_supporting_artifact(
            "test_global_properties.json", GlobalProperties
        )
    )

    assert supporting_artifact is not None
    assert supporting_artifact["library"] == "Mock"
