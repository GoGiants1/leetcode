class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.history_records = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        if self.history_records[index][-1][0] == self.id:
            self.history_records[index].pop()

        self.history_records[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.history_records[index], snap_id, key=lambda x: x[0])
        return self.history_records[index][snap_index - 1][1]