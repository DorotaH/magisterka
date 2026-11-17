import folium
import numpy as np
import pandas as pd


def task_func(
    dic={"Lon": (-180, 180), "Lat": (-90, 90)},
    cities=["New York", "London", "Beijing", "Tokyo", "Sydney"],
):
    """
    Create a map with markers for a list of cities, where the coordinates are randomly generated within given ranges.

    Parameters:
    dic (dict): Dictionary with 'Lon' and 'Lat' keys, each a tuple (min, max) for coordinate range.
                            Default: {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities (list): List of city names. Default: ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']

    Returns:
    tuple: A tuple containing (folium.Map, pandas.DataFrame).
            The DataFrame contains 'City', 'Longitude', and 'Latitude' columns.

    Raises:
    ValueError: If 'Lon' or 'Lat' keys are missing in the dictionary, or if their values are not tuples.

    Requirements:
    - pandas
    - numpy
    - folium

    Example:
    >>> dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    >>> map_obj, city_data = task_func(dic)
    """
    if (
        "Lon" not in dic
        or "Lat" not in dic
        or not isinstance(dic["Lon"], tuple)
        or not isinstance(dic["Lat"], tuple)
    ):
        raise ValueError(
            "Dictionary must contain 'Lon' and 'Lat' keys with tuple values."
        )

    lon_min, lon_max = dic["Lon"]
    lat_min, lat_max = dic["Lat"]

    data = {"City": [], "Longitude": [], "Latitude": []}
    for city in cities:
        data["City"].append(city)
        data["Longitude"].append(np.random.uniform(lon_min, lon_max))
        data["Latitude"].append(np.random.uniform(lat_min, lat_max))

    df = pd.DataFrame(data)

    m = folium.Map(location=[0, 0], zoom_start=2)
    for _, row in df.iterrows():
        folium.Marker([row["Latitude"], row["Longitude"]], popup=row["City"]).add_to(m)

    return m, df
