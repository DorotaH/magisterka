import base64
import re
from html import unescape
import textwrap

def task_func(raw_string, line_length):
    """
    Decode a raw string from base64, decouple HTML entities, replace multiple spaces with a single space, strip leading and subsequent spaces, and wrap text to a certain line length.

    Parameters:
    - raw_string (str): The base64 encoded string.
    - line_length (int): The maximum length of a line.

    Returns:
    - wrapped_text (str): The cleaned and formatted string.

    Requirements:
    - base64
    - re
    - html
    - textwrap

    Example:
    >>> task_func('SGVsbG8sICBXb3JsZCEgICAg', 5)
    'Hello\\n, Wor\\nld!'
    """

    # Decode the string from base64
    decoded_string = base64.b64decode(raw_string).decode('utf-8')

    # Unescape HTML entities
    unescaped_string = unescape(decoded_string)

    # Replace multiple spaces with a single space and strip leading and trailing spaces
    cleaned_string = re.sub(' +', ' ', unescaped_string).strip()

    return textwrap.fill(cleaned_string, line_length)
