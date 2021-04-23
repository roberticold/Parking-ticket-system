import sys


class ParkingGarage():

    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5,]
        self.spaces = len(self.tickets)
        self.currentTicket = {}

    def check_availability(self):
        if self.spaces == 0:
            print("Sorry, we dont have any spots available for the moment.")
        else:
            print(f"Welcome, we have {garage1.spaces} places available ")

    def take_ticket(self):
        while True:
            name = input("Please enter your name: ").lower()
            if name in self.currentTicket:
                print("Please enter another name, this one has been taken already")
            else:
                if self.spaces != 0:
                    self.currentTicket[name] = self.tickets.pop()
                    print(
                        f'{name.upper()}, you are in the spot number {self.currentTicket[name]} and your ticket number is {self.currentTicket[name]}')
                    self.spaces = len(self.tickets)
                    break
                else:
                    print("Sorry, we dont have any spots available for the moment.")
                    break

    def pay_for_ticket(self):
        ticket = input("Please enter your name:  ").lower()
        if ticket in self.currentTicket:
            pay = input(
                "Please insert your method of payment and press  --(y)--:   ").lower()
            if pay == "y":
                self.tickets.append(self.currentTicket[ticket])
                self.spaces = len(self.tickets)
                del self.currentTicket[ticket]
                garage1.leave_garage()
        else:
            print("You dont have any tickets to pay for")

    def leave_garage(self):
        print("You have 15 min to leave")
        print('Have a great day!!!!!')


garage1 = ParkingGarage()


while True:
    try:
        welcome = input(
            "Welcome!!!Please select one option: check-spots/take-ticket/pay-ticket ").lower()
        if welcome == "check-spots":
            garage1.check_availability()
        elif welcome == "take-ticket":
            garage1.take_ticket()
        elif welcome == "pay-ticket":
            garage1.pay_for_ticket()

    except:
        print("Please enter a valid option")
