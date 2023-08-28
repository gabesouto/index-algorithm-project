from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.qeue = []

    def __len__(self):
        return len(self.qeue)

    def enqueue(self, value):
        self.qeue.append(value)

    def dequeue(self):
        return self.qeue.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.qeue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.qeue[index]
