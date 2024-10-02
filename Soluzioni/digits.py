def createString(d:int, n:int):
    if n == 0:
        return ""
    string = createString(d, n-1)
    return string + str(n) + string


def solution(d: int, n:int):
    string = createString(d,n)
    sum = 0
    for digit in string:
        sum += int(digit)
    return sum


print(solution(1,3))