def recurse(routine, routineIndex, currentHeight,  memo):
    if routine[routineIndex] == len(routine):











def main(): 
    memo={}
    n = int(input()) # number of different routines
    routines = []
    ignore = True
    ignoredNum = 0
    for i in range(n*2): 
        if ignore is True:
            ignoredNum = int(input())
            ignore = False
        else:
            routine = input().split()
            routines.append(routine)
            ignore = True
    
    print(routines)

    return 0


if __name__ == "__main__":
    main()