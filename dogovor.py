from abc import ABC

class Dogovor(ABC):

    def __init__(self, vznos, time, maxMoneyBack, minMoneyBack):
        self._vznos = vznos
        #За месяц или квартал или год
        self._typeVznos = 'M'
        #В месяцах
        self._time = time
        self._remainTime = time
        self._maxMoneyBack = maxMoneyBack
        self._minMoneyBack = minMoneyBack

    def getVznos(self):
        return self._vznos

    def getTypeVznos(self):
        return self._typeVznos

    def getMaxMoneyBack(self):
        return self._maxMoneyBack

    def getMinMoneyBack(self):
        return self._minMoneyBack

    def dropMonth(self):
        self._remainTime -= 1

    def getRemainTime(self):
        return self._remainTime

    def getInfo(self):
        return f'Взнос - {self._vznos}, время - {self._time}, максимальный возврат - {self._maxMoneyBack}, минимальный возврат - {self._minMoneyBack}'

class DogovorHouse(Dogovor):
    pass

class DogovorCar(Dogovor):
    pass

class DogovorHealth(Dogovor):
    pass