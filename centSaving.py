def round10(x):
    if x % 10 < 5:
        return x - (x % 10)      #round down
    else:
        return x + (10 - x % 10) #round up

def main():
    n, d = map(int, input().split())   #number of items and number of dividers
    items = input().split() #items for array
    belt = [] #array of item prices

    #appends item prices to belt array
    for i in range(n):
        belt.append(int(items[i]))

    #precompute sums for range sum queries
    psum = [0] * (n+1)
    for i in range(1, n+1):
        psum[i] = psum[i-1] + belt[i-1]

    def range_sum(l, r):
        return psum[r+1] - psum[l]

    INF = float("inf")
    #dp[i][g] = min cost to split first i items into g groups
    dp = [[INF]*(d+1) for i in range(n+1)]
    dp[0][0] = 0   #no items, 0 groups → cost = 0

    #fill dp table
    for i in range(1, n+1): #first i items
        dp[i][0] = round10(range_sum(0, i-1))  #no dividers → 1 group
        for k in range(1, d+1): #using k dividers
            for j in range(i): # last group starts at j
                dp[i][k] = min(dp[i][k], dp[j][k-1] + round10(range_sum(j, i-1)))

    print(min(dp[n]))

if __name__ == "__main__":
    main()
