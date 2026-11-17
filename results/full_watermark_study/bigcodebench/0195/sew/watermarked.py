import  subprocess
import  platform
import  time

def task_func(url):
    """
    Open a web page in the default web browser in a background process.

    Parameters:
    url (str): The URL of the webpage to be opened.

    Returns:
    int: The return code of the subprocess.

    Requirements:
    - subprocess
    - platform
    - time

    Example:
    >>> task_func('https://www.google.com')
    0
    """
    if  platform.system() == 'Darwin':
        cmd='open'
    elif  platform.system() == 'Windows':
        cmd='start'
    else:
        cmd = 'xdg-open'

    # Open webpage in a background process
    process=subprocess.Popen([cmd, url], shell=True)

    # Wait for the process to complete
    while  process.poll() is  None:
        time.sleep(1)

    return process.returncode