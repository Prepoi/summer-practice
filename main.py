from insCampaign import *
from dogovor import *
from random import *
from tkinter import *
import matplotlib.pyplot as plt

baseDemandHouse = randint(3, 10)
baseDemandCar = randint(5, 20)
baseDemandHealth = randint(5, 20)
company = InsCampaign('ООО Страховка', baseDemandHouse, baseDemandCar, baseDemandHealth)

rateHouse = 1.5
rateCar = 2.5
rateHealth = 7.5

def setDemandCompanyZero():
    company.setDemandHouse(0)
    company.setDemandCar(0)
    company.setDemandHealth(0)

def setNewRandintDemand():
    company.setDemandHouse(randint(2, 15))
    company.setDemandCar(randint(3, 20))
    company.setDemandHealth(randint(3, 25))

def getPaymentToPopulation():
    totalPayment = 0
    for dogovor in company.getListOfDogors():
        #Шанс на несчастынй случай в процентах
        chanceToPay = randint(1, 100)
        if chanceToPay <= 2:
            sizePayment = round(uniform(dogovor.getMinMoneyBack(), dogovor.getMaxMoneyBack()), 1)
            totalPayment += sizePayment
        else:
            pass

    return totalPayment

massNowMonthDogovors = []
totalVznos = 0
currentMonth = 0
def appClients():
    global totalVznos
    for strahovkaHouse in range(company.getDemandHouse()):
        chanceClient = randint(1, 100)
        if chanceClient > 33:
            strahovSum = randint(1_000, 8_000)
            vznos = round(strahovSum*rateHouse/100, 1)
            time = randint(1, 3)
            maxMoneyBack = strahovSum
            minMoneyBack = round(strahovSum*0.02, 1)
            company.appNewDogovor(DogovorHouse(vznos, time, maxMoneyBack, minMoneyBack))
            company.addMoney(vznos)
            totalVznos += vznos
            massNowMonthDogovors.append(DogovorHouse(vznos, time, maxMoneyBack, minMoneyBack))

    for strahovkaCar in range(company.getDemandCar()):
        chanceClient = randint(1, 100)
        if chanceClient > 33:
            strahovSum = randint(2_000, 10_000)
            vznos = round(strahovSum*rateCar/100, 1)
            time = randint(1, 3)
            maxMoneyBack = strahovSum
            minMoneyBack = round(strahovSum*0.02, 1)
            company.appNewDogovor(DogovorCar(vznos, time, maxMoneyBack, minMoneyBack))
            company.addMoney(vznos)
            totalVznos += vznos
            massNowMonthDogovors.append(DogovorCar(vznos, time, maxMoneyBack, minMoneyBack))

    for strahovkaHealth in range(company.getDemandHealth()):
        chanceClient = randint(1, 100)
        if chanceClient > 33:
            strahovSum = randint(300, 6_000)
            vznos = round(strahovSum*rateHealth/100, 1)
            time = randint(1, 3)
            maxMoneyBack = strahovSum
            minMoneyBack = round(strahovSum*0.02, 1)
            company.appNewDogovor(DogovorHealth(vznos, time, maxMoneyBack, minMoneyBack))
            company.addMoney(vznos)
            totalVznos += vznos
            massNowMonthDogovors.append(DogovorHealth(vznos, time, maxMoneyBack, minMoneyBack))

    setDemandCompanyZero()

    return massNowMonthDogovors

def getTypeDogovor(dogovor):
    if isinstance(dogovor, DogovorHouse):
        return f'на дом'
    elif isinstance(dogovor, DogovorCar):
        return f'на машину'
    elif isinstance(dogovor, DogovorHealth):
        return f'на здоровье'

def readDogovors():
    for dogovor in company.getListOfDogors():
        print(f'{dogovor.getInfo()}, тип - {getTypeDogovor(dogovor)}')

mainWindow = Tk()
mainWindow.title('Страховая контора')
mainWindow.geometry('500x550-600-200')

labelMoneyCompany = Label(
    mainWindow,
    text=f'Деньги конторы: {round(company.getMoney(), 1)}',
    font=16
    )
def placeCompanyData():
    labelMoneyCompany.place(x=0, y=0)
    labelAllClients.place(x=0, y=20)

labelAllClients = Label(
    mainWindow,
    text=f'Всего клиентов(договоров): {len(company.getListOfDogors())}',
    font=16)
placeCompanyData()

def startGame():
    btnStartGame.place_forget()

    mainGame()

def refreshCompanyData():

    labelMoneyCompany.place_forget()
    labelAllClients.place_forget()

    labelMoneyCompany.config(text=f'Деньги конторы: {round(company.getMoney(), 1)}')
    labelAllClients.config(text=f'Оставшиеся клиенты(договоры): {len(company.getListOfDogors())}')

    placeCompanyData()

countMonth = None
totalPaymentToPopulation = None
countDeniedDogovors = 0
massMonth = []
massSellsStrah = []
def mainGame():

    labelCountMonth = Label(
        mainWindow,
        text='Введите количество месяцев (6-24)',
        justify='center'
    )
    labelCountMonth.place(x=162, y=120)

    entryCountMonth = Entry(
        justify='center'
    )
    entryCountMonth.place(x=192, y=150)


    def clearReadCountMonth():
        entryCountMonth.delete(0, END)
        btnReadCountMonth.place_forget()
        labelCountMonth.place_forget()
        entryCountMonth.place_forget()

    labelErrorCountMonthNotInt = Label(
        mainWindow,
        text='Введено некорректное значение месяца!'
    )
    labelErrorCountMonthNotSix = Label(
        mainWindow,
        text='Введено некорректное количество месяцев!'
    )

    def readCountMonth():
        global countMonth
        if entryCountMonth.get().isdigit():
            currentCountMonth = int(entryCountMonth.get())
            if 6 <= currentCountMonth <= 24:
                countMonth = currentCountMonth
                clearReadCountMonth()
                labelErrorCountMonthNotInt.place_forget()
                labelErrorCountMonthNotSix.place_forget()

                startProcess(countMonth)
            else:
                labelErrorCountMonthNotInt.place_forget()
                labelErrorCountMonthNotSix.place(x=142, y=210)
        else:
            labelErrorCountMonthNotSix.place_forget()
            labelErrorCountMonthNotInt.place(x=142, y=210)

    btnReadCountMonth = Button(
        text='Прочитать',
        command=readCountMonth
    )
    btnReadCountMonth.place(x=222, y=180)

    def startProcess(countMonth):

        labelCurrentRateHouse = Label(
            mainWindow,
            text=f'Текущая ставка на жилье: {rateHouse}%',
            font=("Helvetica", 10)
        )

        labelCurrentRateCar = Label(
            mainWindow,
            text=f'Текущая ставка на авто: {rateCar}%',
            font=("Helvetica", 10)
        )

        labelCurrentRateHealth = Label(
            mainWindow,
            text=f'Текущая ставка на здоровье: {rateHealth}%',
            font=("Helvetica", 10)
        )

        labelHintRate = Label(
            mainWindow,
            text=f'Ставка - взнос, который платит клиент'
        )

        def createLabelsCurrentRate():

            def hideCurrentRates():
                labelCurrentRateHouse.place_forget()
                labelCurrentRateCar.place_forget()
                labelCurrentRateHealth.place_forget()
                labelHintRate.place_forget()

            def setCurrentRates():
                labelCurrentRateHouse.config(text=f'Текущая ставка на жилье: {rateHouse}%')
                labelCurrentRateCar.config(text=f'Текущая ставка на авто: {rateCar}%')
                labelCurrentRateHealth.config(text=f'Текущая ставка на здоровье: {rateHealth}%')

                labelCurrentRateHouse.place(x=0, y=460)
                labelCurrentRateCar.place(x=0, y=480)
                labelCurrentRateHealth.place(x=0, y=500)
                labelHintRate.place(x=0, y=530)

            hideCurrentRates()

            setCurrentRates()

        createLabelsCurrentRate()

        def changeCondition():

            def hideChangeCondition():
                labelChangeRateHouse.place_forget()
                entryRateHouse.place_forget()

                labelChangeRateCar.place_forget()
                entryRateCar.place_forget()

                labelChangeRateHealth.place_forget()
                entryRateHealth.place_forget()

                btnChangeAllRates.place_forget()

            def setChangeCondition():
                labelChangeRateHouse.place(x=0, y=5)
                entryRateHouse.place(x=190, y=5)

                labelChangeRateCar.place(x=0, y=45)
                entryRateCar.place(x=190, y=45)

                labelChangeRateHealth.place(x=0, y=85)
                entryRateHealth.place(x=190, y=85)

                btnChangeAllRates.place(x=80, y=130)

            def clearEntryRates():
                entryRateHouse.delete(0, END)
                entryRateCar.delete(0, END)
                entryRateHealth.delete(0, END)

            def changeAllRates():
                global rateHouse, rateCar, rateHealth
                if entryRateHouse.get() != '' and entryRateHouse.get().isdigit():
                    rateHouse = float(entryRateHouse.get())
                if entryRateCar.get() != '':
                    rateCar = float(entryRateCar.get())
                if entryRateHealth.get() != '':
                    rateHealth = float(entryRateHealth.get())

                createLabelsCurrentRate()

                clearEntryRates()

            windowChangeCondition = Tk()
            windowChangeCondition.geometry('300x200-400-200')

            btnChangeAllRates = Button(
                windowChangeCondition,
                text='Изменить',
                command=changeAllRates,
                padx=28,
                pady=16
            )

            entryRateHouse = Entry(
                windowChangeCondition,
                justify='center',
                width=5
            )

            labelChangeRateHouse = Label(
                windowChangeCondition,
                text=f'Изменить ставку на жилье в %'
            )

            entryRateCar = Entry(
                windowChangeCondition,
                justify='center',
                width=5
            )

            labelChangeRateCar = Label(
                windowChangeCondition,
                text=f'Изменить ставку на авто в %'
            )

            entryRateHealth = Entry(
                windowChangeCondition,
                justify='center',
                width=5
            )

            labelChangeRateHealth = Label(
                windowChangeCondition,
                text=f'Изменить ставку на здоровье в %'
            )

            setChangeCondition()

            windowChangeCondition.mainloop()

        btnChangeCondition = Button(
            mainWindow,
            text='Изменить условия договоров',
            command=changeCondition,
            padx=10,
            pady=20
        )
        btnChangeCondition.place(x=302, y=60)

        def getInfoNowMonth():
            windowInfoOfLastMonth = Tk()
            windowInfoOfLastMonth.geometry('200x200-400-200')

            btnInfoInTxt = Button(
                windowInfoOfLastMonth,
                text=f'Информация в виде текста',
                command=getInfoNowMonthInTxt,
                pady=10,
                padx=14
            )

            btnInfoInGraphBar = Button(
                windowInfoOfLastMonth,
                text=f'Информация о доходах',
                command=getInfoNowMonthInGraphBar,
                pady=10,
                padx=22
            )

            btnInfoInGraphPie = Button(
                windowInfoOfLastMonth,
                text=f'Соотношение видов страховок',
                command=getInfoNowMonthInGraphPie,
                pady=10,
                padx=6
            )

            btnInfoInTxt.place(x=10, y=10)
            btnInfoInGraphBar.place(x=10, y=70)
            btnInfoInGraphPie.place(x=4, y=130)

            windowInfoOfLastMonth.mainloop()


        def getInfoNowMonthInTxt():
            windowInfoOfLastMonthInTxt = Tk()
            windowInfoOfLastMonthInTxt.geometry('300x300-400-200')

            countHouseDogovors = 0
            countCarDogovors = 0
            countHealthDogovors = 0
            for el in massNowMonthDogovors:
                if isinstance(el, DogovorHouse):
                    countHouseDogovors += 1
                elif isinstance(el, DogovorCar):
                    countCarDogovors += 1
                elif isinstance(el, DogovorHealth):
                    countHealthDogovors += 1
            labelInfoHouseDogovors = Label(
                windowInfoOfLastMonthInTxt,
                text=f'Было приобретено {countHouseDogovors} страховок на жилище'
            )
            labelInfoHouseDogovors.place(x=10, y=0)

            labelInfoCarDogovors = Label(
                windowInfoOfLastMonthInTxt,
                text=f'Было приобретено {countCarDogovors} страховок на авто'
            )
            labelInfoCarDogovors.place(x=10, y=30)

            labelInfoHealthDogovors = Label(
                windowInfoOfLastMonthInTxt,
                text=f'Было приобретено {countHealthDogovors} страховок на жизнь'
            )
            labelInfoHealthDogovors.place(x=10, y=60)

            labelInfoNalog = Label(
                windowInfoOfLastMonthInTxt,
                text=f'Было выплачено {round(totalPaymentToPopulation, 2)} за страхвоые случаи'
            )
            labelInfoNalog.place(x=10, y=90)

            labelInfoDohod = Label(
                windowInfoOfLastMonthInTxt,
                text=f'Было куплено страховок на {round(massSellsStrah[currentMonth - 1], 2)}'
            )
            labelInfoDohod.place(x=10, y=120)

            labelInfoNalog = Label(
                windowInfoOfLastMonthInTxt,
                text=f'Был выплачен налог на сумму {round(company.getNalog(), 2)}'
            )
            labelInfoNalog.place(x=10, y=150)

            labelInfoDogovorsDenied = Label(
                windowInfoOfLastMonthInTxt,
                text=f'Количество истекших договоров {countDeniedDogovors}'
            )
            labelInfoDogovorsDenied.place(x=10, y=180)

            windowInfoOfLastMonthInTxt.mainloop()

        def getInfoNowMonthInGraphBar():
            plt.close()
            plt.bar(massMonth, massSellsStrah, width=0.5, linewidth=0.5, edgecolor='k')
            plt.xticks(rotation=30)

            def addlabels(x, y):
                for i in range(len(x)):
                    plt.text(i, y[i], y[i], ha='center')

            addlabels(massMonth, massSellsStrah)

            plt.show()

        def getInfoNowMonthInGraphPie():
            plt.close()
            massNames = ['Жилье', 'Авто', 'Здоровье']

            countHouseDogovors = 0
            countCarDogovors = 0
            countHealthDogovors = 0

            for el in massNowMonthDogovors:
                if isinstance(el, DogovorHouse):
                    countHouseDogovors += 1
                elif isinstance(el, DogovorCar):
                    countCarDogovors += 1
                elif isinstance(el, DogovorHealth):
                    countHealthDogovors += 1

            massCount = [countHouseDogovors, countCarDogovors, countHealthDogovors]

            plt.pie(massCount,
                    labels=massNames,
                    autopct='%1.1f%%',
                    explode=[0.05 for x in range(len(massCount))],
                    shadow=True,
                    rotatelabels=True,
                    wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"}
            )

            plt.show()

        btnGetInfoNowMonth = Button(
            mainWindow,
            text=f'Узнать инфо за месяц',
            command=getInfoNowMonth,
            padx=32,
            pady=20
        )
        btnGetInfoNowMonth.place(x=300, y=130)

        def nextMonth():
            global countMonth, massNowMonthDogovors, totalPaymentToPopulation, totalVznos, countDeniedDogovors, currentMonth
            massNowMonthDogovors = []
            countMonth -= 1
            currentMonth += 1
            totalPaymentToPopulation = 0
            countDeniedDogovors = 0
            massNowMonthDogovors = appClients()
            countDeniedDogovors = company.checkDogovors()
            totalPaymentToPopulation = getPaymentToPopulation()
            company.giveMoney(totalPaymentToPopulation)
            company.payNalog()
            massSellsStrah.append(int(totalVznos))
            setNewRandintDemand()
            if countMonth == 0:
                totalVznos = 0
                btnNextMonth.place_forget()
            else:
                totalVznos = 0
            massMonth.append(f'Месяц {currentMonth}')
            labelCurrentMonth.config(text=f'Месяц: {currentMonth}')

            refreshCompanyData()

        btnNextMonth = Button(
            mainWindow,
            text=f'Следующий месяц',
            command=nextMonth,
            pady=20,
            padx=40
        )
        btnNextMonth.place(x=302, y=320)

        labelCurrentMonth = Label(
            mainWindow,
            text=f'Месяц: {currentMonth}',
            font=14
        )
        labelCurrentMonth.place(x=0, y=350)

    def endProcess():
        pass

btnStartGame = Button(
    mainWindow,
    text='Начать игру',
    command=startGame,
    font=20,
    width=32,
    height=5
)
btnStartGame.place(x=102,y=300)



mainWindow.mainloop()