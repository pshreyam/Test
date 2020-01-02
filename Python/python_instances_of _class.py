class Cars:
    def __init__(self,name,price,year,month,date):
        self.name=name.title()
        self.price=price
        self.year=year
        self.month=month
        self.date=date
        self.man_date=year+"/"+month+"/"+date
    def getdetails(self):
        print("The name of the car is ",self.name)
        print("The price of the car is ",self.price)
        print("The manufacture date of the car is ",self.man_date)
    def updatedetails(self,name,price,year,month,date):
        self.name=name.title()
        self.price=price
        self.year=year
        self.month=month
        self.date=date
        self.man_date=year+"/"+month+"/"+date
class Bmw(Cars):
    def __init__(self,name,price,year,month,date):
        super().__init__(name,price,year,month,date)
bmw1=Bmw("hello","$200","2000","12","10")
bmw1.getdetails()
