class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall_no, rows, cols):
        self._hall_list.append([hall_no, rows, cols])


class Hall(Star_Cinema):
    __seats={}
    __show_list = []
    __show_id=[]
    __booked_seats_data = []
    __total_seat = 0
    __rows=0
    __cols=0

    def __init__(self, hall_no, rows, cols, seats={}, show_list=[]):
        self.__hall_no = hall_no
        self.__rows = rows
        self.__cols = cols
        self.__total_seat = self.__cols * self.__rows
        self.entry_hall(hall_no, rows, cols)

    def entry_show(self, show_id, movie_name, time):
        __new_show = (show_id, movie_name, time)
        self.__show_list.append(__new_show)
        self.__show_id.append(show_id)
        __seats_data = [[chr(j + 65) + str(i+1) for i in range(self.__cols)] for j in range(self.__rows)]
        self.__seats[show_id] = __seats_data


    def book_seats(self):
        __customer_name = input('ENTER CUSTOMER NAME: ')
        __phone_no = input("ENTER PHONE NUMBER: ")
        __show_no = input("ENTER SHOW NO: ")
        __temp_list = []
        __failed_seat_list = []
        __already_booked_list=[]
        __available_seats=[]

        def display_ticket():
            print()
            print(f"{' ' * 5} {'#' * 10} TICKET BOOKED SUCCESSFULLY!! {'#' * 10}")
            print('*' * 65)
            print()
            print(f"NAME: {__customer_name}")
            print(f"PHONE NUMBER: {__phone_no}")
            print()
            for movie in self.__show_list:
                movie = list(movie)
                if __show_no == movie[0]:
                    print("MOVIE NAME: " + movie[1] + " \t\tTIME: " + movie[2])
            print("TICKETS: ", end='')
            for ticket in __available_seats:
                print(ticket+" ", end="")
            print("\nHall: "+self._hall_list[0][0])
            print()
            print('*' * 65)
            print()

        if __show_no not in self.__show_id:
            print()
            print('*' * 30)
            print("\nID didn't match with any show!\n")
            print('*' * 30)
            print()
            return False
        else:
            __seat_no_data = []
            try:
                tickets = int(input("ENTER NUMBER OF TICKETS: "))
            except:
                print()
                print('*' * 40)
                print('\nInvalid number of tickets\n')
                print('*' * 40)
                print()
                return False
            if tickets - 1 > self.__total_seat:
                print()
                print('*' * 40)
                print('\nInvalid number of tickets\n')
                print('*' * 40)
                print()
                return False
            for x in range(0,tickets):
                __seat_no_data.append(input("ENTER SEAT NO ("+str(x+1)+"): ").upper())

            
            for data in __seat_no_data:
                if [__show_no, data] in self.__booked_seats_data:
                    __already_booked_list.append(data)
                elif data not in sum(self.__seats[__show_no], []):
                    __failed_seat_list.append(data)
                else:
                    __available_seats.append(data)
                    __temp_list.append([__show_no, data])
            
            if __already_booked_list != [] or __failed_seat_list != []:
                print()
                print('*' * 40)

                if __already_booked_list != []:
                    print("\nTHESE SEATS WERE BOOKED - " + " ".join(__already_booked_list))

                if __failed_seat_list != []:
                    print("\nINVALID SEAT NO - " + " ".join(__failed_seat_list))
                
                print()
                print('*' * 40)
                print()

                if __temp_list == []:
                    return False

                ans = input("Do you want to book the remaining seats? Enter Y to continue or press any key to quit:  ").upper()
                print()

                if ans == "Y":
                    for dt in __temp_list:
                        self.__booked_seats_data.append(dt)
                else:
                    return False
                display_ticket()

            elif __temp_list != []:
                for dt in __temp_list:
                    self.__booked_seats_data.append(dt)
                display_ticket()
                
            else:
                return False

    def view_show_list(self):
        print()
        print('*' * 90)
        print()
        for show in self.__show_list:
            print(f"MOVIE NAME: {str(show[1])} \t\t SHOW ID: {str(show[0])} \t\t TIME: {str(show[2])}")
        print()
        print('*' * 90)
        print()

    def view_available_seats(self, show_id):
        if show_id not in self.__show_id:
            print()
            print('*' * 30)
            print("\nID didn't match with any show!\n")
            print('*' * 30)
            print()
            return False
        print()
        for movie in self.__show_list:
            movie = list(movie)
            if show_id == movie[0]:
                print("MOVIE NAME: "+movie[1]+"   TIME: "+movie[2])
        print("X for already booked seats")
        print()
        print('*' * 50)
        for data in self.__seats[show_id]:
            for data_val in data:
                if [show_id, data_val] in self.__booked_seats_data:
                    print("X \t", end="")
                else:
                    print(data_val+"\t", end="")
            print()
        print('*' * 50)
        print()



# if __name__ == "__main__":
import datetime
day_time_1 = str(datetime.date.today())+" 04:00 PM"
day_time_2 = str(datetime.date.today())+" 07:00 PM"
day_time_3 = str(datetime.date.today())+" 10:00 PM"

my_hall = Hall('H12', 5, 7)
my_hall.entry_show("101", 'The X-files', day_time_1)
my_hall.entry_show("102", 'Thunder feast', day_time_2)
my_hall.entry_show("103", 'Komola Sundori', day_time_3)

error = False
choice = ''
while True:
    print("1. VIEW ALL SHOWS TODAY \n2. VIEW AVAILABLE SEATS \n3. BOOK TICKET \n0. EXIT")
    try:
        if error == False:
            choice = int(input("ENTER OPTION: "))
        else:
            error = False
            choice = int(input("PLEASE PROVIDE A VALID OPTION (1-3): "))  
        if choice == 1:
            my_hall.view_show_list()
        elif choice == 2:
            __show_id = input("ENTER SHOW ID: ")
            my_hall.view_available_seats(__show_id)
        elif choice == 3:
            my_hall.book_seats()
        elif choice == 0:
            break
        else:
            error = True

    except:
        error = True