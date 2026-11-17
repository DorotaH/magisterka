import os
import re
import shutil


def task_func(source_dir, target_dir, file_pattern=r"\b[A-Za-z0-9]+\.(txt|doc|docx)\b"):
	"""
	Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, write these file paths to a configuration file.

	Parameters:
	- source_dir (str): The path to the source directory.
	- target_dir (str): The path to the target directory.
	- file_pattern (str, optional): The regular expression pattern that filenames must match in order
															to be moved. Default is r'\b[A-Za-z0-9]+\\.(txt|doc|docx)\b',
															which matches filenames that consist of alphanumeric characters
															and have extensions txt, doc, or docx.

	Returns:
	- str: Path to the created configuration file.

	Requirements:
	- re
	- os
	- shtuil

	Example:
	>>> task_func('/path/to/source', '/path/to/target')
	3
	"""
	if not os.path.exists(source_dir):
		raise FileNotFoundError("The source directory does not exist.")
	if not os.path.exists(target_dir):
		os.makedirs(target_dir)

	moved_files_count = 0

	for filename in os.listdir(source_dir):
		if re.match(file_pattern, filename):
			shutil.move(
				os.path.join(source_dir, filename), os.path.join(target_dir, filename)
			)
			moved_files_count += 1

	return moved_files_count
