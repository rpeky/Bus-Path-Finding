import os
import time
import JsonProcessingFunctions
import UserClass

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
    

def main():
    firstrungendata()

    return 


if __name__ == "__main__":
    start_time=time.process_time()
    main()
    print(time.process_time()-start_time)

