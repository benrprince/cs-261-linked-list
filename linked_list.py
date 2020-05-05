# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


"""
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
"""


class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:             
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        if index < 0:
            raise Exception("Index out of Bounds")

        count = 0
        curr_node = self.head
        while curr_node is not self.tail:
            if count == index:
                new_link.next = curr_node.next
                curr_node.next = new_link
                return
            count += 1
            curr_node = curr_node.next

        raise Exception("Index out of Bounds")

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            index: The index of the node that will be removed
        """
        if index < 0:
            raise Exception("Index out of Bounds")

        count = 0
        curr_node = self.head
        temp = curr_node.next
        while curr_node is not self.tail:
            if count == index:
                curr_node.next = temp.next
                return
            count += 1
            curr_node = curr_node.next
            temp = curr_node.next

        raise Exception("Index out of Bounds")

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        new_link.next = self.head.next
        self.head.next = new_link

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        if self.head.next == self.tail:
            new_link.next = self.head.next
            self.head.next = new_link
        else:
            curr_node = self.head
            while curr_node != self.tail:
                if curr_node.next == self.tail:
                    new_link.next = curr_node.next
                    curr_node.next = new_link
                    return
                curr_node = curr_node.next

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """
        if self.head.next == self.tail:
            return None
        else:
            return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        if self.head.next == self.tail:
            return None
        else:
            curr_node = self.head
            while curr_node is not self.tail:
                if curr_node.next == self.tail:
                    return curr_node.data
                curr_node = curr_node.next

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """
        if self.head.next == self.tail:
            return
        else:
            temp = self.head.next
            self.head.next = temp.next

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """
        if self.head.next == self.tail:
            return
        else:
            curr_node = self.head
            temp = self.head.next
            while curr_node is not self.tail:
                if temp.next == self.tail:
                    curr_node.next = self.tail
                    return
                curr_node = curr_node.next
                temp = curr_node.next

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """
        if self.head.next == self.tail:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """
        curr_node = self.head.next
        while curr_node is not self.tail:
            if curr_node.data == value:
                return True
            curr_node = curr_node.next

        return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        curr_node = self.head
        temp = self.head.next
        while curr_node is not self.tail:
            if temp.data == value:
                curr_node.next = temp.next
                return
            curr_node = curr_node.next
            temp = curr_node.next


"""
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
"""


class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:             
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        if index < 0:
            raise Exception("Index out of Bounds")

        count = 0
        curr_node = self.sentinel
        # Do while loop
        while True:
            if count == index:
                temp = curr_node.next
                curr_node.next = new_link
                new_link.prev = curr_node
                new_link.next = temp
                return

            count += 1
            curr_node = curr_node.next
            if curr_node == self.sentinel:
                break

        raise Exception("Index out of Bounds")

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            index: The index of the node that will be removed
        """
        if index < 0:
            raise Exception("Index out of Bounds")

        count = 0
        curr_node = self.sentinel

        while curr_node.next != self.sentinel:
            if count == index:
                curr_node.next = curr_node.next.next
                curr_node.next.prev = curr_node
                return

            count += 1
            curr_node = curr_node.next
        raise Exception("Index out of Bounds")

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        temp = self.sentinel.next
        self.sentinel.next = new_link
        new_link.prev = self.sentinel
        new_link.next = temp

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        temp = self.sentinel.prev

        self.sentinel.prev.next = new_link
        self.sentinel.prev = new_link
        new_link.prev = temp
        new_link.next = self.sentinel

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """
        link = self.sentinel.next
        return link.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """
        link = self.sentinel.prev
        return link.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """
        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """
        self.sentinel.prev = self.sentinel.prev.prev
        self.sentinel.prev.next = self.sentinel

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """
        if self.sentinel.next == self.sentinel:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """
        curr_node = self.sentinel
        while True:
            if curr_node.data == value:
                return True

            curr_node = curr_node.next
            if curr_node == self.sentinel:
                return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        curr_node = self.sentinel
        while True:
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
                return

            curr_node = curr_node.next
            if curr_node == self.sentinel:
                return

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """

        # FIXME: Write this function


# test_list = LinkedList([1, 2, 3, 4])
# test_list.add_front(0)
# test_list.add_back(5)
# test_list.add_link_before(6, 6)
# test_list.remove_link(6)
# test_list.remove_front()
# test_list.remove_back()
# print(test_list.get_front())
# print(test_list.get_back())
# test_list.remove(1)
# print(test_list.__str__())

# circ_list = CircularList([1, 2, 3, 4])
# circ_list.add_back(5)
# circ_list.add_front(0)
# print(circ_list.get_front())
# print(circ_list.get_back())
# circ_list.remove_front()
# circ_list.remove_back()
# circ_list.add_link_before(0, 0)
# circ_list.remove_link(0)
# print(circ_list.contains(0))
# circ_list.remove(5)
#
# print(circ_list.__str__())
#
# print(circ_list.get_front())
# print(circ_list.get_back())


