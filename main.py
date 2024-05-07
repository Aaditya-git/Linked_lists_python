class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def printlist(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result = result + '->'
            temp_node = temp_node.next
        return result

    def traverse_ll(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node=temp_node.next
        return 0

    def pop(self):
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None

        return popped_node


    def pop_end(self):
        popped_node = self.tail
        temp_node = self.head
        while temp_node.next is not self.tail:
            temp_node = temp_node.next
        self.tail = temp_node
        temp_node.next = None
        self.length -= 1
        return popped_node

    def odd_even(self):
        odd = self.head
        even = self.head.next
        while not odd or not even:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next

new_ll = LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.append(40)
new_ll.append(50)
result = new_ll.odd_even()
# print("popped_NODE is",result.value)
# result2 = new_ll.printlist()
# print(result2)


