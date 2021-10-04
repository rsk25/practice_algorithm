import sys

# 1. 어느 줄에 위치해 있는지 파악
# 2. 그 줄이 홀수/짝수? -> 홀: 1/n으로 시작, 짝: m/1으로 시작
# 3. 그 줄의 시작점에서 얼마나 떨어졌는지?


def line_pos(n: int) -> int:
    cnt = 0
    acc = 0
    while acc < n:
        cnt += 1
        acc += cnt
    return cnt


def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


def pos_inline(n: int) -> str:
    lp = line_pos(n)
    acc = 0
    for i in range(lp+1):
        acc += i
    if is_even(lp):
        nu = lp - (n-acc)
        de = 1 + (n-acc)
    else:
        nu = 1 + (n-acc)
        de = lp - (n-acc)
    return str(nu)+'/'+str(de)


if __name__ == '__main__':
    num = int(sys.stdin.readline().rstrip())
    print(pos_inline(num))
