import random
import re

import pandas as pd


def task_func(person_names, email_domains, num_records=5):
    """
    Generate a DataFrame with a specified number of records containing personal names and emails.
    The emails are cleaned by replacing all occurrences of "@" with "[at]".

    Parameters:
    - person_names (list of str): A list of person names to use in the records.
    - email_domains (list of str): A list of email domains to use in the records.
    - num_records (int, optional): The number of records to generate. Default is 5.

    Returns:
    - DataFrame: A pandas DataFrame with columns 'Name' and 'Email' containing the person names and cleaned emails.

    Requirements:
    - pandas for DataFrame manipulation
    - random for random selection
    - re for regular expression operations

    Raises:
    - ValueError: If the number of names provided is less than the number of records requested or if no email domains are provided.

    Example:
    >>> random.seed(0)  # Initialize random seed
    >>> task_func(['John Doe', 'Jane Smith'], ['gmail.com', 'yahoo.com'], 2)
             Name              Email
    0  Jane Smith  jane[at]gmail.com
    1    John Doe  john[at]yahoo.com
    >>> task_func(['Alice'], ['outlook.com'], 1)
        Name                 Email
    0  Alice  alice[at]outlook.com
    """
    if len(person_names) < num_records or len(email_domains) == 0:
        raise ValueError("Insufficient number of names or domains provided.")

    data = []

    # Randomly select 'num_records' names from the provided list
    selected_names = random.sample(person_names, num_records)

    for name in selected_names:
        email = re.sub(
            "@", "[at]", f"{name.split()[0].lower()}@{random.choice(email_domains)}"
        )
        data.append([name, email])

    df = pd.DataFrame(data, columns=["Name", "Email"])
    return df
