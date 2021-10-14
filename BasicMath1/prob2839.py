import sys

def num_bags(target_weight: int) -> int:
    total_weight = 0
    while target_weight > total_weight:
        if total_weight % 3 == 0:

        total_weight += 5
        if target_weight < total_weight:
            total_weight -= 5
            total_weight += 3

if __name__ == '__main__':
