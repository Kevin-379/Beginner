class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist():
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def find(self, item):
        current = self.head
        found = False
        while current is not None:
            if current.data == item:
                found = True
                break
            else:
                current = current.next
        if found:
            print("item is present in list")
        else:
            print("item is not present in the list")

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None:
            if current.data == item:
                found = True
                break
            else:
                previous = current
                current = current.next
        if found:
            previous.next = current.next
        else:
            print("item is not present in the list")

    def printlist(self):
        l="["
        current = self.head
        while current.next is not None:
            l+=str(current.data)+","
            current = current.next
        l+=str(current.data)
        l+="]"
        print(l)

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print(count)

    def append(self, data):
        temp = Node(None)
        temp.next = self.head
        self.head = temp
        current = self.head
        while current.next is not None:
            current.data = current.next.data
            current = current.next
        current.data = data

linkedlist = Linkedlist()
linkedlist.add(4)
linkedlist.add(1)
linkedlist.length()
linkedlist.add(5)
linkedlist.remove(1)
linkedlist.append(1)
linkedlist.printlist()
