def compareRatio(item1, item2):
    return 0


def fractionalKnapsack(profit, weight, capacity):
    n = len(profit)
    items = [[profit[i], weight[i]] for i in range(n)]


if __name__ == "__main__":
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50

    print(fractionalKnapsack(profit, weight, capacity))
