# Subproblem: LIS LDS 

def train():
    n = int(input())
    car = []
    for i in range(n):
        car.append(int(input()))

    right = [1] * n
    left = [1] * n
    total = 0

    for i in reversed(range(n)):
        for j in range(i + 1, n):
            if car[j] > car[i]:
                left[i] = max(left[i], left[j] + 1)
            if car[j] < car[i]:
                right[i] = max(right[i], right[j] + 1)
        total = max(total, right[i] + left[i] - 1)
 
    return total
    
print(train())

