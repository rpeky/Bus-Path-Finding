import os
import time
import JsonProcessingFunctions
import UserClass
from datetime import datetime, timedelta

def makeneededfiles():
    folderstocheck = ['BusArrivalsRequest', 'BusServicesRequest', 'BusRoutesRequest', 'BusStopsRequest', 'Routes_BusService']
    for folder in folderstocheck:
        if(os.path.isdir(folder)):
            pass
        else:
            os.mkdir(folder)
    return

def firstrungendata():
    makeneededfiles()
    JsonProcessingFunctions.BuildBusData()

def idxfind(lst, w):
    for idx, i in enumerate(lst):
        if i[0]==w:
            return idx
    

def main():
    #firstrungendata()
    # u1=UserClass.User()
    # buses=u1.obtain_busin_initialstop()
    # print(buses)
    # sol = u1.find_immediate_solution(buses)
    #print(sol)
    a=JsonProcessingFunctions.BusArrivalData_gettimeforarrival(85039,45)
    proctnow = datetime.strptime(datetime.now().time().strftime("%H:%M:%S"),"%H:%M:%S")
    print(a)
    print(proctnow)
    print(a-proctnow)

    #print(a-tnow)
    return 


if __name__ == "__main__":
    start_time=time.process_time()
    main()
    print(time.process_time()-start_time)

