import shutil
import pathlib


def task_func(source_path, destination_path):
	"""
	Lists files in the specified source directory without descending into subdirectories and copies them to a
	destination directory.

	Parameters:
	- source_path (str):      The source directory path to analyze. Must be an existing, accessible directory.
	- destination_path (str): The destination directory path where files will be copied.
							If it does not exist, this function will create it.

	Returns:
	Tuple[str, List[str]]: A tuple containing the name of the source directory and a list of filenames (not
						full paths) that were copied.

	Raises:
	- ValueError: If source_path does not exist or is not a directory.

	Requirements:
	- shutil
	- pathlib

	Example:
	>>> x = task_func('/Docs/src/Scripts')
	>>> type(x)
	<class 'tuple'>
	>>> x
	('Scripts', ['file_1_in_scripts_dir.txt', 'file_2_in_scripts_dir.txt'])
	"""
	source_path = pathlib.Path(source_path).resolve()
	destination_path = pathlib.Path(destination_path).resolve()

	if not (source_path.exists() and source_path.is_dir()):
		raise ValueError("source_path must be an existing directory.")

	destination_path.mkdir(parents=True, exist_ok=True)

	results = []
	for entry in source_path.iterdir():
		if entry.is_file():
			results.append(str(entry.name))
			shutil.copy(str(entry), str(destination_path))
	return (source_path.name, results)
