from lp_method import knapsack_problem

C = 25  # capacity [kg]
w = [3, 1, 6, 8, 1, 13, 8, 10, 1, 1]  # weights of items [kg]
n = len(w)  # number of items to put into knapsack []
p = [2, 1, 4, 5, 3, 2, 8, 9, 1, 1]  # values of items [€]


knapsack_problem(n, p, w, C)
