from collections import Counter
from itertools import product


def all_combinations():
    return [comb for comb in product(range(1, 7), repeat=2)]


def all_sums(combs):
    return [comb[0] + comb[1] for comb in combs]


def most_common_sums(sums):
    return Counter(sums).most_common(3)
