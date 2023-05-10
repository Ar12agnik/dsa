class node:
    def __init__(self,data) -> None:
        self.lson=None
        self.rson=None
        self.data=data
class heap:
    def __init__(self) -> None:
        self.root=None
        self.last=None
    def insert(self,data):
        newnode=self.node(data)
        if self.root is None:
            self.root=newnode
            self.last=newnode
        else:
            if self.last.lson is None:
                self.last.lson=newnode
                self.last=newnode
            else:
                self.last.rson=newnode
                self.last=newnode
    def heapify(self):
        pass
    # !ask maam rest