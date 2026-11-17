import hashlib
import binascii

def task_func(salt, cursor):
    """
    Updates the passwords in a user table of an SQLite database by hashing them with SHA256, 
    using a provided salt. The function directly modifies the database via the given cursor.

    Parameters:
    - salt (str): The salt value to be appended to each password before hashing.
    - cursor (sqlite3.Cursor): A cursor object through which SQL commands are executed.

    Returns:
    - int: The number of users whose passwords were successfully updated.

    Requirements:
    - hashlib
    - binascii

    Raises:
    TypeError if the salt is not a string
    
    Example:
    >>> conn = sqlite3.connect('sample.db')
    >>> cursor = conn.cursor()
    >>> num_updated = task_func('mysalt', cursor)
    >>> print(num_updated)
    5
    """
    if not isinstance(salt, str):
        raise TypeError
    cursor.execute("SELECT id, password FROM users")
    users = cursor.fetchall()
    count_updated = 0

    for user in users:
        password = user[1].encode('utf-8')
        salted_password = password + salt.encode('utf-8')
        hash_obj = hashlib.sha256(salted_password)
        hashed_password = binascii.hexlify(hash_obj.digest()).decode('utf-8')

        cursor.execute(f"UPDATE users SET password = '{hashed_password}' WHERE id = {user[0]}")
        count_updated += 1

    return count_updated
