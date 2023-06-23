class FlatIterator:
    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        self.current = 0
        self.cursor = 0
        return self

    def __next__(self):
        if self.cursor < len(self.some_list):
            if isinstance(self.some_list[self.cursor], list):
                nested_el = self.some_list[self.cursor][self.current]
                self.current += 1
                if self.current >= len(self.some_list[self.cursor]):
                    self.cursor += 1
                    self.current = 0
                return nested_el
            result = self.some_list[self.cursor]
            self.cursor += 1
            return result
        raise StopIteration


def flat_generator(some_list):
    for element in FlatIterator(some_list):
        if isinstance(element, list):
            yield from flat_generator(element)
        else:
            yield element


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', [111, [333, [555, 666, [777]], 444], 222], 'c'], 44,
        ['d', ['asr'], 'e', 'f', 'h', False],
        [1, 2, None], 77
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)
