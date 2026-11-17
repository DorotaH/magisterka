import logging

import requests


def task_func(repo_url: str) -> dict:
    """
    Fetches and returns information about a GitHub repository using its API URL. The function makes an HTTP GET
    request to the provided repository URL. It incorporates error handling for various scenarios including API
    rate limits, other HTTP errors, and general request issues. The function also checks for a large number of
    open issues in the repository and prints a warning if they exceed a certain threshold.

    Parameters:
    - repo_url (str): The URL of the GitHub repository API.

    Returns:
    - dict: A dictionary containing information about the GitHub repository.

    Raises:
    - requests.exceptions.HTTPError: If an HTTP error occurs, particularly when the GitHub API rate limit is
                    exceeded.
    - requests.exceptions.RequestException: For other general issues encountered during the API request, such
                    as network problems, invalid responses, or timeouts.

    Requirements:
    - requests
    - logging

    Example:
    >>> task_func('https://api.github.com/repos/psf/requests')
    { ... }  # dictionary containing repo information
    >>> task_func('https://api.github.com/repos/some/repo')
    { ... }  # dictionary containing repo information with a possible runtime warning about open issues
    """
    try:
        response = requests.get(repo_url, timeout=2)
        response.raise_for_status()  # Raises HTTPError for bad requests
        repo_info = response.json()
        if (
            response.status_code == 403
            and repo_info.get("message") == "API rate limit exceeded"
        ):
            raise requests.exceptions.HTTPError("API rate limit exceeded")

        if 10000 < repo_info.get("open_issues_count", 0):
            logging.warning("The repository has more than 10000 open issues.")

        return repo_info

    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(
            f"Error fetching repo info: {e}"
        ) from e
