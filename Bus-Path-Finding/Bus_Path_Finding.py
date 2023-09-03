import os
import time
import JsonProcessingFunctions

def makeneededfiles():
    folderstocheck = ['BusArrivalsRequest', 'BusServicesRequest', 'BusRoutesRequest', 'BusStopsRequest']
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
    
    JsonProcessingFunctions.benchtest()
    return


if __name__ == "__main__":
    start_time=time.process_time()
    main()
    print(time.process_time()-start_time)

