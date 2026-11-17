import codecs
import hashlib
import random
import string


def task_func(password_length=10, salt="salty"):
    """
    Generate a random password of a specified length, including Latin characters, numbers, and symbols.
    Then, hash the password using the SHA256 algorithm after mixing it with a specified salt.

    Parameters:
    - password_length (int, optional): Length of the generated password. Defaults to 10.
    - salt (str, optional): Salt to be added to the password before hashing. Defaults to "salty".

    Returns:
    str: The hashed password.

    Requirements:
    - codecs
    - random
    - string
    - hashlib

    Example:
    >>> random.seed(0)
    >>> hashed_password = task_func(12, "my_salt")
    >>> print(hashed_password)
    a706478dc5969e90dcfc2fbaffff0b9f8e7f2b006002edac13cb17f5bf9ba941
    """
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_chars) for i in range(password_length))
    password = codecs.encode(password, "latin-1").decode("utf-8")
    salted_password = (password + salt).encode("utf-8")
    hashed_password = hashlib.sha256(salted_password).hexdigest()

    return hashed_password
