from typing import Dict, List, Tuple

import pulp as pl


def knapsack_lp(
        n: int, p: List[int], w: List[int], C: int, verbose: bool = False
) -> Tuple[float, Dict[str, bool]]:
    """
    Solves knapsack problem using linear programming.

    We need to pack knapsack which has a certain capacity (e.g. kg). There are
    several items that can be loaded into it. Each item has its weight (e.g.
    kg) and value (e.g. Euros). The task is to choose a subset of items that
    (1) can be stored inside knapsack so that it is not overloaded and (2)
    their total value is maximal.

    :param n: number of items that are taken into account
    :param p: a list of values of items [e.g. Euros]
    :param w: a list of weights of items [e.g. kg]
    :param C: a capacity of knapsack [e.g. kg]
    :param verbose: set to true in order to display detailed logs

    :return: two element tuple with (1) found objective value (2) dictionary
        of found decision variables
    """
    assert n == len(p) == len(w), "Incorrect data!"

    # create decision variables
    x = [pl.LpVariable(name=f"x_{i}", cat="Binary") for i in range(1, n+1)]

    # create model, add constraints and objective function
    model = pl.LpProblem(name="knapsack_problem", sense=pl.LpMaximize)
    model += (pl.lpDot(x, w) <= C, "constraints")
    model += pl.lpDot(p, x)

    if verbose:
        print(f"Decision variables: {x}")
        print(f"Constraints: {model.constraints['constraints']}")
        print(f"Objective function: Min({model.objective})")

    # solve model
    model.solve(pl.PULP_CBC_CMD(msg=verbose))

    # obtain target values
    decision_values = {v.name: bool(v.value()) for v in model.variables()}
    objective_value = model.objective.value()

    if verbose:
        print(f"Solved decision values: {decision_values}")
        print(f"Found objective value: {objective_value}")

    return objective_value, decision_values
