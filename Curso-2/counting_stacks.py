#LAB Modulo 3- Sección 2
#Stack counting
# Python essentials 2

class Stak:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

class CountingStack(Stak):
    def __init__(self):
        super().__init__()
        self.count = 0

    def get_counter(self):
        return self.count

    def pop(self):
        self.count += 1
        return Stak.pop(self)

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())