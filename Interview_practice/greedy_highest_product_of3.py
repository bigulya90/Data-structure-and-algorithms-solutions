"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.

Possible solutions:
1. Go over the list and multiply each integer by each other integer, and then multiply that product by each other other integer.
O(n^3)

So, we need to get off O(n^3). Since, we will look at every int in the least, we will spend at least O(n).

2. Sort the list and get the highest int from the list. O(n lg n)

3. To hit the O(n) runtime, try to use Greedy algo and keep the hig

"""