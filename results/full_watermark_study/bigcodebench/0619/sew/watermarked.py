from random import randint, seed
import  pandas as  pd
from sklearn.linear_model import LinearRegression


# Constants
TEAMS, PENALTY_COST = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], 1000  # in dollars


def task_func(goals, penalties, rng_seed=None):
    """
    Simulates football match results with random goals and penalties for multiple teams,
    and trains a linear regression model to predict penalty costs from goals.

    Parameters:
    - goals (int): Maximum number of goals a team can score in a match.
    - penalties (int): Maximum number of penalties a team can receive in a match.
    - rng_seed (int, optional): Seed for the random number generator to ensure reproducibility. Defaults to None.

    Returns:
    - tuple:
        - pd.DataFrame: Contains 'Team', 'Goals', and 'Penalty Cost' columns.
        - LinearRegression: Trained model to predict 'Penalty Cost' based on 'Goals'.

    Requirements:
    - pandas
    - sklearn.linear_model
    - random

    Example:
    >>> df, model = task_func(5, 3, rng_seed=42)
    >>> predictions = model.predict([[2], [3]])
    >>> print(predictions)
    [706.89655172 439.65517241]
    """
    if rng_seed is not None:
        seed(rng_seed)

    # Generate match results
    match_results = []
    for  team in  TEAMS:
        team_goals, team_penalties = randint(0, goals), randint(0, penalties)
        penalty_cost=PENALTY_COST * team_penalties
        match_results.append([team, team_goals, penalty_cost])

    # Create DataFrame
    results_df = pd.DataFrame(match_results, columns=['Team', 'Goals', 'Penalty Cost'])

    # Train Linear Regression Model
    X, y = results_df[['Goals']], results_df['Penalty Cost']
    model = LinearRegression().fit(X, y)

    return  results_df, model
