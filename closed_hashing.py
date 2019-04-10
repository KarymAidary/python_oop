class HashTable:    
    def __init__(self):
        self.size = 20
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __repr__(self):
        return '%s' % ([value for value in self.data if value is not None])

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self,key):
        return self.get(key)

    def hash(self, key):
        if type(key) == int:
            return key%self.size
        elif type(key) == str:
            index = 0
            for symbol in key:
                index += ord(symbol)
            return index%self.size
        else:
            print('You cannot use this type')

    def rehash(self, oldhash):
        return (oldhash+1)%len(self.slots)

    def add(self, key, value):
        hashvalue = self.hash(value)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value  
            else:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and \
                    self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)  
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=value
                else:
                    self.data[nextslot] = value                    
    
    def get(self, key):
        startslot = self.hash(key)
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
             not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position)
                if position == startslot:
                    stop = True
        return data

if __name__ == "__main__":
    hash = HashTable()
    hash[1] = 'Karym'
    
    print(hash[1])