import sys


SIDE = 6


def layer_pos(n: int) -> int:
    cnt = 1
    acc = 1
    while acc < n:
        acc += (cnt * SIDE)
        cnt += 1
    return cnt


if __name__ == '__main__':
    num = int(sys.stdin.readline().rstrip())
    print(layer_pos(num))
