import argparse


def auxFib(
    number: int,
    memo: list[int],
) -> int:
    if number <= 1:
        return number
    if memo[number] != -69:
        return memo[number]
    memo[number] = auxFib(number - 1, memo) + auxFib(number - 2, memo)
    return memo[number]


def fib(number: int) -> int:
    memo = [-69] * (number + 1)
    return auxFib(number, memo)


def fibIterative(
    number: int,
) -> int:
    if number <= 1:
        return number
    dp = [0] * (number + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, number + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[number]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A simple program that processes arguments."
    )
    parser.add_argument(
        "number",
        help="n^th number of fibonacci number",
    )
    args = parser.parse_args()
    print(fib(int(args.number)))
    print(fibIterative(int(args.number)))
