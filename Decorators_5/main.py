from decor import loger
import os

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

PATH = os.path.dirname(os.path.realpath(__file__))


@loger(PATH)
def recurse(arr):
    for item in arr:
        if isinstance(item, list):
            yield from recurse(item)
        else:
            yield item


if __name__ == "__main__":
    for i in recurse(nested_list):
        print(i)