import os
import shutil
import subprocess
from glob import glob


def task_func(src_folder, dst_folder):
	"""Compress all files in the specified source folder and move the compressed files to a destination folder.
	This operation is executed as a background process using the 'gzip' command.

	Parameters:
	src_folder (str): The path of the source folder containing the files to be compressed.
	dst_folder (str): The path of the destination folder where the compressed files will be moved.

	Returns:
	dict: A dictionary containing:
			- 'success': A boolean indicating if all files were compressed and moved successfully.
			- 'message': A descriptive message about the operation's result.
			- 'failed_files': A list of filenames that failed to compress or move.

	Requirements:
	- subprocess
	- os
	- shutil
	- glob
	- gzip

	Example:
	>>> import tempfile
	>>> import os
	>>> src_folder = tempfile.mkdtemp()
	>>> dst_folder = tempfile.mkdtemp()
	>>> for i in range(3):
	...     with open(os.path.join(src_folder, f'file{i}.txt'), 'w') as f:
	...         _ = f.write(f'This is file {i}.')
	>>> task_func(src_folder, dst_folder)
	{'success': True, 'message': 'All files compressed and moved successfully.', 'failed_files': []}
	"""
	# Check if source and destination folders exist
	if not os.path.isdir(src_folder):
		raise ValueError(f"Source folder '{src_folder}' does not exist.")
	if not os.path.isdir(dst_folder):
		raise ValueError(f"Destination folder '{dst_folder}' does not exist.")

	processes = []
	failed_files = []

	# Compress files in a background process
	for file in glob(os.path.join(src_folder, "*")):
		process = subprocess.Popen(["gzip", file])
		processes.append((process, file))

	# Wait for all processes to complete
	for process, file in processes:
		retcode = process.wait()
		if retcode != 0:
			failed_files.append(os.path.basename(file))

	# Move compressed files to destination folder
	for file in glob(os.path.join(src_folder, "*.gz")):
		try:
			shutil.move(file, dst_folder)
		except Exception:
			failed_files.append(os.path.basename(file))

	if failed_files:
		return {
			"success": False,
			"message": "Some files failed to compress or move.",
			"failed_files": failed_files,
		}
	else:
		return {
			"success": True,
			"message": "All files compressed and moved successfully.",
			"failed_files": [],
		}
