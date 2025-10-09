def auxKnapsack(max_bag_weight, profit, weight, n):
    if n == 0 or weight == 0:
        return 0
    pick = 0
    if weight[n - 1] <= max_bag_weight:
        pick = profit[n - 1] + auxKnapsack(
            max_bag_weight - weight[n - 1], profit, weight, n - 1
        )
    not_pick = auxKnapsack(max_bag_weight, profit, weight, n - 1)
    return max(pick, not_pick)


def knapsack(max_bag_weight, profit, weight):
    n = len(profit)
    return auxKnapsack(max_bag_weight, profit, weight, n)


def knapsackBottomUp(max_bag_weight, profit, weight):
    w = len(weight)
    dp = [[0 for _ in range(max_bag_weight + 1)] for _ in range(w + 1)]

    for i in range(w + 1):
        for j in range(max_bag_weight + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0
                if weight[i - 1] <= j:
                    pick = profit[i - 1] + dp[i - 1][j - profit[i - 1]]
                notPick = dp[i - 1][j]
                dp[i][j] = max(pick, notPick)

    return dp[w][max_bag_weight]


if __name__ == "__main__":
    profit = [1, 2, 3]
    weight = [4, 5, 1]
    max_bag_weight = 4

    print(knapsack(max_bag_weight, profit, weight))
    print(knapsackBottomUp(max_bag_weight, profit, weight))
