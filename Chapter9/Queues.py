class Queue:
    def __init__(self, item=None):
        self.q = []
        if item:
            self.enqueue(item)
    
    def enqueue(self, item):
        self.q.append(item)
    
    def dequeue(self):
        if self.q:
            val = self.q[0]
            self.q.remove(self.q[0])
            return val
        
    def __repr__(self) -> str:
        return f"Queue: {self.q}"

    def __len__(self) -> int:
        return len(self.q)

    def read(self):
        print(self.q[0])


if __name__=='__main__':
    queue = Queue()
    for _ in range(5, 9):
        queue.enqueue(_)
    
    print(queue)
    print(len(queue))

    for _ in range(5, 9):
        queue.dequeue()

    print(queue)
