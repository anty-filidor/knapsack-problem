import random

from typing import List, Tuple


def generate_data() -> Tuple[int, Tuple[int, List[int], List[int], int]]:
    """
    Generates a dataset for knapsack problem.

    Every exemplar of the set is generated with following conditions:
        - sum of weights of items must be smaller than 1.3*total capacity
        - total capacity of n-th exemplar is 50 units higher than n-1th exemplar
        - each item can have weight from range [1, 10]
        - each item can have value from range [1, 10]

    :return: a tuple with:
        - label of the data (i.e. value of total capacity)
        - tuple with data to solve knapsack problem, i.e.
                - number of items that are taken into account
                - a list of values of items [e.g. Euros]
                - a list of weights of items [e.g. kg]
                - a capacity of knapsack [e.g. kg]
    """
    for C in range(50, 5000, 50):
        w = []
        p = []
        n = 0
        while sum(w) < int(1.3 * C):
            w.append(random.randint(1, 11))
            p.append(random.randint(1, 11))
            n += 1
        yield C, (n, p, w, C)
