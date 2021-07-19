#!/usr/bin/env/ python3 

# Error... weird
def solve(n):

	dp = [[0 for i in range(8)] for j in range(8)]
	dp[0][7] = 1

	for i in range(0, n+1):
		dp[i][0] += dp[i - 1][7]

		dp[i][1] += dp[i - 1][6]

		dp[i][2] += dp[i - 1][5]

		dp[i][3] += dp[i - 1][7]
		dp[i][3] += dp[i - 1][4]

		dp[i][4] += dp[i - 1][3]

		dp[i][5] += dp[i - 1][2]

		dp[i][6] += dp[i - 1][7]
		dp[i][6] += dp[i - 1][1]

		dp[i][7] += dp[i - 1][3]
		dp[i][7] += dp[i - 1][6]
		dp[i][7] += dp[i - 1][0]
	return dp[n][7]

def main():
	solve(10)

if __name__ == '__main__':
	main()