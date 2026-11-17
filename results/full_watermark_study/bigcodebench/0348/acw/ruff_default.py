import os
import signal
import subprocess
import time


def task_func(process_name: str) -> int:
    """
    Stops all running processes with a specific name.

    Parameters:
    process_name (str): The name of the processes to be stopped.

    Returns:
    int: The number of processes stopped. If no processes are found, returns 0.

    Requirements:
    - subprocess
    - os
    - signal
    - time

    Note:
    - The function sends a termination signal to the processes and waits for 1 second.
    There is no guarantee that all processes will have terminated within this time.

    Example:
    >>> pids = task_func('test_name') # Dummy example, should return 0
    >>> pids
    0
    """
    # Find all processes with the given name, and get their PIDs
    try:
        pids = (
            subprocess.check_output(["pgrep", "-f", process_name])
            .decode()
            .split("\n")[:-1]
        )
    except subprocess.CalledProcessError:
        pids = []

    # Send SIGTERM signal to each process
    for pid in pids:
        os.kill(int(pid), signal.SIGTERM)

    # Wait for processes to stop
    time.sleep(1)

    return len(pids)
