import random
class ticket:
    def printTicket(self,int,str,gender,pick,destination):
        print("\n\n   *******PASSENGER TICKET*******")
        print("tickets:",int)
        print("Name:", str)
        print("Gender:", gender)
        print("from", pick, "to", destination)
        print("PNR NUMBER:",random.randint(9999,10000))

class manager(ticket):
    tickets=input("Enter no.of tickets:")
    name=input("Enter passenger name:")
    gender=input("Enter passenger gender:")
    pick=input("Enter Starting point: ")
    destination=input("Enter Destination: ")
    obj=ticket()
    obj.printTicket(ticket,name,gender,pick,destination)