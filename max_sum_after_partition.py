def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)  # Initialize DP array

    for i in range(1, n + 1):
        curr_max = 0
        for j in range(1, min(k, i) + 1):
            curr_max = max(curr_max, arr[i - j])  # Find max in the last j elements
            dp[i] = max(dp[i], dp[i - j] + curr_max * j)  # Update DP value

    return dp[n]
