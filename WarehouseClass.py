from PlaceClass import place
class warehouse(place):
    def __init__(self,name,temp=0,capacity=0):
        super().__init__(name)
        self.temp=temp
        self.capacity=capacity
        #self.row = []  # This represents a list of rows in a warehouse.
        self.log = []

    def importProduct(self,productName):
        self.log.append(productName)

    def transferProduct(self,productName,warethouseObject):
        warethouseObject.log.append(productName)
        self.log.remove(productName)

    def exportProduct(self,productName):
        self.log.remove(productName)

    '''
    def addRow(self):
        self.row.append([])
        print("addrow raw")
    def addProduct(self, r=0, product=None):
        self.row[r].append(product)
        print("addproduct raw")
    def removeProduct(self,r=0):
        x=self.row[r][0]
        self.row[r]=[]
        return x
    '''