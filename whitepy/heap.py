class Heap(dict):
    def __init__(self, stack):
        super(Heap, self).__init__()
        self.stack = stack

    def set(self):
        item = self.stack.pop()
        addr = self.stack.pop()
        self.update({addr: item})

    def get(self):
        addr = self.stack.pop()
        item = self[addr]
        self.stack.push(item)
