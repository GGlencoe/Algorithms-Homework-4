def spidermanWorkout(scenario, currentIndex, currentHeight, memo):
    if currentIndex == len(scenario):
        return "" if currentHeight == 0 else "IMPOSSIBLE"
    
    if currentHeight < 0:
        return "IMPOSSIBLE"
    
    if (currentIndex, currentHeight) in memo:
        return memo[(currentIndex, currentHeight)]

    step = scenario[currentIndex]
    down = spidermanWorkout(scenario, currentIndex+1, currentHeight-step, memo)
    if down != "IMPOSSIBLE":
        memo[(currentIndex, currentHeight)] = "D" + down
        return memo[(currentIndex, currentHeight)]

    up = spidermanWorkout(scenario, currentIndex+1, currentHeight+step, memo)

    if up != "IMPOSSIBLE":
        memo[(currentIndex, currentHeight)] = "U" + up
        return memo[(currentIndex, currentHeight)]

    memo[(currentIndex, currentHeight)] = "IMPOSSIBLE"
    return "IMPOSSIBLE"


def main():
    ScenarioNumber = int(input()) 

    allScenarios = []

    for number in range(ScenarioNumber):      
        ScenarioSize = int(input())  
        ScenarioDistances = [0] * ScenarioSize  

        values = [int(x) for x in input().split()]

        for i in range(ScenarioSize):
            ScenarioDistances[i] = values[i]
        allScenarios.append(ScenarioDistances)

    for scenario in allScenarios:
        memo = {}
        print(spidermanWorkout(scenario, 0, 0, memo))
    return 0

if __name__ == "__main__":
    main()