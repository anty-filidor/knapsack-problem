from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class _KnapsackItem:
    """Auxiliary class to group data relevant for each of items."""

    weight: int
    value: int
    idx: int

    def __post_init__(self) -> None:
        """Computes fields that results from input data."""
        self._cost = self.value / self.weight

    def __lt__(self, other: '_KnapsackItem') -> bool:
        """Implements < operator."""
        return self._cost < other._cost

    def __repr__(self) -> str:
        """Returns representation of the objects."""
        return f"x_{self.idx}"


def knapsack_gd(
        n: int, p: List[int], w: List[int], C: int, verbose: bool = False
) -> Tuple[float, Dict[str, bool]]:
    """
    Solves knapsack problem in greedy way.

    We need to item knapsack which has a certain capacity (e.g. kg). There are
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

    # convert input data to auxiliary objects and sort them
    items = sorted(
        [_KnapsackItem(w[i], p[i], i + 1) for i in range(n)],
        reverse=True
    )

    # init variables to return
    objective_value = 0
    decision_values = {str(p): False for p in items}

    # perform main loop until
    used_capacity = 0
    for item in items:
        if item.weight <= C - used_capacity:
            used_capacity += item.weight
            objective_value += item.value
            decision_values[str(item)] = True

    if verbose:
        print(f"Solved decision values: {decision_values}")
        print(f"Found objective value: {objective_value}")

    return objective_value, decision_values
