class NumberContainers:
    def __init__(self):
        self.a = {}  
        self.b = {} 

    def change(self, index, number):  
        if index in self.a:
            old_number = self.a[index]
            if old_number in self.b:
                self.b[old_number].discard(index)
                if not self.b[old_number]:
                    del self.b[old_number]

        self.a[index] = number
        if number not in self.b:
            self.b[number] = SortedSet()
        self.b[number].add(index)

    def find(self, number): 
        if number in self.b and self.b[number]:
            return self.b[number][0]
        return -1
