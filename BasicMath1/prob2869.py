import sys

# V = A*d - B(d-1)


def num_days(crawl: int, slip: int, top: int) -> int:
    days = float((top - slip) / (crawl - slip))
    if days - int(days) > 0:
        return int(days+1)
    return int(days)


if __name__ == '__main__':
    a, b, v = map(int, sys.stdin.readline().split())
    print(num_days(a, b, v))
