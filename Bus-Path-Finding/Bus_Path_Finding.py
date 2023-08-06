import os
import time

def makeneededfiles():
    folderstocheck = ['BusArrivalsRequest', 'BusServicesRequest', 'BusRoutesRequest', 'BusStopsRequest']
    for folder in folderstocheck:
        if(os.path.isdir(folder)):
            pass
        else:
            os.mkdir(folder)
    return

def main():
    makeneededfiles()
    return


if __name__ == "__main__":
    start_time=time.process_time()
    main()
    print(time.process_time()-start_time)

