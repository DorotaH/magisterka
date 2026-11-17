import json
import smtplib

# Constants
SMTP_SERVER, SMTP_PORT = "smtp.gmail.com", 587
EMAIL_ADDRESS, EMAIL_PASSWORD = "your.email@gmail.com", "your.password"


def task_func(
    input_data=None,
    smtp_server=SMTP_SERVER,
    smtp_port=SMTP_PORT,
    email_address=EMAIL_ADDRESS,
    email_password=EMAIL_PASSWORD,
    smtp=None,
):
    """
    Extract recepient email address and names from JSON-formatted string and send the names in an email. The sent message should be in the format 'Subject: Extracted Names\n\nName1\nName2\n...'.

    Parameters:
    input_data (str): JSON-formatted string containing the recipient email address and the list of names.
    smtp_server (str): The SMTP server to use for sending the email.
    smtp_port (int): The port to use for the SMTP server.
    email_address (str): The email address from which to send the email.
    email_password (str): The password for the email address.

    Returns:
    list: A list of extracted names.

    Requirements:
    - re
    - smtplib

    Example:
    >>> from unittest.mock import MagicMock
    >>> mock_smtp_instance = MagicMock()
    >>> mock_smtp = MagicMock(return_value=mock_smtp_instance)
    >>> task_func('{"recipient": "recipient@example.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}', smtp=mock_smtp)
    ['Josie Smith', 'Mugsy Dog Smith']
    """

    if input_data is None:
        return list()

    # Parse input JSON data
    try:
        data = json.loads(input_data)
        recipient_email, names = data.get("recipient"), data.get("names", [])
    except (json.JSONDecodeError, ValueError):
        return list()

    if not recipient_email or not names:
        return list()

    message = "Subject: Extracted Names\n\n" + "\n".join(names)

    server = (
        smtp(smtp_server, smtp_port) if smtp else smtplib.SMTP(smtp_server, smtp_port)
    )
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recipient_email, message)
    server.quit()
    return names
