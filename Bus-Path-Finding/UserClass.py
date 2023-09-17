import json
from Bus_Path_Finding import idxfind
import JsonProcessingFunctions
import datetime


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

        #availbus = self.obtain_busin_initialstop()

        
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
    
    def idxfind(self, lst, w):
        for idx, i in enumerate(lst):
            if i[0]==w:
                return idx
    
    def find_route(self):
        pass

    # check direct solution
    # reject if destination is not even along the bus route
    # easiest case - initial and destination lie along either d1 or d2, so its a linear path
    # not likely to happen but can compare to bus changing alternatives for difference in distance
    def find_immediate_solution(self, availbus):
        sol=dict()
        sol['bus_totake']=''
        sol['dist']=100000
        sol['route_tour']=[]
        sol['wait_time']=datetime.timedelta(days=2)
        for bus in availbus:
            routeinfo=JsonProcessingFunctions.open_load_json(bus,5)
            if any(self.destination in sublist for sublist in routeinfo['d1']) or any(self.destination in sublist for sublist in routeinfo['d2']):
                print('destination valid, bus {} has a direct route'.format(bus))
                
                #check stop in d1 or d2
                inid1=False
                inid2=False
                destd1=False
                destd2=False
                
                if any(self.initialstop in sublist for sublist in routeinfo['d1']):
                    inid1=True
                if any(self.initialstop in sublist for sublist in routeinfo['d2']):
                    inid2=True
                if any(self.destination in sublist for sublist in routeinfo['d1']):
                    destd1=True
                if any(self.destination in sublist for sublist in routeinfo['d2']):
                    destd2=True
                    
                #Most straightforward cases

                #both route 1 and direct
                
                if inid1==True and destd1==True and inid2==False and destd2==False:
                    start_indx=idxfind(routeinfo['d1'],self.initialstop)
                    end_indx=idxfind(routeinfo['d1'],self.destination)
                    #print(start_indx,end_indx)
                    
                    # if end index is before start index, reject
                    if end_indx > start_indx:
                        tempdist = routeinfo['d1'][end_indx][1]-routeinfo['d1'][start_indx][1]
                        temptime = JsonProcessingFunctions.BusArrivalData_gettimeforarrival_nextbusifnegative1dayresult_returntimeforbustoreach(self.initialstop, bus)
                        if tempdist<sol['dist'] and temptime < sol['wait_time']:
                            print('bus {} currently has fastest path'.format(bus))
                            sol['bus_totake']=bus
                            sol['dist']=tempdist
                            sol['route_tour']=[]
                            for _ in range(start_indx,end_indx+1):
                                sol['route_tour'].append(routeinfo['d1'][_][0])
                            sol['wait_time'] = temptime
                        #for debug purposes
                        elif temptime > sol['wait_time']:
                            print('bus {} takes too long'.format(bus))
                        elif tempdist > sol['dist']:
                            print('theres a shorter route')
                        else:
                            print('bus {} not currently in service'.format(bus))

                    else:
                        print('end index is before start index, reject for straightforward case')
                
                #both route 2 and direct

                elif inid1==False and destd1==False and inid2==True and destd2==True:
                    start_indx=idxfind(routeinfo['d2'],self.initialstop)
                    end_indx=idxfind(routeinfo['d2'],self.destination)

                    # reject if end index is before start index
                    if end_indx > start_indx:
                        tempdist=routeinfo['d2'][end_indx][1]-routeinfo['d2'][start_indx][1]
                        temptime = JsonProcessingFunctions.BusArrivalData_gettimeforarrival_nextbusifnegative1dayresult_returntimeforbustoreach(self.initialstop, bus)
                        if tempdist<sol['dist'] and temptime < sol['wait_time']:
                            print('bus {} currently has fastest path'.format(bus))
                            sol['bus_totake']=bus
                            sol['dist']=tempdist
                            sol['route_tour']=[]
                            for _ in range(start_indx,end_indx+1):
                                sol['route_tour'].append(routeinfo['d2'][_][0])
                            sol['wait_time'] = temptime
                        #for debug purposes
                        elif temptime > sol['wait_time']:
                            print('bus {} takes too long'.format(bus))
                        elif tempdist > sol['dist']:
                            print('theres a shorter route')
                        else:
                            print('bus {} not currently in service'.format(bus))

                    else:
                        print('end index is before start index, reject for straightforward case')        
                

                # potentially long cases (the opposite the road type cases, but currently only path finding through taking the bus)
                # Start in route 1 but end in route 2, so possible to stay till interchange and swap to other route by retaking the bus
                elif inid1==True and destd1==False and inid2==False and destd2==True:
                    start_indx=idxfind(routeinfo['d1'],self.initialstop)
                    end_indx=idxfind(routeinfo['d2'],self.destination)
                    


                
                # Start in route 2 but end in route 1, so possible to stay till interchange and swap to other route by retaking the bus
                elif inid1==False and destd1==False and inid2==True and destd2==True:
                    start_indx=idxfind(routeinfo['d2'],self.initialstop)
                    end_indx=idxfind(routeinfo['d1'],self.destination)
                    


            else:
                print('bus {} has no direct route'.format(bus))
                continue
            
        print('\n')    
        print('final solution:')    
        print(sol)            
        return sol
    

   


