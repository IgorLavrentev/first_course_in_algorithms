class Queue:
    def __init__(self):
        self.queue = [] # инициализация хранилища данных

    def enqueue(self, item): # вставка в хвост
        self.queue.append(item)

    def dequeue(self): # выдача из головы
        if self.queue is None:
            return None # если очередь пустая
        el = self.queue[0]
        del self.queue[0]
        return el

    def size(self):
        return len(self.queue) # размер очереди

    def print_queue(self):
        for i in range(len(self.queue)):
            print(self.queue[i])

# функция, которая "вращает" очередь по кругу на N элементов
def queue_circle(qu, n): # qu- очередь, n- количество элементов
    for _ in range(n):
        x = qu.dequeue()
        qu.enqueue(x)
