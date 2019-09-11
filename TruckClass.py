class truck:
    def __init__(self,name="",minload=0,maxload=0):
        self.name=name
        self.minload=minload
        self.maxload=maxload
        self.distance=0
        self.lastplacename=''

    def printDistance(self):
        if self.distance-int(self.distance)==0:
            return str(int(self.distance))
        else:
            return '%.2f'%(self.distance)