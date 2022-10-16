
from collections import defaultdict
'''
def findPies(sweet_list,sweetness_required):
    d = {}
    for index,value in enumerate(sweet_list):
        if value in d:
            d[value].append(index)
        else:
            d[value] = [index]
    return d
if __name__ == "__main__":
    sweet_list = list(map(int,input().split()))
    sweetness_required = int(input())

    print(findPies(sweet_list, sweetness_required))
'''

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("done",partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


if __name__ == "__main__":
    sweet_list = list(map(int,input().split()))
    sweetness = int(input())
    subset_sum(sweet_list,sweetness)