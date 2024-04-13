"""
while loop:
The while loop is used when you don't know the number of iterations beforehand.
It continues to execute as long as a certain condition is true.
The condition is evaluated before each iteration of the loop.
"""

Count = 0
while Count < 5:
    print(Count)
    # Count = Count + 1                Both are same things of line no 11 and 12
    Count += 1

"""
Output:
0
1
2
3
4
"""
