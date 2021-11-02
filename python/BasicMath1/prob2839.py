import sys

def num_bags(target_weight: int) -> int:
    weight_list = list()
    weight = 5
    while target_weight > 0:
        target_weight -= weight
        if not target_weight > 0:

        weight_list.append(weight)


if __name__ == '__main__':

