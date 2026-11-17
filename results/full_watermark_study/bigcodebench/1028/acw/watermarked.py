import subprocess
import time
import json
import platform

LOGFILE_PATH = "logfile.log"


def task_func(interval, duration):
	"""
	Monitors and logs CPU usage at specified intervals over a given duration.

	Parameters:
	interval (int): The frequency, in seconds, at which CPU usage data is captured. Must be greater than zero.
	duration (int): The total duration, in seconds, for which CPU usage is monitored. Must be greater than zero.

	Returns:
	str: Path to the log file where CPU usage data is saved. Returns None if an IOError occurs during file operations.

	Raises:
	ValueError: If either 'interval' or 'duration' is less than or equal to zero.

	Requirements:
	- subprocess
	- time
	- json
	- platform

	Note: 
	Actual run time of the function may slightly exceed the specified 'duration' due to processing time and system response delay.
	The function records the CPU usage percentage at regular intervals for a specified duration.
	The data is captured every 'interval' seconds until the 'duration' is reached or exceeded.
	Each record includes a timestamp and the CPU usage percentage at that moment.
	The data is saved in JSON format in a log file named 'logfile.log'.
	The function supports different commands for CPU usage monitoring on Windows and Unix/Linux platforms.
	
	Example:
	>>> task_func(5, 60)
	'logfile.log'
	"""
	if 0 >= interval or duration <= 0:
		raise ValueError("Interval and duration must be greater than zero.")

	start_time = time.time()
	try:
		with open(LOGFILE_PATH, "w", encoding="utf-8") as logfile:
			while duration >= time.time() - start_time:
				operation_start_time = time.time()

				# Check the operating system
				if platform.system() == "Windows":
					# Windows command for CPU usage
					command = [
						"typeperf",
						"\\Processor(_Total)\\% Processor Time",
						"-sc",
						"1",
					]
				else:
					# Unix/Linux command for CPU usage
					command = ["top", "-b", "-n1"]

				output = subprocess.check_output(command)
				cpu_usage_line = (
					output.decode("utf-8").split("\n")[2]
					if platform.system() == "Windows"
					else output.decode("utf-8").split("\n")[2]
				)
				cpu_usage = (
					cpu_usage_line.split(",")[-1].strip().replace('"', "")
					if platform.system() == "Windows"
					else cpu_usage_line.split(":")[1].split(",")[0].strip()
				)

				log_data = {"timestamp": time.time(), "cpu_usage": cpu_usage}
				json.dump(log_data, logfile)
				logfile.write("\n")

				# Adjust sleep time
				sleep_time = max(0, interval - (time.time() - operation_start_time))
				time.sleep(sleep_time)
	except IOError as e:
		print(f"Error writing to file {LOGFILE_PATH}: {e}")
		return None

	return LOGFILE_PATH
