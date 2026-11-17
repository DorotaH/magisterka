import binascii
import io
import gzip

def task_func(compressed_hex):
    """
    Uncompress a gzip-compressed hexadecimal string and decrypt the result to UTF-8.
    
    Parameters:
    - compressed_hex (str): The gzip-compressed hexadecimal string.
    
    Returns:
    - decoded_string (str): The decoded and decompressed string in UTF-8 format, or an error message.
    
    Requirements:
    - binascii
    - io
    - gzip
    
    Example:
    >>> task_func('1f8b08000000000002ff0b49494e55560304000000ffff8b202d0b000000')
    'Error during decompression: CRC check failed 0xff000000 != 0x41449975'
    """
    try:
        compressed_bytes = binascii.unhexlify(compressed_hex)
        decompressed_bytes = gzip.GzipFile(fileobj=io.BytesIO(compressed_bytes)).read()
        decoded_string = decompressed_bytes.decode('utf-8')
        return decoded_string
    except gzip.BadGzipFile as e:
        return "Error during decompression: " + str(e)
