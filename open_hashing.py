class HashTable:    
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __repr__(self):
        return '%s' % ([value for value in self.data if value is not None])

    def hash(self, key):
        index = 0
        if type(key) == int:
            if key > len(self.array):           
                return key%len(self.array)
            else:
                return key
        elif type(key) == str:
            for symbol in key:
                index += ord(symbol)
            return index%len(self.array) 
        else:
            print('You cannot use this type')

    def add(self, key, value):
        key = self.hash(key)
        if self.array[key]:
            array_list = list()
            array_list.append(self.array[key])
        else:
            self.array[key] = value            


if __name__ == "__main__":
    hash = HashTable()