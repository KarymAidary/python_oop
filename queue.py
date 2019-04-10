class Queue:
    def __init__(self):
        self.item_list = []

    def __repr__(self):
        return '%s' % [item for item in self.item_list]

    def enqueue(self, item, priority=None):
        if priority is None:
            self.item_list.insert(0, item)
        else:
            self.item_list.insert(priority, item)

    def dequeue(self):
        return self.item_list.pop()

    def size(self):
        return len(self.item_list)

if __name__ == "__main__":
    items = Queue()
    items.enqueue(1)
    items.enqueue(4, 2)
    items.enqueue(3)
    print(items)    
    