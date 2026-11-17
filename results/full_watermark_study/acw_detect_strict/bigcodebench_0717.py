import sys
from configparser import ConfigParser

# Constants
PATH_TO_APPEND = "/path/to/whatever"
CONFIG_FILE = "/path/to/config.ini"


def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
	"""
	Add a specific path to sys.path and update a configuration file with this path.

	Parameters:
	- path_to_append (str): The path to append to sys.path. Default is '/path/to/whatever'.
	- config_file (str): The path to the config file to update. Default is '/path/to/config.ini'.

	Returns:
	- config (object): The object contains the updated configuration.
	- config_file (str): The path to the configuration file that was just modified.

	Requirements:
	- sys
	- configparser.ConfigParser

	Example:
	>>> config = task_func('/path/to/new_directory', '/path/to/new_config.ini')
	>>> 'path_to_append' in config['DEFAULT']
	True
	"""
	if isinstance(path_to_append, list):
		for path in path_to_append:
			sys.path.append(path)
	else:
		sys.path.append(path_to_append)

	config = ConfigParser()

	# Create the file if it doesn't exist
	if not os.path.exists(config_file):
		open(config_file, "a").close()

	config.read(config_file)
	path_str = (
		",".join(path_to_append) if isinstance(path_to_append, list) else path_to_append
	)
	config.set("DEFAULT", "path_to_append", path_str)

	with open(config_file, "w") as file:
		config.write(file)

	return config, config_file
