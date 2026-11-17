import collections

import matplotlib.pyplot as plt
import seaborn as sns


def task_func(dictionary, new_key, new_value):
    """
    Add a new key-value pair to the dictionary and plot the distribution of its values.

    Parameters:
    dictionary (dict): The dictionary to be updated.
    new_key (str): The new key to be added to the dictionary.
    new_value (str): The corresponding value for the new key.

    Returns:
    dict: The updated dictionary.
    matplotlib.axes.Axes: The axes object of the plotted bar graph.

    Requirements:
    - collections
    - numpy
    - seaborn
    - matplotlib

    Example:
    >>> updated_dict, plot_axes = task_func({'key1': 'value1', 'key2': 'value2'}, 'key3', 'value3')
    >>> updated_dict
    {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    """
    # Add new key-value pair to the dictionary
    dictionary[new_key] = new_value

    # Plot the distribution of its values
    values_counts = collections.Counter(dictionary.values())
    ax = sns.barplot(y=list(values_counts.keys()), x=list(values_counts.values()))
    plt.title("Distribution of Dictionary Values")
    plt.xlabel("Values")
    plt.ylabel("Counts")

    return dictionary, ax
