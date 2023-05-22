class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class Bus:
    def __init__(self, couch, driver, departure, frm, to):
        self.couch = couch
        self.driver = driver
        self.departure = departure
        self.frm = frm
        self.to = to
        self.seat = ["Empty" for i in range(40)]

class busCompany:
    totalBus = 5
    busList = []   # dummy Database

    def addBus(self):
        busNo = int(input("Enter Bus no.: "))
        flag = 1
        for bus in self.busList:
            if busNo == bus['couch']:
                print("Bus already added")
                flag = 0
                break

        if flag:
            busDriver = input("Enter bus driver name: ")
            busDeparture = input("Enter bus departure time: ")
            busFrm = input("Enter bus departure from: ")
            busTo = input("Enter bus destination to: ")
            self.newBus = Bus(busNo, busDriver, busDeparture, busFrm, busTo)
            self.busList.append(vars(self.newBus))
            print("Bus added successfully")

class busCounter(busCompany):
    userList = []
    busSeat = 40
    def reservation(self):
        busNo = int(input("Enter Bus no.: "))
        for bus in self.busList:
            if busNo == bus['couch']:
                passenger = input('Enter passenger name: ')
                seatNo = int(input("Enter seat no. to book: "))
                if seatNo-1 > self.busSeat:
                    print('Invalid seat number')
                elif bus['seat'][seatNo-1] != "Empty":
                    print("Seat already booked")
                else:
                    bus['seat'][seatNo-1] = passenger
            else:
                print("Invalid Bus number")
                break

    def showBusInfo(self):
        busNo = int(input("Enter Bus no.: "))
        for bus in self.busList:
            if bus['couch'] == busNo:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number: {busNo} \t\t Driver: {bus['driver']}")
                print(f"Departure: {bus['departure']}")
                print(f"From: {bus['frm']} \t\t To: {bus['to']}")
                print()
                a = 1
                for i in range(10):
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]}", end="\t")
                        a += 1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()

    def getUser(self):
        return self.userList
    
    def createAccount(self):
        name = input("Enter user name: ")
        flag = 0
        for user in self.getUser():
            if user.username == name:
                print("Username already exists")
                flag = 1
                break
        if flag == 0:
            password = input("Enter password: ")
            self.newUser = User(name, password)
            self.userList.append(vars(self.newUser))
            print("Account created successfully")

    def availableBuses(self):
        if len(self.busList) == 0:
            print("No bus available")
        else:
            for bus in self.busList:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number: {bus['couch']} \t\t Driver: {bus['driver']}")
                print(f"Departure: {bus['departure']}")
                print(f"From: {bus['frm']} \t\t To: {bus['to']}")
                print()
                a = 1
                for i in range(10):
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]}", end="\t")
                        a += 1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}.{bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()





a = Bus(10, 'Naim', '12:00 PM', 'Cumilla', 'Sylhet')
print(vars(a))

company = busCompany()
company.addBus()
company.addBus()

counter1 = busCounter()
counter1.reservation()
#counter1.showBusInfo()
counter1.availableBuses()
