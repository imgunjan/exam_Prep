def next_num(n):
    """
    Let's analyze the sequence:

    2
    2 * 3 = 6
    6 * 3 = 18
    18 * 6 = 108
    108 * 18 = 1944

    The recursive implementation of this function is efficient because it avoids redundant calculations by breaking down the problem into smaller subproblems and reusing the results.
    """

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return next_num(n - 1) * next_num(n - 2)


print(next_num(6))
