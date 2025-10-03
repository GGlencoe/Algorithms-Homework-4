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
            new_height = h + distance
            if new_height <= total:
                dp[i+1][new_height] = min(dp[i+1][new_height], max(dp[i][h], new_height)) # update peak height at next rep

            # go down
            if h - distance >= 0:
                new_height = h - distance
                dp[i+1][new_height] = min(dp[i+1][new_height], dp[i][h])
    
    # Check if we can end at 0
    if dp[reps][0] == INF:
        return "IMPOSSIBLE"
    
    path = []
    current_height = 0
    target_peak = dp[reps][0]

    # work backwards to find path then reverse the array of moves
    for i in range(reps-1, -1, -1):
        distance = climb_distances[i]
        
        #check if came from up
        prev_h_up = current_height - distance
        if prev_h_up >= 0 and prev_h_up <= total + 1:
            # max height if went up would be max(dp[i][prev_h_up], curr_h)
            if dp[i][prev_h_up] != INF:
                new_peak = max(dp[i][prev_h_up], current_height)
                if new_peak == target_peak or (i<reps-1 and new_peak < target_peak):
                    #checks if leads to target peak
                    if dp[i][prev_h_up] <= target_peak:
                        path.append('U')
                        target_peak = dp[i][prev_h_up]
                        current_height = prev_h_up
                        continue
        
        #check if came from down
        prev_h_down = current_height + distance
        if prev_h_down < total + 1:
            if dp[i][prev_h_down] != INF:
                if dp[i][prev_h_down] <= target_peak:
                    path.append('D')
                    target_peak = dp[i][prev_h_down]
                    current_height = prev_h_down
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
