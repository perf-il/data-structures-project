class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        head = self.head
        if head is None:
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, head)
        self.size += 1

    def insert_at_end(self, data) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        tail = self.tail
        if tail is None:
            self.tail = self.head = Node(data)
        else:
            cur = self.head
            while cur.next_node is not None:
                cur = cur.next_node
            cur.next_node = tail = Node(data)
            self.tail.next_node = tail
            self.tail = tail
        self.size += 1

    def to_list(self):
        """возвращает список с данными, содержащимися в односвязном списке """
        node = self.head
        ll_list = []
        if node is None:
            ll_list.append(None)
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, id_data):
        """возвращает первый найденный в `LinkedList` словарь с ключом 'id',
        значение которого равно переданному в метод значению."""
        lst = self.to_list()
        for node in lst:
            try:
                if node['id'] == id_data:
                    return node
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()
