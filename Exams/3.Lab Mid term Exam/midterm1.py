class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall_no, rows, cols):
        hall1 = Hall(hall_no, rows, cols)
        self.hall_list.append(hall1)

class Hall(Star_Cinema):
    #show_list=[]
    def __init__(self, hall_no, rows, cols, seats={}, show_list=[]):
        self.hall_no = hall_no      # hall_id
        self.rows = rows
        self.cols = cols
        self.seats = seats         # dictionary of seats information
        #self.seat = ["Empty" for i in range(300)]
        self.show_list = show_list  # list of tuples
        

        # hall1 = Hall(11, 20, 50)
        # hall1.seats = {}
        # hall1.show_list = [()]

        # self.hall_list.append(hall1)

        #print(hall1)

    def entry_show(self, show_id, movie_name, time):
        show_list=[]
        newShow = (show_id, movie_name, time)
        self.show_list.append(newShow)

        show_id = int(input("Enter Show ID Number: "))
        flag = 1
        for show in self.show_list:
            if show_id == show_id in [show[0] for show in self.show_list]:
                print("Show already added")
                flag = 0
                break

        if flag:
            #show_id = input("Enter show_id: ")
            movie_name = input("Enter movie_name: ")
            time = input("Enter Show-time: ")
            self.newShow = (show_id, movie_name, time)
            self.show_list.append(self.newShow)
            print("Show added successfully")

    def book_seats(self, customer_name, phone_no, show_id):

        seats = [[chr(j+65)+str(i) for i in range(cols)] for j in range(rows)]
        seatDict = dict(show_id, seats)

        show_no = int(input("Enter show no.: "))
        for show in self.show_list:
            if show_no == show_id in [show[0] for show in self.show_list]:
                customer_name = input('Enter Customer name: ')
                phone_no = int(input("Enter Phone number: "))
                seat_no = int(input("Enter seat no. to book: "))
                
                if seat_no-1 > self.total_seat:
                    print('Invalid seat number')
                elif show['seat'][seat_no-1] != "Empty":
                    print("Seat already booked")
                else:
                    show['seat'][seat_no-1] = customer_name

                    print(f"{' '*10} {'#'*10} TICKET BOOKED SUCCESSFULLY!! {'#'*10}")
                    print('*'*100)
                    print(f"NAME: {customer_name}")
                    print(f"PHONE NUMBER: {phone_no}")
                    print()
                    print(f"MOVIE NAME: {movie_name[i]} \t\t TIME: {time[i]}")
                    print(f"SEAT NUMBERS: {seat_no}")
                    print(f"HALL: {hall_no}")
                    print()
                    print('*'*100)
            else:
                print("Invalid Show ID")
                break

    def view_show_list(self):
        movie_name = [show[1] for show in self.show_list]
        show_id = [show[0] for show in self.show_list]
        time = [show[2] for show in self.show_list]
        
        print('*'*70)
        print()
        i=0
        for show in self.show_list:
            print(f"MOVIE NAME: {movie_name[i]} \t\t SHOW ID: {show_id[i]} \t\t TIME: {time[i]}")
            i = i+1
        print()
        print('*'*70)

    def view_available_seats(self, show_id):


        # Printing the seat arrangement as per sample replica
        rows = 
        cols = 
        seats = [[chr(j+65)+str(i) for i in range(cols)] for j in range(rows)]
        #print(seats)

        print('*'*70)
        print()
        for x in seats:
            for y in x:
                print(y, end="\t\t")
            print()
        print()
        print('*'*70)

        seats[2][1] = 'X'
        seats[2][3] = 'XX'

        print('*'*70)
        print()
        for x in seats:
            for y in x:
                print(y, end="\t\t")
            print()
        print()
        print('*'*70)


hall1 = Hall('A101', 20, 50)
hall1.entry_show(101, 'Titanic', '12PM')
print(hall1.show_list)
#hall1.view_show_list()

while True:
    
    print("1. VIEW ALL SHOWS TODAY \n2. VIEW AVAILABLE SEATS \n3. BOOK TICKET")
    choice = int(input("ENTER OPTION: "))

    if choice == 1:
        hall1.view_show_list()
    elif choice == 2:
        show_id = input("ENTER SHOW ID: ")
        hall1.view_available_seats(show_id)
    elif choice == 3:
        customer_name = input('ENTER CUSTOMER NAME: ')
        phone_no = input("ENTER CUSTOMER PHONE NUMBER: ")
        show_id = input("ENTER SHOW ID: ")
        no_of_tickets = int(input("ENTER NUMBER OF TICKETS: "))
        for i in range(no_of_tickets):
            seat_no = [input("ENTER SEAT NUMBER: ")]

        




