
class Convas:
    def draw_pci(self,shape):
        print('---kaishi drawing----')
        shape.draw(self)

class cycle:
    def draw(self,canvas):
        print('cycle')

class squar:
    def draw(self,canvas):
        print('squar')

c=Convas()
c.draw_pci(cycle())


