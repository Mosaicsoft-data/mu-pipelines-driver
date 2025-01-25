from test.mock.load_csv.load_csv import LoadCSV
from test.mock.save_to_table.save_to_table import SaveToTable

from mu_pipelines_interfaces.config_types.job_config import JobConfigItem
from mu_pipelines_interfaces.configuration_provider import ConfigurationProvider

from mu_pipelines_driver.config.absolute_configuration_provider import (
    AbsoluteConfigurationProvider,
)
from mu_pipelines_driver.ioc.ioc_container import IOCContainer


def test_ioc_container() -> None:
    config_provider: ConfigurationProvider = AbsoluteConfigurationProvider(
        job_config_path="test/config/test_job_config.json",
        global_properties_path="test/config/test_global_properties.json",
        connection_config_path="test/config/test_connection_properties.json",
    )
    job_config_item: JobConfigItem = config_provider.job_config.pop()
    ioc_container: IOCContainer = IOCContainer(job_config_item, config_provider)

    assert ioc_container.execute_modules.__len__() == 1
    assert ioc_container.destination_modules.__len__() == 1

    for exec_module in ioc_container.execute_modules:
        assert isinstance(exec_module, LoadCSV)

    for dest_module in ioc_container.destination_modules:
        assert isinstance(dest_module, SaveToTable)
