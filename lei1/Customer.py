
class Customer:
    def __init__(self,fav,addr):
        self.fav=fav
        self.addr=addr
    def info(self):
        print(self.fav+'and' +self.addr)

        