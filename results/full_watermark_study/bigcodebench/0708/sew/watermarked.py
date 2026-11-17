import  json
import  csv
import  os
import  base64

def task_func(raw_string, filename, output_dir):
    """
    Processes a base64-encoded JSON string, stores the data in a CSV file, and returns the path of the file.

    Parameters:
    - raw_string (str): The base64 encoded JSON string.
    - filename (str): The name of the file to which the data should be saved (without extension).
    - output_dir (str): The path of the directory in which the file should be saved.

    Returns:
    - file_path (str): The path of the file.

    Requirements:
    - json
    - csv
    - os
    - base64

    Example:
    >>> task_func('eyJrZXkiOiAiVmFsdWUifQ==', 'data', './output')
    './output/data.csv'
    """
    # Decode the string and load the data
    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    data = json.loads(decoded_string)

    # Prepare the output directory
    os.makedirs(output_dir, exist_ok=True)

    # Prepare the file path
    file_path = os.path.join(output_dir, f'{filename}.csv')

    # Save the data to the file
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for  key, value in  data.items():
            writer.writerow([key, value])

    return  file_path
