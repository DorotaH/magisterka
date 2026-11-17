import base64
import hashlib


def task_func(filename, data, password):
    """
    Encrypt a string with a password, then write the encrypted string to a file.
    If the file or directory does not exist, create it.

    Parameters:
    filename (str): The name of the file to write to.
    data (str): The string to encrypt and write to the file.
    password (str): The password to use for encryption.

    Returns:
    str: The encrypted string.

    Requirements:
    - hashlib
    - base64

    Example:
    >>> task_func('test.txt', 'Hello, World!', 'password')
    'Fu0k9LUEJCY+ookLrA=='
    """
    # Ensure the file exists
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    if not os.path.exists(filename):
        open(filename, "a").close()

    # Encrypt the data using simple XOR operation with password hash as key
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = []
    for i, byte in enumerate(data.encode()):
        encrypted_bytes.append(byte ^ key[i % len(key)])
    encrypted = base64.b64encode(bytes(encrypted_bytes)).decode()

    # Write to the file
    with open(filename, "w") as f:
        f.write(encrypted)

    return encrypted
