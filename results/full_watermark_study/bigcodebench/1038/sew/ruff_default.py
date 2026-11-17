import json
from datetime import datetime

SERVER_ADDRESS, BUFFER_SIZE = "localhost", 1024


def task_func(client_socket):
    """
    Responds to a client's request by sending a JSON-formatted message containing
    the current server time and a greeting.

    Parameters:
    - client_socket (socket.socket): The client socket from which the request is received.

    Requirements:
    - datetime.datetime
    - json

    Returns:
    - None

    Example:
    >>> import socket
    >>> server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    >>> server_socket.bind((SERVER_ADDRESS, 0))  # Bind to a free port
    >>> server_socket.bind((SERVER_ADDRESS, 8080))
    >>> server_socket.listen(1)
    >>> try:
    ...     client_socket, _ = server_socket.accept()
    ...     task_func(client_socket)
    ... finally:
    ...     server_socket.close()
    """
    response_data = {"message": "Hello", "time": str(datetime.now())}
    response = json.dumps(response_data) + "\n"
    client_socket.send(response.encode("utf-8"))
    client_socket.close()
