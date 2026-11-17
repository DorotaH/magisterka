import random
import subprocess

# Constants
SCRIPTS, SCRIPTS_DIR = ["script1.sh", "script2.sh", "script3.sh"], "/path/to/scripts"


def task_func():
    """
    Run a random bash script from a list of scripts.

    Parameters:
    - None

    Returns:
    - script (str): The full path of the script that was executed.

    Requirements:
    - subprocess
    - random

    Example:
    >>> task_func()
    """
    script_name = random.choice(SCRIPTS)
    script_path = os.path.join(SCRIPTS_DIR, script_name)  # Generate the full path
    subprocess.call(script_path, shell=True)

    return script_path  # Return the full path
