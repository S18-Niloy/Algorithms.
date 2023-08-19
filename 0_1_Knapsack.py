def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity], reconstruct_solution(dp, values, weights, n, capacity)

def reconstruct_solution(dp, values, weights, n, capacity):
    selected_items = []
    while n > 0 and capacity > 0:
        if dp[n][capacity] != dp[n - 1][capacity]:
            selected_items.append(n - 1)
            capacity -= weights[n - 1]
        n -= 1
    return selected_items

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected_items = knapsack_01(values, weights, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
