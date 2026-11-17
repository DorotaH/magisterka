import random

import pandas as pd


def task_func(df):
    """
    Generate a DataFrame that contains savegames for a number of games between different teams.
    Each row of the input DataFrame represents a match, and contains two teams and their respective scores.
    The function adds a 'winner' column to the DataFrame, which is the team with the highest score in each match.
    If the scores are equal, the winner is should be randomly decided.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame with columns 'team1', 'team2', 'score1', 'score2'.

    Requirements:
    - pandas
    - random

    Returns:
    - df (pandas.DataFrame): The DataFrame with the added 'winner' column.

    Example:
    >>> import numpy as np
    >>> import pandas as pd
    >>> df = pd.DataFrame({'team1': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], 20),
    ...                    'team2': np.random.choice(['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], 20),
    ...                    'score1': np.random.randint(0, 10, 20),
    ...                    'score2': np.random.randint(0, 10, 20)})
    >>> df = task_func(df)
    >>> assert 'winner' in df.columns
    >>> assert df['winner'].dtype == object
    >>> assert all(winner in ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'] for winner in df['winner'])
    """

    def determine_winner(row):
        if row["score1"] > row["score2"]:
            return row["team1"]
        elif row["score1"] < row["score2"]:
            return row["team2"]
        else:
            return random.choice([row["team1"], row["team2"]])

    # Using pd.Series to explicitly create a new Series for the 'winner' column
    winner_series = pd.Series(
        [determine_winner(row) for index, row in df.iterrows()], index=df.index
    )
    df["winner"] = winner_series
    return df
