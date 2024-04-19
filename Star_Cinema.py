class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        Star_Cinema().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        seats = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seats

    def book_seats(self, id, num_seats):
        if id not in self.seats:
            return

        booked_seats = []
        for i in range(num_seats):
            while True:
                row = int(input("Enter Seat Row: "))
                col = int(input("Enter Seat Col: "))
                if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                    print("Invalid seat.")
                    continue
                if self.seats[id][row][col] == 1:
                    print("Seat is already booked.")
                else:
                    self.seats[id][row][col] = 1
                    booked_seats.append((row, col))
                    break

        print(f"Seats {booked_seats} booked successfully.")

    def view_show_list(self):
        print("Shows running:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.seats:
            print("Invalid show ID.")
            return

        print("Available seats:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == 0:
                    print("[0]", end="")
                else:
                    print("[X]", end="")
            print()

hall1 = Hall(6, 7, 1)
hall1.entry_show("101", "Dune", "12:00 PM")
hall1.entry_show("102", "Interstellar", "03:00 PM")

hall2 = Hall(8, 10, 2)
hall2.entry_show("103", "Godzilla x Kong: The New Empire", "06:00 PM")
hall2.entry_show("104", "Avengers", "09:00 PM")

print("Welcome to Star Cinema!")
while True:
    print("\n1. View all shows today\n2. View available seats\n3. Book ticket\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for hall in Star_Cinema.hall_list:
            hall.view_show_list()

    elif choice == "2":
        show_id = input("Enter the ID of the show: ")
        for hall in Star_Cinema.hall_list:
            hall.view_available_seats(show_id)

    elif choice == "3":
        show_id = input("Enter the ID of the show: ")
        num_seats = int(input("Enter the number of seats to book: "))
        for hall in Star_Cinema.hall_list:
            hall.book_seats(show_id, num_seats)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please enter again.")
