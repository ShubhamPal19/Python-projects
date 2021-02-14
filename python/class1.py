class website:
    pass
a=website # object not created 
b=website()  # object created
print(a)
print(website)
print(b)
  

class stock:
    num=34
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("in init function")
        self.total=self.num+a+b

rishi=stock(3,4)
ravi=stock(34,2)
rishi.facevalue=8100
print(ravi.num,ravi.total)
ravi.total=3422432
print(ravi.total)
print(ravi.num)
ravi.num=2323423
print(ravi.num)
print(rishi.num)
stock.num=232
print(stock.num)
print(rishi.num)
print(rishi.__dict__) #num is not the property of object although he can ACCESS the  num
         

