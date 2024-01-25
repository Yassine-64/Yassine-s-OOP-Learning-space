class Car:
    def __init__(self ,speed ,color ,nitrospeed ,model):
        self.speed = speed
        self.color = color
        self.nitrospeed = nitrospeed
        self.model = model 

    def accelerate(self):
        pass

    def turn(self):
        pass

    def brake(self):
        pass

    def boost(self):
        pass

class Employee:
    def __init__(self ,name ,sales ,bonushrs ,basesalary):
        self.name = name
        self.sales = sales
        self.bonushrs = bonushrs
        self.basesalary = basesalary

    def calculateNetSalary(self):
        bonus = self.bonushrs * 50
        total_salary = self.basesalary + bonus + (self.sales * 0.1)
        net_salary = total_salary - (total_salary * 0.2)
        return net_salary
#exemple 
emp1 = Employee('Yassine' ,13 ,7 ,1500)
netsalary = emp1.calculateNetSalary()
print(netsalary)

class Mobile:
    def __init__(self ,companyname ,storage , serialNumber ,name , dualsim , support4k):
        self.companyname = companyname
        self.storage = storage
        self.serialNumber = serialNumber
        self.name = name
        self.dualsim = dualsim
        self.support4k = support4k

    def call(self):
        pass
    def sendMessage(self):
        sent = "eror hhhhhhhhhh xiaomi "  + self.name
        return sent 
    def call(self):
        pass
    def playmedia(self):
        media = "sorry we can't play media f infinix hh"
        return media 
    

class speedcar:
    def __init__(self ,speed ,enginePower ,color ,name):
        self.speed = speed 
        self.enginePower = enginePower
        self.color = color
        self.carnmae = name

    def start(self):
        pass
    def stop(self):
        pass
    def changegear(self):
        pass

