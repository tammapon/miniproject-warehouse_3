from PlaceClass import place
class harbor(place):
    def __init__(self, name,Count=0):
        super().__init__(name)
        self.count = Count
        self.importlist = []
        self.exportlist = []
