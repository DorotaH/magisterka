import  csv
import  sys

def  task_func(filename):
    """
    Read a CSV file, inverse the order of the lines and write the inverted lines back into the file. Then reset the cursor to the beginning of the file.

    Parameters:
    - filename (str): The name of the CSV file.

    Returns:
    - filename (str): The name of the CSV file.

    Requirements:
    - csv
    - sys

    Example:
    >>> task_func('file.csv')
    'file.csv'
    """
    try:
        with open(filename, 'r+') as file:
            reader=csv.reader(file)
            rows=list(reader)
            file.seek(0)
            file.truncate()

            writer=csv.writer(file)
            writer.writerows(reversed(rows))

            file.seek(0)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

    return  filename
