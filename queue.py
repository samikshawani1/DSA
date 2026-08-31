class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.queue)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.peek()

print("Deleted:", q.dequeue())

q.display()
