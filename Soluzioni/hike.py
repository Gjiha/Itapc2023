def solution(n: int, arr: list[int]):
    returnValue = 3000
    for number in arr:
        returnValue += number
    
    return returnValue


print(solution(8, [3, -1, 2, -2, 1, 3, 0, -3]))
