from linprog_method import knapsack_lp
from greedy_method import knapsack_gd

C = 25  # capacity [kg]
w = [3, 1, 6, 8, 1, 13, 8, 10, 1, 1]  # weights of items [kg]
n = len(w)  # number of items to put into knapsack []
p = [2, 1, 4, 5, 3, 2, 8, 9, 1, 1]  # values of items [€]

C = 27
w = [15, 10, 2, 4]
n = 4
p = [3, 25, 2, 10]


print(knapsack_lp(n, p, w, C, True))
print(knapsack_gd(n, p, w, C, True))
