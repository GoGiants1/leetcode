class BrowserHistory:

    def __init__(self, homepage: str):
        self.his = [homepage]
        self.now = 0
        

    def visit(self, url: str) -> None:
        
        while self.now < len(self.his) - 1:
            self.his.pop()
        self.his.append(url)
        self.now += 1
        
    def back(self, steps: int) -> str:
        nxt = self.now - steps
        if nxt < 0:
            nxt = 0
        self.now = nxt
        return self.his[nxt]
        
        
    def forward(self, steps: int) -> str:
        nxt = self.now + steps
        if nxt >= len(self.his):
            nxt = len(self.his) - 1
        self.now = nxt
        return self.his[nxt]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)