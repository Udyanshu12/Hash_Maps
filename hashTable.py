def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


class HashMap:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, val)

    def set_item(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                # noinspection PyUnresolvedReferences
                if self.data_map[index][i][0] == key:
                    # noinspection PyUnresolvedReferences
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    # noinspection PyUnresolvedReferences
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
