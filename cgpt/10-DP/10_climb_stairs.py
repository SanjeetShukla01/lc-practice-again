
# The Climbing Stairs problem is a classic dynamic programming challenge. You are climbing a staircase.
# It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top? 2


# Understanding the Pattern:
#
# If you have 1 step, there's only 1 way to climb it.
# If you have 2 steps, there are 2 ways to climb them (1+1 or 2).
# For 3 steps, you can either take 1 step from the 2nd step or 2 steps from the 1st step. So, the number of ways is the sum of ways to reach the 1st and 2nd steps.
# This pattern continues: the number of ways to reach the nth step is the sum of the number of ways to reach the *(n-1)*th and *(n-2)*th steps.
#


# Dynamic Programming Approach:
# We use an array dp (or a list in Python) to store the number of ways to reach each step.
# dp[i] represents the number of distinct ways to reach the ith step.
# Base Cases:
# dp[1] = 1
# dp[2] = 2
# Recursive Relation:
# dp[i] = dp[i-1] + dp[i-2] for i > 2
# Iteration:
# We iterate from the 3rd step up to the nth step, calculating dp[i] using the recursive relation.
# Result:
# dp[n] contains the final answer, the number of distinct ways to climb n stairs.




def climb_stairs(n):
    if n <= 2:
        return n
    one_step_before = 2  # Number of ways to reach the (i-1)th step  This represents the number of ways to reach the 2nd step (which is 2).
    two_steps_before = 1  # Number of ways to reach the (i-2)th step   This represents the number of ways to reach the 1st step (which is 1).

    for i in range(3, n + 1):
        current_step = one_step_before + two_steps_before
        two_steps_before = one_step_before
        one_step_before = current_step

    return one_step_before


if __name__ == '__main__':
    num_stairs = 5
    ways = climb_stairs(num_stairs)
    print(f"Number of ways to climb {num_stairs} stairs: {ways}") #output: Number of ways to climb 5 stairs: 8