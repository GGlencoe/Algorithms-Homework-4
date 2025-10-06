# Subproblem: If I fix one car, what is the longest train I can build starting or ending with that car?

def train():
    n = int(input())
    car = []
    for i in range(n):
        car.append(int(input()))
    
    print(n)
    print(car)

train()