class Customer():
    def __init__ (self, ccnumber, customername):
        self.ccnumber=ccnumber 
        self.customername=customername

    def getCcNumber(self):
        return self.ccnumber

    def getCustomerName(self):
        return self.customername
    
    def setCcNumber(self, ccnumber):
        self.ccnumber=ccnumber


    def setCustomerName(self, customername):
        self.custoername=customername

    def __str__(self):
        return self.customername + '' + self.ccnumber