class InsCampaign():

    def __init__(self, name, baseDemandHouse, baseDemandCar, baseDemandHealth):
        self.__name = name
        self.__money = 30_000
        self.__listOfDovors = []
        self.__demandHouse = baseDemandHouse
        self.__demandCar = baseDemandCar
        self.__demandHealth = baseDemandHealth
        self.__nalog = 3

    def getListOfDogors(self):
        return self.__listOfDovors

    def appNewDogovor(self, newDogovor):
        self.__listOfDovors.append(newDogovor)

    def getDemandHouse(self):
        return self.__demandHouse

    def getDemandCar(self):
        return self.__demandCar

    def getDemandHealth(self):
        return self.__demandHealth

    def setDemandHouse(self, newDemandHouse):
        self.__demandHouse = newDemandHouse

    def setDemandCar(self, newDemandCar):
        self.__demandCar = newDemandCar

    def setDemandHealth(self, newDemandHealth):
        self.__demandHealth = newDemandHealth

    def setNalog(self, newNalog):
        self.__nalog = newNalog

    def getMoney(self):
        return self.__money

    def addMoney(self, money):
        self.__money += money

    def giveMoney(self, money):
        self.__money -= money

    def payNalog(self):
        self.__money = self.__money*(1 - self.__nalog/100)

    def getNalog(self):
        return self.__money - self.__money*(1 - self.__nalog/100)

    def checkDogovors(self):
        countDeniedDogovors = 0
        massToPop = []
        for el in range(len(self.__listOfDovors) - 1):
            self.__listOfDovors[el].dropMonth()
            if self.__listOfDovors[el].getRemainTime() == 0:
                countDeniedDogovors += 1
                massToPop.append(self.__listOfDovors[el])
        for el in massToPop:
            self.__listOfDovors.remove(el)
        return countDeniedDogovors
