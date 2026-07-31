import heapq
from itertools import permutations

INF = float('inf')


def reduce_matrix(mat):
    """
    Reduce the cost matrix and return the reduced matrix
    along with the reduction cost.
    """
    m = [row[:] for row in mat]
    n = len(m)
    cost = 0

    # Row reduction
    for i in range(n):
        row_min = min(m[i])

        if row_min != INF and row_min != 0:
            cost += row_min
            m[i] = [
                x - row_min if x != INF else INF
                for x in m[i]
            ]

    # Column reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))

        if col_min != INF and col_min != 0:
            cost += col_min

            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, cost


def tsp_brute_force(cost, n):
    """
    Brute Force solution for verification.
    """

    cities = list(range(1, n))
    best_cost = INF
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]

        total_cost = sum(
            cost[path[i]][path[i + 1]]
            for i in range(n)
        )

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


# -------- Cost Matrix --------

cost = [
    [INF, 10, 8, 9, 7],
    [10, INF, 10, 5, 6],
    [8, 10, INF, 8, 9],
    [9, 5, 8, INF, 6],
    [7, 6, 9, 6, INF]
]

n = 5
cities = ["A", "B", "C", "D", "E"]

best_path, best_cost = tsp_brute_force(cost, n)

print("5-City TSP - Cost Matrix:\n")

print(f'{"":>4}', end="")
for city in cities:
    print(f"{city:>6}", end="")
print()

for i, row in enumerate(cost):
    print(f"{cities[i]:>4}", end="")

    for value in row:
        if value == INF:
            print(f'{"INF":>6}', end="")
        else:
            print(f"{int(value):>6}", end="")

    print()

print("\nOptimal Tour:")
print(" -> ".join(cities[i] for i in best_path))

print(f"\nMinimum Cost: {int(best_cost)}")

print("\nPath Verification:")

for i in range(n):
    u = best_path[i]
    v = best_path[i + 1]

    print(f"{cities[u]} -> {cities[v]} : Cost = {int(cost[u][v])}")
