from aerie_cli.aerie_host import AerieHostConfiguration
from aerie_cli.persistent import PersistentConfigurationManager

import json

def find_configuration(configuration_identifier: str) -> AerieHostConfiguration:
    """Find a configuration by name or path.
    
    configuration_identifier (str): The name or path of a configuration. Paths should be to a configuration json file.

    Raises:
        ValueError
        FileNotFoundError

    Returns:
        AerieHostConfiguration
    """
    # search for configuration by name
    for persistent_configuration in PersistentConfigurationManager.get_configurations():
        if persistent_configuration.name != configuration_identifier:
            continue
        return persistent_configuration

    # search for configuration by path
    with open(configuration_identifier, 'r') as fid:
        found_configuration = json.load(fid)
    
    return AerieHostConfiguration.from_dict(found_configuration)