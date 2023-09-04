import httplib2 as http
import json
import os
from urllib.parse import urlparse

headers = { 'AccountKey': '4BXSLAQ5T+C4NJ6TA9/qjA==',
            'accept':   'application/json' 
            }

def BusArrivalData(BusStopCode):
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode='+str(BusStopCode))
    target.geturl()
    method = 'GET'
    body = ''

    h = http.Http()

    response, content = h.request(
        target.geturl(),
        method,
        body,
        headers
        )

    jsonObj = json.loads(content)

    filetoadd = str(BusStopCode)+"_ArrivalData.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusArrivalsRequest')
    full_path = os.path.join(newdir, filetoadd)
    with open(full_path,'w') as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return

def BusServicesData(skip):
    timesskip=str(skip*500)
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusServices?$skip='+timesskip)
    target.geturl()
    method = 'GET'
    body = ''

    h = http.Http()

    response, content = h.request(
        target.geturl(),
        method,
        body,
        headers
        )

    jsonObj = json.loads(content)

    filetoadd = str(skip)+"_ServicesData.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusServicesRequest')
    full_path = os.path.join(newdir, filetoadd)
    with open(full_path,'w') as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return

def BusRoutesData(skip):
    timesskip=str(skip*500)
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip='+timesskip)
    target.geturl()
    method = 'GET'
    body = ''

    h = http.Http()

    response, content = h.request(
        target.geturl(),
        method,
        body,
        headers
        )

    jsonObj = json.loads(content)

    filetoadd = str(skip)+"_RoutesData.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusRoutesRequest')
    full_path = os.path.join(newdir, filetoadd)
    with open(full_path,'w') as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return

def BusStopsData(skip):
    timesskip=str(skip*500)
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip='+timesskip)
    target.geturl()
    method = 'GET'
    body = ''

    h = http.Http()

    response, content = h.request(
        target.geturl(),
        method,
        body,
        headers
        )

    jsonObj = json.loads(content)

    filetoadd = str(skip)+"_StopsData.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusStopsRequest')
    full_path = os.path.join(newdir, filetoadd)
    with open(full_path,'w') as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return

# def generate_busstopdict():
    
#     pass

# loading locations
# file_loc      filesuffix                      folderlocation
#    0          NA                              NA
#    1          _ArrivalData.json               BusArrivalsRequest
#    2          _ServicesData.json              BusServicesRequest
#    3          _RoutesData.json                BusRoutesRequest
#    4          _StopsData.json                 BusStopsRequest
#    5          _ServiceRouteInfo.json          Routes_BusService

def open_load_json(file_idx, file_loc):
    
    filesuffix = [
        'error: convenience index',
        '_ArrivalData.json',
        '_ServicesData.json',
        '_RoutesData.json',
        '_StopsData.json'  ,
        '_ServiceRouteInfo.json'
        ]    
    
    folderlocation = [
        'error: convenience index',
        'BusArrivalsRequest',
        'BusServicesRequest',
        'BusRoutesRequest',
        'BusStopsRequest',
        'Routes_BusService'
        ]

    filename = str(file_idx)+str(filesuffix[int(file_loc)])
    cwd = os.getcwd()
    newdir = os.path.join(cwd, folderlocation[int(file_loc)])
    full_path = os.path.join(newdir, filename)
    f = open(full_path)
    jsob = json.load(f)
    return jsob

def BuildBusData():
    
    for i in range(2):
        BusServicesData(i)
    
    for i in range(51):
        BusRoutesData(i)

    for i in range(11):
        BusStopsData(i)
        
# consolidate data into one big dictionary, output to json for easier reference in future

#bsc list should contain a tuple containing the bus stop code and which stopsdata page the stop is in (for future reference if needed)
    bsclist=[]
    bsclisttostore=[]
    for i in range(11):
        stopdatapage = open_load_json(i,4)
        for bsc in stopdatapage['value']:
            bsclist.append((bsc['BusStopCode'],i,bsc['Description']))
            bsclisttostore.append(bsc['BusStopCode'])
    with open('bsclisttostore.json','w') as outfile:
        json.dump(bsclisttostore, outfile)        
            
    bsnlist=[]
    bsnlisttostore=[]
    for i in range(2):
        servicesdata = open_load_json(i,2)
        for bsn in servicesdata['value']:
            bsnlist.append((bsn['ServiceNo'],i))
            bsnlisttostore.append(bsn['ServiceNo'])
    with open('bsnlisttostore.json','w') as outfile:
        json.dump(bsnlisttostore, outfile)   
            
    for bsc in bsclisttostore:
        BusArrivalData(bsc)
        
    for bsn in bsnlisttostore:
        generate_busserviceroute(bsn)
 
    return

def generate_busserviceroute(busservno):
    direc1stops=[]
    direc2stops=[]
    serviceroute = {'d1':direc1stops, 
                    'd2':direc2stops}
    #maybe can integrate into build data when generating the routesdata json, test if fn works first tho
    for _ in range(51):
        routedata = open_load_json(_,3)
        for info in routedata['value']:
            if info['ServiceNo'] == busservno and info['Direction']==1:
                direc1stops.append((info['BusStopCode'],info['Distance']))
            elif info['ServiceNo'] == busservno and info['Direction']==2:
                direc2stops.append((info['BusStopCode'],info['Distance']))
            else:
                pass
    
    filetoadd = busservno+"_ServiceRouteInfo.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'Routes_BusService')
    full_path = os.path.join(newdir, filetoadd)
    with open(full_path,'w') as outfile:
        json.dump(serviceroute, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return

def benchtest():

    
    return