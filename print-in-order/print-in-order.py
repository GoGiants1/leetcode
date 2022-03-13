from threading import Lock

class Foo:
    def __init__(self):
        self.first_ = Lock()
        self.second_ = Lock()
        self.first_.acquire()
        self.second_.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_.release()
        

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        self.first_.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.second_.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()