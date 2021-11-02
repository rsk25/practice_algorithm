import sys


def break_even_amount(fixed: int, marginal: int, price: int) -> int:
    num = 1
    if price == marginal:
        num = -1
    else:
        break_even = fixed/(price - marginal)
        if break_even <= 0:
            num = -1
        else:
            num = break_even + 1
    return int(num)


if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().split())
    print(break_even_amount(a, b, c))
