def spiderman_workout(reps, climb_distances):

    total = sum(climb_distances) # Max height possible
    if total % 2 != 0: return "IMPOSSIBLE" # If total is odd, can't end at 0
    
    #initalizes 2d array filled with 'INF'
    INF = float('INF')
    dp = [[INF] * (total + 1) for _ in range(reps + 1)]
    dp[0][0] = 0 # Starting point at 0 reps and height 0    

    for i in range(reps):
        distance = climb_distances[i]
        for h in range(total + 1):

            if dp[i][h] == INF: # checks if at valid state
                continue
            
            # go up
            newHeight = h + distance
            if newHeight <= total:
                dp[i+1][newHeight] = min(dp[i+1][newHeight], max(dp[i][h], newHeight)) # update peak height at next rep

            # go down
            if h - distance >= 0:
                newHeight = h - distance
                dp[i+1][newHeight] = min(dp[i+1][newHeight], dp[i][h])
    
    # Check if we can end at 0
    if dp[reps][0] == INF:
        return "IMPOSSIBLE"
    
    path = []
    curr_height = 0
    peak = dp[reps][0] # target peak height at the end

    # work backwards to find path then reverse the array of moves
    for i in range(reps-1, -1, -1):
        distance = climb_distances[i]
        
        #check if came from up
        previousHeightIfUp = curr_height - distance
        if previousHeightIfUp >= 0 and previousHeightIfUp <= total + 1:
            # max height if went up would be max(dp[i][previousHeightIfUp], curr_h)
            if dp[i][previousHeightIfUp] != INF:
                new_peak = max(dp[i][previousHeightIfUp], curr_height)
                if new_peak == peak or (i<reps-1 and new_peak < peak):
                    #checks if leads to target peak
                    if dp[i][previousHeightIfUp] <= peak:
                        path.append('U')
                        peak = dp[i][previousHeightIfUp]
                        curr_height = previousHeightIfUp
                        continue
        
        #check if came from down
        previousHeightIfDown = curr_height + distance
        if previousHeightIfDown < total + 1:
            if dp[i][previousHeightIfDown] != INF:
                if dp[i][previousHeightIfDown] <= peak:
                    path.append('D')
                    peak = dp[i][previousHeightIfDown]
                    curr_height = previousHeightIfDown
                    continue
    
    # reverse the path to get correct order
    path.reverse()
    return ''.join(path)
    
def main():
    scenarioNumber = int(input())

    allScenarios = []

    for number in range(scenarioNumber):
        reps = int(input())
        climb_distances = list(map(int, input().split()))
        result = spiderman_workout(reps, climb_distances)
        allScenarios.append(result)

    for scenario in allScenarios:
        print(scenario)
        
if __name__ == "__main__":
    main()
