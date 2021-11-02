import sys


def total_people(floor: int, room_num: int) -> int:
    prev_floor = list(range(1, room_num+1))
    for f in range(floor+1):
        if f == 0:
            continue
        else:
            tmp = prev_floor.copy()
            for r in range(room_num):
                tmp[r] = sum(prev_floor[:r+1])
            prev_floor = tmp

    return prev_floor[room_num-1]


if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip())
    result = list()
    for i in range(t):
        k = int(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        result.append(total_people(k, n))
    print(*result, sep='\n')
