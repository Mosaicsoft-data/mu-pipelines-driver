from mu_pipelines_interfaces.config_types.connection_properties import (
    ConnectionConfig,
    ConnectionProperties,
)
from mu_pipelines_interfaces.config_types.job_config import DestinationConfig
from mu_pipelines_interfaces.configuration_provider import GlobalProperties

from mu_pipelines_driver.ioc.import_mapped_class import ClassModuleMappingItem


class DestinationModuleMappingItem(ClassModuleMappingItem):
    type: str


DESTINATION_MODULE_MAPPING: list[DestinationModuleMappingItem] = [
    {
        "type": "jdbc-postgres-mock",
        "module_path": "test.mock.save_to_table.save_to_table",
        "class_name": "SaveToTable",
    },
]


def find_destination_module_mapping(
    dest_config: DestinationConfig,
    global_properties: GlobalProperties,
    connection_properties: ConnectionProperties,
) -> DestinationModuleMappingItem | None:
    temp_type: str = dest_config["type"]

    # When the destination depends on a connection_config in connection_properties
    # TODO determine whether this is needed in the mapping
    if "connection_details" in dest_config:
        connection_config: ConnectionConfig = next(
            CONN
            for CONN in connection_properties["connections"]
            if CONN["name"] == dest_config["connection_details"]
        )
        connection_config_type: str = connection_config["type"]
        temp_type = "{temp_type}-{connection_config_type}".format(
            temp_type=temp_type, connection_config_type=connection_config_type
        )

    mapping_type: str = "{type}-{library_type}".format(
        type=temp_type, library_type=global_properties["library"]
    )

    return next(
        (
            MAPPING
            for MAPPING in DESTINATION_MODULE_MAPPING
            if MAPPING["type"] == mapping_type.lower()
        ),
        None,
    )
