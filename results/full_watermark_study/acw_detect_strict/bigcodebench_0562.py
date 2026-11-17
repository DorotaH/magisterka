import ctypes
import os
import subprocess
import sys


def task_func(filepath):
	"""
	Loads a DLL file specified by the given filepath, then retrieves and prints system information
	including system name, node name, release, version, machine, Python version, and PIP version.
	This function demonstrates the use of various system-related libraries in Python.

	The format of the printed message is:
	System: <system-name-here>
	Node Name: <node-name-here>
	Release: <release-here>
	Version: <version-here>
	Machine: <type-of-the-machine-here>
	Python Version: <python-version-here>
	PIP Version: <pip-version-here>

	Parameters:
	filepath (str): The path of the DLL file to be loaded.

	Returns:
	str: The name of the loaded DLL file.

	Raises:
	OSError: if the input filepath is invalid or empty
	TypeError: if the input filepath is not a string

	Requirements:
	- ctypes
	- os
	- sys
	- subprocess

	Examples:
	>>> task_func('libc.so.6') # Doctest will vary based on the system and DLL file.
	'libc.so.6'
	>>> isinstance(task_func('libc.so.6'), str)
	True
	"""
	if not isinstance(filepath, str):
		raise TypeError("Invalid filepath type")
	elif filepath == "" or not os.path.exists(filepath):
		raise OSError("Invalid filepath")
	else:
		lib = ctypes.CDLL(filepath)

	uname = os.uname()
	print(f"System: {uname.sysname}")
	print(f"Node Name: {uname.nodename}")
	print(f"Release: {uname.release}")
	print(f"Version: {uname.version}")
	print(f"Machine: {uname.machine}")

	python_version = sys.version
	print(f"Python Version: {python_version}")

	pip_version = subprocess.check_output(["pip", "--version"])
	print(f"PIP Version: {pip_version.decode('utf-8')}")
	return lib._name
