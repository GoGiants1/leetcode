class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    def __repr__(self):
        return f"\nkey: {self.key}, val: {self.val}, prev: {self.prev.key if self.prev else None}, next: {self.next.key if self.next else None} \n"  

    

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.cap = capacity 
        self.cnt = 0
        self.nodes = {}

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        # push back to tail
        self.back_to_tail(self.nodes[key])

        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = value
            self.back_to_tail(self.nodes[key])
        else:
            if self.cnt < self.cap:
                self.cnt += 1
                self.nodes[key] = ListNode(key=key, val=value)
                if self.tail is None:
                    self.tail = self.head = self.nodes[key]
                else:
                    self.back_to_tail(self.nodes[key])
            else:
                victim = self.head
                del self.nodes[victim.key]
                self.back_to_tail(victim)
                self.tail.key = key
                self.tail.val = value
                self.nodes[key] = self.tail
        
        
    def back_to_tail(self, nd: ListNode):
        curr = nd
        if curr.prev and curr.next:
            curr.prev.next, curr.next.prev = curr.next, curr.prev
            self.tail.next, curr.next, curr.prev = curr, None, self.tail
            self.tail = self.tail.next
        elif curr.next is None and curr.prev is None:
            self.tail.next, curr.prev = curr, self.tail
            self.tail = curr
        elif curr.next:
            self.head, curr.next.prev = curr.next, None
            self.tail.next, curr.prev, self.tail = curr, self.tail, curr
        
        self.tail.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)