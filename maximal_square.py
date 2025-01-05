def maximal_square(matrix):
    if not matrix or not matrix[0]:
        return 0

    # Initialize dimensions
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]  # DP table
    max_side = 0  # Tracks the largest square side length

    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is '1'
            if matrix[i][j] == '1':
                if i == 0 or j == 0:  # First row or first column
                    dp[i][j] = 1  # Base case
                else:
                    # Calculate square size using neighbors
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                # Update max square size
                max_side = max(max_side, dp[i][j])

    # Return the area of the square
    return max_side * max_side