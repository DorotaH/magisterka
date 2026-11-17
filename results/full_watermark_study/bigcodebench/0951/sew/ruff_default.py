import random
from random import randint

import numpy as np
import pandas as pd

# Constants
CATEGORIES = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys & Games"]


def task_func(mystrings, n_products, seed=0):
    """
    Create a product catalog DataFrame where each row represents a product with the following columns:
    - 'Product Name': The name of the product with spaces replaced by underscores.
    - 'Category': The category to which the product belongs.
    - 'Price': The price of the product, generated randomly based on a normal distribution with a mean of 50 and a standard deviation of 10.

    Parameters:
    mystrings (list of str): List of product names.
    n_products (int): Number of products to generate in the catalog.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the product catalog information.

    Requirements:
    - pandas
    - numpy
    - random.randint
    - random.seed

    Constants:
    - CATEGORIES: A list of categories used to randomly assign a category to each product.

    Examples:
    >>> task_func(['Mobile Phone', 'T Shirt', 'Coffee Maker', 'Python Book', 'Toy Car'], 2)
       Product Name        Category  Price
    0   Python_Book           Books  67.64
    1  Mobile_Phone  Home & Kitchen  54.00
    >>> task_func(['Laptop', 'Sweater'], 1)
      Product Name Category  Price
    0      Sweater    Books  67.64
    """
    catalogue_data = []
    random.seed(seed)
    np.random.seed(seed)
    for _ in range(n_products):
        product_name, category = (
            mystrings[randint(0, len(mystrings) - 1)].replace(" ", "_"),
            CATEGORIES[randint(0, len(CATEGORIES) - 1)],
        )
        price = round(np.random.normal(50, 10), 2)
        catalogue_data.append([product_name, category, price])

    catalogue_df = pd.DataFrame(
        catalogue_data, columns=["Product Name", "Category", "Price"]
    )

    return catalogue_df
