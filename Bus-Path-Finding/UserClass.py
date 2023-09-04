import json
import JsonProcessingFunctions

class User():
    
    def __init__(self):
        self.pathfound = False
        self.initialstop = ""
        self.destination = ""
        with open('bsclisttostore.json','r') as f:
            self.bscchecklist = json.load(f)
        with open('bsnlisttostore.json','r') as f:
            self.bsnchecklist = json.load(f)
            
        self.query_initialstop()
        self.query_destination()

        return
    
    def query_initialstop(self):
        while True:
            newstop = input("Enter initial bus stop: \n")
            try:
               if newstop in self.bscchecklist:
                   self.initialstop = newstop
                   print("Valid input")
                   break
               else:
                   raise ValueError
            except ValueError:
                print("Value error! Try again :(")
                continue
            
    def query_destination(self):
        while True:
            endstop = input("Enter destination bus stop: \n")
            try:
               if endstop in self.bscchecklist and endstop != self.initialstop:
                   self.destination = endstop
                   print("Valid input")
                   break
               elif endstop in self.bscchecklist and endstop == self.initialstop:
                   print("Origin and destination cannot be the same stop! You are already there lol")
                   raise ValueError
               else:
                   raise ValueError
            except ValueError:
                print("Value error! Try again :(")
                continue

            
    def obtain_busin_initialstop(self):
        arrivaldata = JsonProcessingFunctions.open_load_json(self.initialstop, 1)
        availiable_bus = []
        for busservice in arrivaldata['Services']:
            availiable_bus.append(busservice['ServiceNo'])
        return availiable_bus
    

   


