class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 1. Функція для реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо наступний вузол
            current.next = prev       # Міняємо напрямок посилання
            prev = current            # Зсув попереднього вузла
            current = next_node       # Переходимо до наступного вузла
        self.head = prev               # Нова голова списку
        print("\nСписок було реверсовано")

    # 2. Функція для сортування однозв'язного списку методом злиття
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self  # Якщо список пустий або складається з одного елемента

        # Функція для знаходження середини списку
        def get_middle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None  # Розділення списку на дві половини
            return head, middle

        # Функція для злиття двох відсортованих списків
        def sorted_merge(left, right):
            if left is None:
                return right
            if right is None:
                return left
            if left.data <= right.data:
                result = left
                result.next = sorted_merge(left.next, right)
            else:
                result = right
                result.next = sorted_merge(left, right.next)
            return result

        # Рекурсивна реалізація сортування злиттям
        def merge_sort_recursive(node):
            if node is None or node.next is None:
                return node
            left, right = get_middle(node)
            left = merge_sort_recursive(left)
            right = merge_sort_recursive(right)
            return sorted_merge(left, right)

        self.head = merge_sort_recursive(self.head)
        print("\nСписок було відсортовано методом злиття")

    # 3. Функція для об'єднання двох відсортованих однозв'язних списків в один відсортований список
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()  # Фіктивний вузол для спрощення злиття
        tail = dummy
        l1, l2 = list1.head, list2.head

        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Додаємо залишок одного зі списків
        tail.next = l1 if l1 else l2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

# Тестування
llist = LinkedList()

# Додавання елементів
llist.insert_at_end(10)
llist.insert_at_end(3)
llist.insert_at_end(7)
llist.insert_at_end(2)
llist.insert_at_end(5)

print("Початковий список:")
llist.print_list()

# Реверсування списку
llist.reverse()
print("Список після реверсування:")
llist.print_list()

# Сортування списку методом злиття
llist.merge_sort()
print("Список після сортування:")
llist.print_list()

# Об'єднання двох відсортованих списків
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(4)
list1.insert_at_end(9)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(5)
list2.insert_at_end(6)

print("\nПерший відсортований список:")
list1.print_list()
print("Другий відсортований список:")
list2.print_list()

merged_list = LinkedList.merge_sorted_lists(list1, list2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()
