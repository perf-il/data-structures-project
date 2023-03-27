class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            node = Node(data)
            self.tail.next_node = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        node = self.head
        if self.size > 0:
            self.head = node.next_node
            self.size -= 1
            return node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        deque_list = list()
        node = self.head
        if node is None:
            return f''
        while node is not None:
            deque_list.append(node.data)
            node = node.next_node
        return '\n'.join(deque_list)

