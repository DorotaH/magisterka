import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def task_func(img_path, angle):
    """
    Open an image, rotate it around a certain angle, and then display both the original and the rotated images side by side.
    Additionally, return both images as numpy arrays.

    Parameters:
    img_path (str): The path of the image file.
    angle (float): The angle to rotate the image (in degrees).

    Returns:
    tuple: A tuple containing two numpy arrays, the first representing the original image and
            the second representing the rotated image. Expands the rotated image to make it large enough to hold the entire rotated image.

    Raises:
    FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - PIL
    - matplotlib
    - numpy
    - os

    Example:
    >>> img_path = 'sample.png'
    >>> create_dummy_image(image_path=img_path)
    >>> original_img_array, rotated_img_array = task_func(img_path, 45)
    >>> os.remove(img_path)
    """
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")

    img = Image.open(img_path)
    rotated_img = img.rotate(angle, expand=True)

    # Convert images to numpy arrays
    original_img_array = np.array(img)
    rotated_img_array = np.array(rotated_img)

    # Display original and rotated images side by side
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.subplot(1, 2, 2)
    plt.imshow(rotated_img)
    plt.title("Rotated Image")

    return original_img_array, rotated_img_array
