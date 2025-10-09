# dynamic-programming-greedy-algo-notes

Notes on:

1. knapsack problem, both classical and unbounded
2. Longest Common Subsequence (LCS)

- [Dynamic Programming](#dynamic-programming)
    - [Knapsack Notes](#knapsack-notes)
        - [Recursion](#recursion)
    - [LCS Notes](#lcs-notes)

## Dynamic Programming

### Knapsack Notes

Given bag W, where it can hold at most W amount of weight, and n items, where
each n is associated with weight and profits, puts items into the bag such the
sum of profits associated with them is the maximum possible.

Unbounded variation allows infinite uses of the same item.

#### Recursion

For each item, starting from the last index item, if weight of said item does
not exceed maximum capacity of bag, track the maximum profit (pick) that can
gain from adding said item to the bag with profit from previous item, compare to
the maximum profit without adding said item to the bag, return the maximum of
this two.

### LCS Notes
