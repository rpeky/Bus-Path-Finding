import http
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

    filetoadd = timesskip+"_ServicesData.json"
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

    filetoadd = timesskip+"_RoutesData.json"
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

    filetoadd = timesskip+"_StopsData.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusStopsRequest')
    full_path = os.path.join(newdir, filetoadd)
    with open(full_path,'w') as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return

