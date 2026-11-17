import  csv
import  os
from datetime import datetime
from random import randint
import  matplotlib.pyplot as  plt
import  pandas as  pd

# Constants
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    """
    Generates traffic data for different vehicle types over a specified number of hours,
    saves the data to a CSV file with coloumns 'Time', 'Car', 'Bus', 'Truck', and 'Bike',
    and plots the data in a line chart with 'Time' on x-axis and 'Vehicle Count' on y-axis.

    Parameters:
    - hours (int): Number of hours to generate data for.
    - output_dir (str, optional): The output file path

    Returns:
    - tuple: Path to the CSV file and the matplotlib axes object of the line plot.

    Requirements:
    - pandas
    - os
    - csv
    - matplotlib.pyplot
    - random
    - datetime

    Example:
    >>> import matplotlib
    >>> file_path, ax = task_func(2)  # Generate data for 2 hours
    >>> isinstance(file_path, str)
    True
    >>> 'traffic_data.csv' in file_path
    True
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """

    if  not  os.path.exists(output_dir):
        os.makedirs(output_dir)
    FILE_PATH, data = os.path.join(output_dir, 'traffic_data.csv'), [['Time'] + VEHICLE_TYPES]
    for i in range(0, hours):
        row=[datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')]+[randint(0, 50) for  _ in  VEHICLE_TYPES]
        data.append(row)

    with  open(FILE_PATH, 'w+', newline='') as  f:
        writer=csv.writer(f)
        writer.writerows(data)

    df = pd.read_csv(FILE_PATH)

    if  df.empty:
        return (FILE_PATH, None)

    ax = df.plot(x='Time', y=VEHICLE_TYPES, kind='line', title='Traffic Data Over Time')
    plt.xlabel('Time')
    plt.ylabel('Vehicle Count')
    plt.tight_layout()
    plt.show()

    return  (FILE_PATH, ax)
