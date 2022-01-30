from data_generator import generate_data
from greedy_method import knapsack_gd
from linprog_method import knapsack_lp
from timer import timer

# exemplary calls
# C = 25  # capacity [kg]
# w = [3, 1, 6, 8, 1, 13, 8, 10, 1, 1]  # weights of items [kg]
# n = len(w)  # number of items to put into knapsack []
# p = [2, 1, 4, 5, 3, 2, 8, 9, 1, 1]  # values of items [€]
# print(knapsack_lp(n, p, w, C, False))
# print(knapsack_gd(n, p, w, C, False))


# measure efficiency of implemented methods
timer(knapsack_gd, knapsack_lp, 100, 10000)
