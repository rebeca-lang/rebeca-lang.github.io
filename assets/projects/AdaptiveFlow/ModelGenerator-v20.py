#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xml.etree.ElementTree as ET
import pandas as pd
import pickle
import networkx as nx
import matplotlib.pyplot as plt
import os.path
import os, sys
import re
from numpy import *
import random

print ('Number of arguments:', len(sys.argv), 'arguments.')

xml_files = ['environment', 'topology', 'configuration']
modelFileName = 'model'
root_file = {}

if(len(sys.argv) == 4):
    root_file['environment'] = ET.parse(sys.argv[1]).getroot()
    root_file['topology'] = ET.parse(sys.argv[2]).getroot()
    root_file['configuration'] = ET.parse(sys.argv[3]).getroot()
elif(len(sys.argv) == 5):
    root_file['environment'] = ET.parse(sys.argv[1]).getroot()
    root_file['topology'] = ET.parse(sys.argv[2]).getroot()
    root_file['configuration'] = ET.parse(sys.argv[3]).getroot()
    modelFileName = sys.argv[4]
else:
    print('NUMBER OF ARGUMENT NOT SUFFICIENT: \n 1-environmet.xml \n 2-topology.xml \n 3-configuration.xml \n 4-modelFileName(optional)')
    print('USING DEFAULT FILES!!!')
    root_file = {file : ET.parse('../input/' + file + '.xml').getroot() for file in xml_files}


# In[2]:


# Function for parsing and splitting a string to a list of numbers
def extractNumber(s):
    l = []
    for t in s.split():
        try:
            num = t.replace('[','')
            #num = num.replace(',','')
            num = num.replace(']','')
            l.append(int(num))
        except ValueError:
            pass
    if(len(l) == 1):
        return l[0]
    else:
        return l


# In[3]:


def extractNetworkData(root):
    segments = {}
    lengthTot = []
    for segment in root.iter('segment'):
        segments[segment.get('id')] = {'x' : segment.get('x'), 'y' : segment.get('y'),
                                 'length': segment.get('length'), 'freespeed' : segment.get('freespeed'),
                                 'capacity': segment.get('capacity'), 'available' : segment.get('available'),
                                 'N': segment.get('N'), 'NE' : segment.get('NE'),
                                 'E': segment.get('E'), 'ES' : segment.get('ES'),
                                 'S': segment.get('S'), 'SW' : segment.get('SW'),
                                 'W': segment.get('W'), 'WN' : segment.get('WN'),
                                 'directions': segment.get('directions')}
        lengthTot.append(int(segment.get('length')))

    return segments, int(sum(lengthTot) / float(len(lengthTot)))


# In[4]:


# Extract cell id on the environment from a given coordinate x,y
def getEnvironmentSegmentId(environment,x,y):
    for identifier, value in environment.items():
        if (value['x'] == x and value['y'] == y):
            return identifier
    return None


# In[5]:


def extractTopologyData(root, environment, numOfRows, numOfColumns):
    POIs = {}
    routes = {}
    maxRouteLength = numOfRows + numOfColumns
    index = 0
    for POI in root.iter('poi'):
        x = POI.get('x')
        y = POI.get('y')
        segment = getEnvironmentSegmentId(environment,x,y)
        if (segment == None):
            print('Error in topology file, position not defined in the environment, id: ', POI.get('id'))
            return

        if(POI.get('type') == 'ParkingStation'):
            POIs[POI.get('id')] = { 'x' : x, 'y' : y, 'type' : POI.get('type')}
        elif(POI.get('type') == 'ChargingStation'):
            POIs[POI.get('id')] = {'x' : x, 'y' : y,'type' : POI.get('type'), 'chargingTime' : POI.get('chargingTime')}
        else:
            POIs[POI.get('id')] = {'x' : x, 'y' : y,'type' : POI.get('type'), 'loadTime' : POI.get('loadTime')}
    
    index = 0
    
    for route in root.iter('route'):
        #routes[route.get('origin'),route.get('destination')] = {'path' : route.get('path').split(',')}
        routes[route.get('origin'),route.get('destination')] = {'path' : [(int(environment[segment]['x']) * numOfRows) + int(environment[segment]['y']) for segment in route.get('path').split(',')]}
        if(len(route.get('path').split(',')) > maxRouteLength):
            maxRouteLength = len(route.get('path').split(','))

    return POIs, routes, maxRouteLength


# In[6]:


# deprecated
# def extractTracksData(root, topology):
#     maxNumOfSteps = 0;
#     for track in root.iter('track'):
#         t = track.text.replace('],[',';').replace('[','').replace(']','')
#         if(len(t.split(';')) > maxNumOfSteps):
#             maxNumOfSteps = len(t.split(';'))

#     #print(str(maxNumOfSteps))
#     tracks = {}
#     for track in root.iter('track'):
#         origin = track.get('POIorigin')
#         destination = track.get('POIdestination')

#         if (origin not in topology or destination not in topology):
#             print('Error in track definition, origin or destination not in the topology: track ', track.get('id'))
#             return

#         route = ['-1,-1'] * maxNumOfSteps
#         t = track.text.replace('],[',';').replace('[','').replace(']','').split(';')

#         for index in range(len(t)):
#             route[index] = t[index]

#         #print(route)

#         tracks[track.get('id')] = {'POIorigin' : origin, 'POIdestination' : destination,
#                                    'route' : str(route).replace('[','{').replace(']','}').replace("{'",'{{').replace("'}", '}}').replace("', '",'},{')}

#     return tracks, maxNumOfSteps


# In[7]:


def extractConfigurationData(root):
    system = {'resending_period' : root.find('system').find('resending_period').get('value'),
                'number_vehicles' : root.find('system').find('number_vehicles').get('value'),
                'safe_distance' : root.find('system').find('safe_distance').get('value'),
                'battery_limit' : root.find('system').find('battery_limit').get('value'),
                'policy' : root.find('system').find('policy').get('value'),
                'obstacle_occurences' : root.find('system').find('obstacle_occurences').get('value'),
                'obstacle_number' : root.find('system').find('obstacle_number').get('value'),
                'obstacle_max_time' : root.find('system').find('obstacle_max_time').get('value'),
                'obstacle_max_duration' : root.find('system').find('obstacle_max_duration').get('value'),
                'max_attempts' : root.find('system').find('max_attempts').get('value')}

    machines = {}
    for machine in root.iter('machine'):
        machines[machine.get('id')] = {'type' : machine.get('type'),
                                       'leavingTime' : machine.get('leavingTime'),
                                       'fuelCapacity' : machine.get('fuelCapacity'),
                                       'fuelConsumption' : machine.get('fuelConsumption'),
                                       'speed': machine.get('speed'),
                                       'emission' : machine.get('emission'),
                                       'capacity' : machine.get('capacity'),
                                       'unloadTime': machine.get('unloadTime'),
                                       'tasks' : ('{' + machine.find('tasks').text + '}')}

    return  system , machines


# In[8]:


environment, avg_length = extractNetworkData(root_file['environment'])


# In[9]:


# Generate the matrices, and adjacency matrix
# The version 19 consider also the direction of the segment. It creates the adjacencyMatrix
# to be used for calculating dijkstra.
def generateMatrices(environment):
    x = 0
    y = 0

    for segment in environment.values():
        if (int(segment['x']) > x):
            x = int(segment['x'])
        if (int(segment['y']) > y):
            y = int(segment['y'])
    x += 1
    y += 1

    rows = x
    columns = y

    availabilityMatrix = zeros((x, y), dtype=bool)
    capacityMatrix = zeros((x, y), dtype=int16)
    lengthMatrix = zeros((x, y), dtype=int16)
    speedMatrix = zeros((x, y), dtype=int16)
    adjacencyMatrix = zeros((x * y, x * y), dtype=bool)

    for identifier, segment in environment.items():

        x = int(segment['x'])
        y = int(segment['y'])

        #print(x,y,segment['directions'].split(','))

        availabilityMatrix[x][y] = segment['available'] == 'true'
        capacityMatrix[x][y] = int(segment['capacity'])
        lengthMatrix[x][y] = int(segment['length'])
        speedMatrix[x][y] = int(segment['freespeed'])
        
        if('N' in segment['directions'].split(',')):
            adjacencyMatrix[ (x * columns) + y ][ ((x - 1) * columns) + y ] = True
        if('NE' in segment['directions'].split(',')):
            adjacencyMatrix[ (x * columns) + y ][ ((x - 1) * columns) + (y + 1) ] = True
        if('E' in segment['directions'].split(',')):
            adjacencyMatrix[ (x * columns) + y ][ (x * columns) + (y + 1) ] = True
        if('ES' in segment['directions'].split(',')):
            adjacencyMatrix[ (x * columns) + y ][ ((x + 1) * columns) + (y + 1) ] = True
        if('S' in segment['directions'].split(',')):
            adjacencyMatrix[ (x * columns) + y ][ ((x + 1) * columns) + y ] = True
        if('SW' in segment['directions'].split(',')):
            adjacencyMatrix[ (x * columns) + y ][ ((x + 1) * columns) + (y - 1) ] = True
        if('W' in segment['directions'].split(',')):
            adjacencyMatrix[ (x * columns) + y ][ (x * columns) + (y - 1) ] = True
        if('WN' in segment['directions'].split(',')):
            adjacencyMatrix[ (x * columns) + y ][ ((x -1) * columns) + (y - 1) ] = True
        
        #adjacencyMatrix[ (x * columns) + y ][ (x * columns) + y ] = True

    return {'capacityMatrix' : capacityMatrix, 'lengthMatrix' : lengthMatrix,
            'speedMatrix' : speedMatrix, 'availabilityMatrix' : availabilityMatrix, 
           'adjacencyMatrix' : adjacencyMatrix}, rows, columns


# In[10]:


matrices, rows, columns = generateMatrices(environment)
NUM_OF_ROWS = str(rows)
NUM_OF_COLUMNS = str(columns)
NUM_OF_SEGMENTS = str(rows * columns)


# In[35]:


#print(matrices['adjacencyMatrix'])


# In[36]:


# Check PoIs position
def hasTopologyAPoIAtCoord(x, y, topology):
    for poi in topology.values():
        if (poi['x'] == str(x) and poi['y'] == str(y)):
            return True
    return False


# In[37]:


topology, routes, maxRouteLength = extractTopologyData(root_file['topology'],environment, rows, columns)
numOfRoutes = len(routes)
#print(routes)
# String data
NUM_OF_ROUTES = str(numOfRoutes)
MAX_TRACK_LENGTH = str(maxRouteLength + 1)


# In[38]:


CHARGING_TIME = str(topology['1']['chargingTime'])


# In[39]:


# Deprecated
# tracks, maxNumOfSteps = extractTracksData(root_file['track'],topology)
#tracks


# In[40]:


system, machines = extractConfigurationData(root_file['configuration'])
#system


# In[42]:


OBSTACLE_OCCURRENCES = system['obstacle_occurences']
OBSTACLE_NUMBER = system['obstacle_number']
OBSTACLE_MAX_TIME = system['obstacle_max_time']
OBSTACLE_MAX_DURATION = system['obstacle_max_duration']
#print(OBSTACLE_OCCURRENCES,OBSTACLE_NUMBER,OBSTACLE_MAX_TIME,OBSTACLE_MAX_DURATION)


# In[44]:


# In[74]:


#Generate random obstacles for random times
def generateRandomObstaclesString(numOfEvents, numOfObstacles, topology, numOfSegments, numOfRows):
    changesEnv = zeros((numOfEvents, numOfObstacles), dtype=int16) - 1
    for i in range(numOfEvents):
        obstacles = random.randint(1,numOfObstacles + 1)
        for j in range(obstacles):
            obstacleSegmentId = random.randint(-1,numOfSegments)
            x = int(obstacleSegmentId / numOfRows)
            y = obstacleSegmentId % numOfRows
            if(hasTopologyAPoIAtCoord(x,y,topology)):
                changesEnv[i][j-1] = -1
            else :
                changesEnv[i][j-1] = obstacleSegmentId
            #print(changesEnv[i][j])
    return str(changesEnv).replace('[','{').replace(']','}').replace(' ',',').replace(',,',',').replace('{,','{').replace(',}','}').replace('\n','').replace(',,',',').replace('{,','{')

CHANGES_ENV = generateRandomObstaclesString(int(OBSTACLE_OCCURRENCES),int(OBSTACLE_NUMBER),topology, int(NUM_OF_SEGMENTS), int(NUM_OF_ROWS))
#print(CHANGES_ENV)


# In[45]:


# In[75]:


def generateRandomTimesStringForObstacle(numOfEvents, maxTime, maxDuration):
    changesTimes = zeros((numOfEvents, 2), dtype=int16)
    lastTime = 0
    for i in range(numOfEvents):
        initTime = random.randint(lastTime, lastTime + int(maxTime / numOfEvents))
        lastTime = random.randint(initTime + 1, (initTime + 1) + maxDuration )

        changesTimes[i][0] = initTime
        changesTimes[i][1] = lastTime

    return str(changesTimes).replace('[','{').replace(']','}').replace(' ',',').replace(',,',',').replace('{,','{').replace(',}','}').replace('\n','').replace(',,',',').replace('{,','{')

CHANGES_TIME = generateRandomTimesStringForObstacle(int(OBSTACLE_OCCURRENCES),int(OBSTACLE_MAX_TIME),int(OBSTACLE_MAX_DURATION))
#print(CHANGES_TIME)


# In[46]:


# In[76]:


# Data extracted from files, used for the model specification
numOfSegments = str(len(environment))
numOfPOIs = str(len(topology))
numOfMachine = str(len(machines))
queueSize = str(len(machines) + 1)
print('segments:',numOfSegments,', POIs:',numOfPOIs,', machines:' ,numOfMachine)


# In[47]:


# Mapping fixed routes into a matrix int[numOfRoutes][maxRouteLength]
# origin = m ---> destination = n
# Route from m to n =routesMatrix[(m+n)*(m+n+1)/2 + n][...] --> Cantor Pairing Function
def mapRoutesToMatrix(routes, numOfPOIs, maxRouteLength):
    maxNumOfRoutes = (numOfPOIs - 1) * ( (numOfPOIs - 1) * 2 + 1) + (numOfPOIs - 1)
    routesMatrix = zeros((maxNumOfRoutes, maxRouteLength + 1), dtype = int16) - 1
    for origin,destination in routes:
        x = int(origin)
        y = int(destination)
        
        for i in range(len(routes[origin,destination]['path'])):
            #print(origin,destination,i,routes[origin,destination]['path'][i])
            routesMatrix[int( ((x + y) * ( x + y + 1) / 2 + y) )][i] = routes[origin,destination]['path'][i] 
        
    return routesMatrix, maxNumOfRoutes


# In[48]:


routesMatrix, maxNumOfRoutes = mapRoutesToMatrix(routes, len(topology),maxRouteLength)
MAX_NUM_OF_ROUTES = str(maxNumOfRoutes)
#print(str(routesMatrix))


# In[49]:


# In[77]:


# Mapping of matrices into Rebeca code
def mapMatrixIntoRebecaString(matrix):
    matrixString = re.sub('\s+',',',str(matrix.tolist()))
    #print(matrixString)

    return matrixString.replace('[,','{').replace('[','{').replace(']','}').replace('},','},\n').replace(',,',',').replace(',\n,',',\n').lower()


# In[50]:


# In[78]:


# Matrices for the model
MAP_SPEEDS = mapMatrixIntoRebecaString(matrices['speedMatrix'])
MAP_LENGTHS = mapMatrixIntoRebecaString(matrices['lengthMatrix'])
MAP_CAPACITIES = mapMatrixIntoRebecaString(matrices['capacityMatrix'])
MAP_AVAILABILITY = mapMatrixIntoRebecaString(matrices['availabilityMatrix'])
MAP_ADJACENCY_MATRIX = mapMatrixIntoRebecaString(matrices['adjacencyMatrix'])
MAP_ROUTES_MATRIX = mapMatrixIntoRebecaString(routesMatrix)
#print(MAP_ROUTES_MATRIX)


# In[51]:


# In[79]:


# Tasks vehicles matrix
def fromMachineToTasksMatrix(machines):
    returnString = '{'
    for machine in machines.values():
        returnString += machine['tasks'] + ','
        numOfTasks = len(machine['tasks'].split(','))
    returnString += '}'

    return returnString.replace('},}','}}').replace('},{','},\n{'), str(numOfTasks)

TASKS_VEHICLES, NUM_OF_TASKS = fromMachineToTasksMatrix(machines)


# In[52]:


# In[80]:


# Generate distance matrix between PoIs
def createDistanceMatrixBetweenPoIs(topology):
    returnString = '{'
    for i in range(len(topology)):
        returnString += '{'
        for j in range(len(topology)):
            xDist = abs(int(topology[str(i)]['x']) - int(topology[str(j)]['x']))
            yDist = abs(int(topology[str(i)]['y']) - int(topology[str(j)]['y']))
            returnString += str((xDist + yDist) * avg_length) + ','
        returnString += '}'
    returnString += '}'
    return returnString.replace(',}{','},\n{').replace(',}}','}}')

TASKS_DISTANCES = createDistanceMatrixBetweenPoIs(topology)


# In[53]:


# In[81]:


# Extract all info from a dictionary
def mapEnvironmentCellsOrChannelsInfoIntoString(element, dictionary):
    string = [0] * len(dictionary)
    for identifier, value in dictionary.items():
        string[int(identifier)] = int(value[element])

    return str(string).replace('[','{').replace(']','}')


# In[54]:


# In[82]:


def mapMachinesInfoIntoString(element,dictionary):
    string = [''] * len(dictionary)
    for identifier, value in dictionary.items():
        string[int(identifier)] = value[element]

    return str(string).replace('[','{').replace(']','}').replace("'",'')


# In[55]:


# In[83]:


# Machines info
CAPACITY = mapMachinesInfoIntoString('capacity', machines)
VEHICLES_BATTERIES = mapMachinesInfoIntoString('fuelCapacity', machines)
BATTERY_CONSUMPTION = mapMachinesInfoIntoString('fuelConsumption', machines)
VEHICLES_SPEED = mapMachinesInfoIntoString('speed', machines)
CO2_EMISSIONS = mapMachinesInfoIntoString('emission', machines)
UNLOAD_TIME = mapMachinesInfoIntoString('unloadTime', machines)
LEAVING_TIME = mapMachinesInfoIntoString('leavingTime', machines)


# In[56]:


# In[84]:


def mapPoIsLocationIntoString(topology):
    IoPs_LOCATION = '{'
    parkingStations = '{'
    chargingStations = '{'
    loadUnloadStations = '{'
    loadTime = '{'
    numOfPoI = 0
    numOfPS = 0
    numOfCS = 0
    numOfLUS = 0
    for i in range(len(topology)):
        x = topology[str(i)]['x']
        y = topology[str(i)]['y']
        poiType = topology[str(i)]['type']
        IoPs_LOCATION += '{' + x + ',' + y + '}'
        numOfPoI += 1
        if(poiType == 'ParkingStation'):
            parkingStations += '{' + x + ',' + y + '}'
            numOfPS += 1
        elif(poiType == 'ChargingStation'):
            chargingStations += '{' + x + ',' + y + '}'
            numOfCS += 1
        else:
            loadUnloadStations += '{' + x + ',' + y + '}'
            numOfLUS += 1
            loadTime +=  topology[str(i)]['loadTime'] + ', '

    IoPs_LOCATION += '}'
    parkingStations += '}'
    chargingStations += '}'
    loadUnloadStations += '}'
    loadTime += '}'

    a = IoPs_LOCATION.replace('}{','},{')
    b = parkingStations.replace('}{','},{')
    c = chargingStations.replace('}{','},{')
    d = loadUnloadStations.replace('}{','},{')
    e = loadTime.replace(', }','}')

    return a , str(numOfPOIs), b, str(numOfPS), c, str(numOfCS), d, str(numOfLUS), e


# In[57]:


# In[85]:


IoPs_LOCATION, NUM_OF_POIs, PARKING_STATION_POSITIONS, NUM_OF_PARKING_STATIONS, CHARGING_STATION_POSITIONS, NUM_OF_CHARGING_STATIONS, LOAD_UNLOAD_POSITIONS, NUM_OF_LOAD_UNLOAD_STATIONS, LOAD_TIME = mapPoIsLocationIntoString(topology)


# In[86]:


#LOAD_TIME


# In[58]:


# In[87]:


# Deprecated
# def mapTracksIntoString(dictionary):
#     string = [''] * len(dictionary)
#     for identifier, track in dictionary.items():
#         string[int(identifier)] = track['route']

#     return str(string).replace('[','{').replace(']','}').replace("}',",'},\n').replace("'",'')


# In[88]:


#TRACKS = mapTracksIntoString(tracks)
#print(TRACKS)


# In[89]:


# Deprecated
#main for PoIs
# def extractMainPoiIs(PoIs):
#     string = ''
#     for identifier, poi in PoIs.items():
#         if (poi['type'] == 'CrossController'):
#             string += (poi['type'] + ' ' + identifier + '():();' + '\n'
#                       )
#         elif (poi['type'] == 'DecisionStation'):
#             string += (poi['type'] + ' ' + identifier + '():(' + poi['N'] + ',' + poi['E'] + ',' + poi['S'] + ',' + poi['W'] + ',' +
#                       poi['x'] + ',' + poi['y'] + ');' + '\n'
#                       )

#         elif (poi['type'] != 'PrePoint'):
#             string += (poi['type'] + ' ' + identifier + '():(' + poi['N'] + ',' + poi['E'] + ',' + poi['S'] + ',' + poi['W'] + ',' +
#                       poi['x'] + ',' + poi['y'] + ',' + poi['operationTime'] + ');' + '\n'
#                       )
#         else:
#             string += (poi['type'] + ' ' + identifier + '(' + poi['segments'] + '):(' + poi['x'] + ',' + poi['y'] + ');' + '\n'
#                       )
#     return string


# In[90]:


#poisMain = extractMainPoiIs(topology)


# In[59]:


# In[91]:


#main for PoIs
def extractMainSegments(environment):
    string = ''
    for identifier, segment in environment.items():
        string += ('Segment ' + identifier + '():(' +
                    segment['N'] + ', \t' + segment['NE'] + ', \t' +
                    segment['E'] + ', \t' + segment['ES'] + ', \t' +
                    segment['S'] + ', \t' + segment['SW'] + ', \t' +
                    segment['W'] + ', \t' + segment['WN'] + ', \t' +
                    segment['x'] + ', ' +
                    segment['y'] + ');' + '\n')

    return string
MAIN = extractMainSegments(environment)
# Deprecated
# def checkPoIsAdjacency(poi, poiId, topology):
#     if (poi != 'crossController'):
#         if (poiId == 'null'):
#             return ('null,' + '-1')
#         else:
#             return (topology[poiId])


# In[60]:


# In[92]:



modelString =('env int RESENDING_PERIOD = ' + system['resending_period'] + '; // time to wait before ask again the availability of a segment' + '\n' +
'env int NUMBER_VEHICLES = ' + system['number_vehicles'] + '; // number of simulated vehicles' + '\n' +
'env int SAFE_DISTANCE = ' + system['safe_distance'] + '; // meters' + '\n' +
'env int BATTERY_LIMIT = ' + system['battery_limit'] + '; // battery reserve' + '\n' +
'env int MAX_ATTEMPTS = ' + system['max_attempts'] + '; // max attempts on the same segment' + '\n' +
'' + '\n' +
'/* Used adaptive policy: 1 wait, 2: overpass, 3: change route, 4: rong */' + '\n' +
'env int POLICY = ' + system['policy'] + ';' + '\n' +
'' + '\n' +
'' + '\n' +
'/* Fuel configuration: tank size and costs, wat/km for each vehicle */' + '\n' +
'env double[' + numOfMachine + '] VEHICLES_BATTERIES = ' + VEHICLES_BATTERIES + '; // watt' + '\n' +
'env int[' + numOfMachine + '] VEHICLES_SPEED = ' + VEHICLES_SPEED + '; // m/s' + '\n' +
'env double[' + numOfMachine + '] BATTERY_CONSUMPTION = ' + BATTERY_CONSUMPTION + '; // max battery consumption: watt/meter' + '\n' +
'' + '\n' +
'env int[' + numOfMachine + '] CAPACITY= ' + CAPACITY + ';		// loads(tons) that can be transported by vehicles' + '\n' +
'' + '\n' +
'/* CO2 emissions per vehicles grams per 100 meters */' + '\n' +
'env double[' + numOfMachine + '] CO2_EMISSIONS = ' + CO2_EMISSIONS + '; // grams/100 meters' + '\n' +
'' + '\n' +
'env double[' + numOfMachine + '] UNLOAD_TIME = ' + UNLOAD_TIME + ';' + '\n' +
'' + '\n' +
'/* Environment random changes */' + '\n' +
'env int[' + OBSTACLE_OCCURRENCES + '][' + OBSTACLE_NUMBER + '] CHANGES_ENV = ' + CHANGES_ENV + ';' + '\n' +
'env int[' + OBSTACLE_OCCURRENCES + '][2] CHANGES_TIME = ' + CHANGES_TIME + ';' + '\n' +
'env int OBSTACLE_OCCURRENCES = ' + OBSTACLE_OCCURRENCES + ';' + '\n' +
'env int OBSTACLE_NUMBER = ' + OBSTACLE_NUMBER + ';' + '\n' +
'' + '\n' +
'/* Location of PoIs */' + '\n' +
'env int[' + NUM_OF_PARKING_STATIONS + '][2] PARKING_STATION_POSITIONS = ' + PARKING_STATION_POSITIONS + ';' + '\n' +
'env int[' + NUM_OF_CHARGING_STATIONS + '][2] CHARGING_STATION_POSITIONS = ' + CHARGING_STATION_POSITIONS + ';' + '\n' +
'env int[' + NUM_OF_LOAD_UNLOAD_STATIONS + '][2] LOAD_UNLOAD_POSITIONS = ' + LOAD_UNLOAD_POSITIONS + '; // Vehicles can load or unload at each point' + '\n' +
'' + '\n' +
'env int[' + NUM_OF_POIs + '][2] IoPs_LOCATION=' + IoPs_LOCATION + ';' + '\n' +
'' + '\n' +
'env int NUM_OF_POIs = ' + NUM_OF_POIs + ';' + '\n' +
'env int NUM_OF_PARKING_STATIONS = ' + NUM_OF_PARKING_STATIONS + ';' + '\n' +
'env int NUM_OF_CHARGING_STATIONS = ' + NUM_OF_CHARGING_STATIONS + ';' + '\n' +
'env int NUM_OF_LOAD_UNLOAD_STATIONS = ' + NUM_OF_LOAD_UNLOAD_STATIONS + ';' + '\n' +
'' + '\n' +
'/* Time needed for charging 1 unit of battery */' + '\n' +
'env double CHARGING_TIME = ' + CHARGING_TIME + ';' + '\n' +
'' + '\n' +
'/* Time needed for load one ton of material */' + '\n' +
'env double[' + NUM_OF_LOAD_UNLOAD_STATIONS + '] LOAD_TIME = ' + LOAD_TIME + ';' + '\n' +
'' + '\n' +
'/* Distances between each PoI */' + '\n' +
' env int[' + NUM_OF_POIs + '][' + NUM_OF_POIs + '] TASKS_DISTANCES = \n' + TASKS_DISTANCES + ';' + '\n' +
'' + '\n' +
'' + '\n' +
'env int MAX_TRACK_LENGTH = ' + MAX_TRACK_LENGTH + ';' + '\n' +
'' + '\n' +
'/* Tasks always start with a loading point id and is alternated with unloading points id, ends with a parking station' + '\n' +
'* After load/unload operation, the vehicle with few battery will reach the battery charging station' + '\n' +
'* Before going back to the parking station, the vehicle reaches th  battery chargin station' + '\n' +
'*      LP   UP   LP   UP   LP   UP' + '\n' +
'* e.g. 0 -> 0 -> 1 -> 0 -> 1 -> 0 -> ...' + '\n' +
'*/' + '\n' +
'env int[' + numOfMachine + '][' + NUM_OF_TASKS + '] TASKS_VEHICLES= \n' + TASKS_VEHICLES + ';' + '\n' +
'' + '\n' +
'env  int NUM_OF_TASKS = ' + NUM_OF_TASKS + ';' + '\n' +
'' + '\n' +
'env int[' + numOfMachine + '] LEAVING_TIME= ' + LEAVING_TIME + ';' + '\n' +
'' + '\n' +
'/* Segments Max Speeds */' + '\n' +
'env int[' + NUM_OF_ROWS + '][' + NUM_OF_COLUMNS + '] MAP_SPEEDS = \n' + MAP_SPEEDS + ';' + '\n' +
'' + '\n' +
'/* Segment Lengths */' + '\n' +
'env int[' + NUM_OF_ROWS + '][' + NUM_OF_COLUMNS + '] MAP_LENGTHS = \n' + MAP_LENGTHS + ';' + '\n' +
'' + '\n' +
'/* Segment Capacities */' + '\n' +
'env int[' + NUM_OF_ROWS + '][' + NUM_OF_COLUMNS + '] MAP_CAPACITIES = \n' + MAP_CAPACITIES + ';' + '\n' +
'' + '\n' +
'/* Whether the cell is available or not(because of obstacles or other). This specifies the initial site map! */' + '\n' +
'env boolean[' + NUM_OF_ROWS + '][' + NUM_OF_COLUMNS + '] MAP_AVAILABILITY= \n' + MAP_AVAILABILITY + ';' + '\n' +
'' + '\n' +
'/* The adjacency matrix. If a vehicle can move from a segment to the other. */' + '\n' +
'env boolean[' + NUM_OF_SEGMENTS + '][' + NUM_OF_SEGMENTS + '] ADJACENCY_MATRIX= \n' + MAP_ADJACENCY_MATRIX + ';' + '\n' +
'' + '\n' +
'/* The pre-given routes. Fixed path specified in topology.xml. */' + '\n' +
'/* origin = m ---> destination = n */' + '\n' +
'/* Route from m to n =routesMatrix[(m+n)*(m+n+1)/2 + n][...] --> Cantor Pairing Function */' + '\n' +
'env int[' + MAX_NUM_OF_ROUTES + '][' + MAX_TRACK_LENGTH + '] ROUTES_MATRIX= \n' + MAP_ROUTES_MATRIX + ';' + '\n' +
'' + '\n' +
'/* Segments ids: map from x,y to segment id*/' + '\n' +
'/* f(x,y) = (id) = ((x * NUM_OF_COLUMNS) + y)' + '\n' +
' * inverse: f(id) = (x,y) =( ((int) id / NUM_OF_COLUMNS) , id % NUM_OF_COLUMNS )' + '\n' +
' */' + '\n' +
'' + '\n' +
'env int NUM_OF_SEGMENTS = ' + NUM_OF_SEGMENTS + ';' + '\n' +
'env int NUM_OF_ROWS = ' + NUM_OF_ROWS + ';' + '\n' +
'env int NUM_OF_COLUMNS = ' + NUM_OF_COLUMNS + ';' + '\n' +
'env int MAX_NUM_OF_ROUTES = ' + MAX_NUM_OF_ROUTES + ';' + '\n' +
'' + '\n' +
'/*********************************************************/' + '\n' +
'' + '\n' +
'reactiveclass Segment(' + queueSize + ') {' + '\n' +
'' + '\n' +
'	knownrebecs{' + '\n' +
'	}' + '\n' +
'' + '\n' +
'	statevars{' + '\n' +
'		/* Neighbours */' + '\n' +
'		@doNotExport' + '\n' +
'		Segment[8] segments;' + '\n' +
'' + '\n' +
'    /* Segment current capacity */' + '\n' +
'    @doNotExport' + '\n' +
'    int currCapacity;' + '\n' +
'    /* Segment position/coordinate on the map */' + '\n' +
'    @doNotExport' + '\n' +
'		int[2] coord;' + '\n' +
'    /* is the segment a PoI */' + '\n' +
'' + '\n' +
'		int arrivedVehicles;' + '\n' +
'' + '\n' +
'    @doNotExport' + '\n' +
'    boolean isParkingStation;' + '\n' +
'    @doNotExport' + '\n' +
'    boolean isChargingStation;' + '\n' +
'    @doNotExport' + '\n' +
'    boolean isLoadUnloadLocation;' + '\n' +
'	}' + '\n' +
'' + '\n' +
'	/* N.B. id of IoPs are the index of array IoPs_LOCATION */' + '\n' +
'	Segment(Segment N, Segment NE,' + '\n' +
'          Segment E, Segment ES,' + '\n' +
'          Segment S, Segment SW,' + '\n' +
'          Segment W, Segment WN,' + '\n' +
'          int x, int y){' + '\n' +
'' + '\n' +
'		segments[0] = N; // NORTH' + '\n' +
'		segments[1] = NE;// NORTH-EAST' + '\n' +
'		segments[2] = E; // EAST' + '\n' +
'		segments[3] = ES;// EAST-SOUTH' + '\n' +
'		segments[4] = S; // SOUTH' + '\n' +
'		segments[5] = SW;// SOUTH-WEST' + '\n' +
'		segments[6] = W; // WEST' + '\n' +
'		segments[7] = WN;// WEST-NORTH' + '\n' +
'' + '\n' +
'		coord[0] = x;' + '\n' +
'		coord[1] = y;' + '\n' +
'' + '\n' +
'    currCapacity = MAP_CAPACITIES[coord[0]][coord[1]];' + '\n' +
'' + '\n' +
'		arrivedVehicles = 0;' + '\n' +
'' + '\n' +
'    isParkingStation = isTheSegmentAParkingStation(coord);' + '\n' +
'    isChargingStation = isTheSegmentAChargingStation(coord);' + '\n' +
'    isLoadUnloadLocation = isTheSegmentALoadUnloadLocation(coord);' + '\n' +
'' + '\n' +
'    /* Start the run if the segment correspond to the parking station and current time=0 */' + '\n' +
'    if (isParkingStation && (now == 0)){' + '\n' +
'      self.startMovingVehicles();' + '\n' +
'    }' + '\n' +
'	}' + '\n' +
'' + '\n' +
'  /* Start the vehicles movements */' + '\n' +
'  msgsrv startMovingVehicles(){' + '\n' +
'    currCapacity = MAP_CAPACITIES[coord[0]][coord[1]];' + '\n' +
'    arrivedVehicles = 0;' + '\n' +
'    for (int vehID = 0; vehID < NUMBER_VEHICLES; vehID++){' + '\n' +
'      double vehBatteryLevel = VEHICLES_BATTERIES[vehID];' + '\n' +
'      int vehSourceTask = 0; // isParkingStation' + '\n' +
'      int vehDestinationTask = TASKS_VEHICLES[vehID][0]; // First Task' + '\n' +
'' + '\n' +
'      int[' + MAX_TRACK_LENGTH + '] currRoute;' + '\n' +
'      int[' + MAX_TRACK_LENGTH + '] failingSegments;' + '\n' +
'      /* Initialize currRoute & failingSegments */' + '\n' +
'      for (int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'        currRoute[i] = -1;' + '\n' +
'        failingSegments[i] = -1;' + '\n' +
'      }' + '\n' +
'' + '\n' +
'      /* Populate the route (sequence of segment Ids) */' + '\n' +
'      self.initRouteWithDijkstra(vehID, 0, 0, vehSourceTask, vehDestinationTask, currRoute, failingSegments, false, vehBatteryLevel, 0, 0, 0) after(LEAVING_TIME[vehID]);' + '\n' +
'      currCapacity--;' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    assertion(currCapacity >= 0, "The segment is out of capacity!");' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  /* The preceding segment asks for the permission of the current segment to allow the vehicle to access it */' + '\n' +
'	msgsrv givePermisionForVehicle(int vehicleId, int taskIndex, int trackIndex, int source, int destination, int[' + MAX_TRACK_LENGTH + '] currRoute, int[' + MAX_TRACK_LENGTH + ']  failingSegments,' + '\n' +
'                                  boolean isLoaded, double battery, double consumedBattery, int movedMaterial, double co2Emission){' + '\n' +
'' + '\n' +
'    /* Check if the current segment is temporarly unavailable*/' + '\n' +
'    boolean isTheSegmentAvailable = isTheSegmentAvailableNow((coord[0] * NUM_OF_COLUMNS) + coord[1], now) && MAP_AVAILABILITY[coord[0]][coord[1]];' + '\n' +
'' + '\n' +
'		if (currCapacity > 0 && isTheSegmentAvailable){' + '\n' +
'			currCapacity--;' + '\n' +
'			((Segment)sender).getPermision(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                                      isLoaded, battery, consumedBattery, movedMaterial, co2Emission);' + '\n' +
'    }' + '\n' +
'		else{' + '\n' +
'			((Segment)sender).segmentNotFree(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                                        isLoaded, battery, consumedBattery, movedMaterial, co2Emission);' + '\n' +
'		}' + '\n' +
'    assertion(currCapacity >= 0, "The segment is out of capacity!");' + '\n' +
'	}' + '\n' +
'' + '\n' +
'  /* The preceding segment informs the segment that the vehicle has accessed */' + '\n' +
'	msgsrv vehicleEntered (int vehicleId, int taskIndex, int trackIndex, int source, int destination, int[' + MAX_TRACK_LENGTH + '] currRoute, int[' + MAX_TRACK_LENGTH + ']  failingSegments,' + '\n' +
'                          boolean isLoaded, double battery, double consumedBattery, int movedMaterial, double co2Emission){' + '\n' +
'    assertion(currCapacity >= 0, "The segment is out of capacity!");' + '\n' +
'' + '\n' +
'    /* Clean failingSegments */' + '\n' +
'    for (int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'       failingSegments[i] = -1;' + '\n' +
'    }' + '\n' +
'' + '\n' +
'  	int nextX = currRoute[trackIndex + 1] == -1 ? -1 : ((int) currRoute[trackIndex + 1] / NUM_OF_COLUMNS);' + '\n' +
'  	int nextY = currRoute[trackIndex + 1] == -1 ? -1 : currRoute[trackIndex + 1] % NUM_OF_COLUMNS;' + '\n' +
'' + '\n' +
'    int operatingTime = 0;' + '\n' +
'' + '\n' +
'    /* Check if the vehicle is arrived to the destination PoI*/' + '\n' +
'    if(nextX == -1 || nextY == -1 || currRoute[trackIndex + 1] == -1){ // Vehicle arrived' + '\n' +
'      /* Check the current position for performing the task */' + '\n' +
'      if(isParkingStation && !isChargingStation && !isLoadUnloadLocation){ // Arrived at the parking station' + '\n' +
'      /* Nothing to do --> end of the day --> restart the run */' + '\n' +
'        arrivedVehicles++;' + '\n' +
'        if(arrivedVehicles == NUMBER_VEHICLES){ // restart the run as the beginning' + '\n' +
'          self.startMovingVehicles() after(100);' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'      else if(!isParkingStation && isChargingStation && !isLoadUnloadLocation){ // Arrived at the parking station' + '\n' +
'        operatingTime = (int)((VEHICLES_BATTERIES[vehicleId] - battery)* CHARGING_TIME);' + '\n' +
'        //delay(chargingTime);' + '\n' +
'        battery = VEHICLES_BATTERIES[vehicleId];' + '\n' +
'      }' + '\n' +
'      else if(!isParkingStation && !isChargingStation && isLoadUnloadLocation){ // Arrived at the loadUnloadLocation' + '\n' +
'        double locationUnloadTime = UNLOAD_TIME[vehicleId];' + '\n' +
'        double locationLoadTime = LOAD_TIME[TASKS_VEHICLES[vehicleId][taskIndex] - NUM_OF_PARKING_STATIONS - NUM_OF_CHARGING_STATIONS];' + '\n' +
'        operatingTime = isLoaded ? (int)(locationUnloadTime * CAPACITY[vehicleId]) : (int)(locationLoadTime * CAPACITY[vehicleId]);' + '\n' +
'' + '\n' +
'        //delay(loadUnloadTime);' + '\n' +
'' + '\n' +
'        movedMaterial = isLoaded ? movedMaterial + CAPACITY[vehicleId] : movedMaterial;' + '\n' +
'        isLoaded = !isLoaded;' + '\n' +
'        taskIndex++;' + '\n' +
'      }' + '\n' +
'      trackIndex = 0;' + '\n' +
'      source = destination;' + '\n' +
'      if( taskIndex == (NUM_OF_TASKS - 1) && isLoadUnloadLocation){' + '\n' +
'        /* Change vehicle plan: reach the charging station before going back to the parking station */' + '\n' +
'        destination = 1;' + '\n' +
'      }' + '\n' +
'      else if (!isParkingStation){' + '\n' +
'        destination = TASKS_VEHICLES[vehicleId][taskIndex];' + '\n' +
'      }' + '\n' +
'      /* Clean the route */' + '\n' +
'      for (int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'          currRoute[i] = -1;' + '\n' +
'          failingSegments[i] = -1;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'    else { // Not arrived' + '\n' +
'      trackIndex++;' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    if(destination != 0 || !isParkingStation)' + '\n' +
'      self.startSendingToNext(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                              isLoaded, battery, consumedBattery, movedMaterial, co2Emission);' + '\n' +
'	}' + '\n' +
'' + '\n' +
'  /* The segment select the next segment, or ask for a re-route process if the vehicle reached the destination */' + '\n' +
'	msgsrv startSendingToNext(int vehicleId, int taskIndex, int trackIndex, int source, int destination, int[' + MAX_TRACK_LENGTH + '] currRoute, int[' + MAX_TRACK_LENGTH + ']  failingSegments,' + '\n' +
'                              boolean isLoaded, double battery, double consumedBattery, int movedMaterial, double co2Emission){' + '\n' +
'' + '\n' +
'    /* Check The Battery Level if the segment is a loadUnloadLocation*/' + '\n' +
'    if((isChargingStation || isLoadUnloadLocation) && currRoute[trackIndex] == -1){' + '\n' +
'      int batteryLifeMeters = (int) battery / BATTERY_CONSUMPTION[vehicleId];' + '\n' +
'      int totalDistance = TASKS_DISTANCES[source][destination] + TASKS_DISTANCES[destination][1];' + '\n' +
'      /* Check if the vehicle has enough battery for reaching the destination task */' + '\n' +
'      if((batteryLifeMeters - BATTERY_LIMIT) < totalDistance){ // Not enough battery' + '\n' +
'        /* Change vehicle plan: reach the charging station */' + '\n' +
'        trackIndex  = 0;' + '\n' +
'        destination = 1;' + '\n' +
'      }' + '\n' +
'      if( taskIndex == (NUM_OF_TASKS - 1) && !isChargingStation){' + '\n' +
'        /* Change vehicle plan: reach the charging station */' + '\n' +
'        trackIndex  = 0;' + '\n' +
'        destination = 1;' + '\n' +
'      }' + '\n' +
'      /* Update the route */' + '\n' +
'      for (int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'        currRoute[i] = -1;' + '\n' +
'        failingSegments[i] = -1;' + '\n' +
'      }' + '\n' +
'      self.initRouteWithDijkstra(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                                                        isLoaded, battery, consumedBattery, movedMaterial, co2Emission) after(1);' + '\n' +
'    }' + '\n' +
'    else {' + '\n' +
'      int nextX = ( (int) currRoute[trackIndex] / NUM_OF_COLUMNS );' + '\n' +
'      int nextY = currRoute[trackIndex] % NUM_OF_COLUMNS;' + '\n' +
'' + '\n' +
'      assertion(nextX != -1 && nextY != -1, "The next movement is not possible, out of track!");' + '\n' +
'' + '\n' +
'      int nextMovement = getNextCardinalMovement(coord, nextX, nextY);' + '\n' +
'' + '\n' +
'  		((Segment)segments[nextMovement]).givePermisionForVehicle(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                                                        isLoaded, battery, consumedBattery, movedMaterial, co2Emission);' + '\n' +
'    }' + '\n' +
'' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  /* The next segment gives the permission of accessing it */' + '\n' +
'	msgsrv getPermision (int vehicleId, int taskIndex, int trackIndex, int source, int destination, int[' + MAX_TRACK_LENGTH + '] currRoute, int[' + MAX_TRACK_LENGTH + ']  failingSegments,' + '\n' +
'                                  boolean isLoaded, double battery, double consumedBattery, int movedMaterial, double co2Emission){' + '\n' +
'' + '\n' +
'    assertion(currCapacity >= 0, "The segment is out of capacity!");' + '\n' +
'' + '\n' +
'		int vehicleSpeed = MAP_SPEEDS[coord[0]][coord[1]] <= VEHICLES_SPEED[vehicleId] ? MAP_SPEEDS[coord[0]][coord[1]] : VEHICLES_SPEED[vehicleId];' + '\n' +
'		int segmentLength = MAP_LENGTHS[coord[0]][coord[1]];' + '\n' +
'    int operatingTime = 0;' + '\n' +
'    operatingTime = ((int)(segmentLength-SAFE_DISTANCE) / vehicleSpeed);' + '\n' +
'		//delay((segmentLength-SAFE_DISTANCE)/vehicleSpeed);' + '\n' +
'' + '\n' +
'		/* Consumptions and emissions are related to the speed of the vehicle */' + '\n' +
'    double batteryConsumption = (BATTERY_CONSUMPTION[vehicleId] / VEHICLES_SPEED[vehicleId]) * vehicleSpeed;' + '\n' +
'		double currentEmission = (CO2_EMISSIONS[vehicleId] / VEHICLES_SPEED[vehicleId]) * vehicleSpeed;' + '\n' +
'' + '\n' +
'		consumedBattery +=  ((int)((batteryConsumption * segmentLength)));' + '\n' +
'		battery =  battery - ((int)((batteryConsumption * segmentLength)));' + '\n' +
'		if(battery < 0)' + '\n' +
'			assertion(false,"The battery is out of charge!");' + '\n' +
'' + '\n' +
'		co2Emission += ( currentEmission * ((int)segmentLength / 100) );' + '\n' +
'    currCapacity++;' + '\n' +
'		((Segment)sender).vehicleEntered(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                                      isLoaded, battery, consumedBattery, movedMaterial, co2Emission) after(operatingTime);' + '\n' +
'' + '\n' +
'	}' + '\n' +
'' + '\n' +
'  /* Create the route from a PoI to the next one */' + '\n' +
'  msgsrv initRouteWithDijkstra(int vehicleId, int taskIndex, int trackIndex, int source, int destination, int[' + MAX_TRACK_LENGTH + '] currRoute, int[' + MAX_TRACK_LENGTH + ']  failingSegments,' + '\n' +
'                                  boolean isLoaded, double battery, double consumedBattery, int movedMaterial, double co2Emission){' + '\n' +
'' + '\n' +
'    int startVertex = coord[0] * NUM_OF_COLUMNS + coord[1];' + '\n' +
'    int destVertex = (IoPs_LOCATION[destination][0] * NUM_OF_COLUMNS) + IoPs_LOCATION[destination][1];' + '\n' +
'' + '\n' +
'    int[' + MAX_TRACK_LENGTH + '] newRoute;' + '\n' +
'    for(int i; i < MAX_TRACK_LENGTH; i++)\n' +
'	    newRoute[i] = -1;' + '\n' +
'    int nextMovement = -1;' + '\n' +
'' + '\n' +
'    if(POLICY != 4){' + '\n' +
'	    /*Init all the route with Dijkstra shortest path algorithm : A* */' + '\n' +
'' + '\n' +
'	    /*************************************************************/' + '\n' +
'	    /* Modify the mapAvailability with the current obstacle */' + '\n' +
'	    boolean[' + NUM_OF_SEGMENTS + '] mapAvailability;' + '\n' +
'' + '\n' +
'	    for (int i = 0; i <NUM_OF_SEGMENTS; i++){' + '\n' +
'	      mapAvailability[i] = MAP_AVAILABILITY[((int)i / NUM_OF_COLUMNS)][i % NUM_OF_COLUMNS];' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    int[' + NUM_OF_SEGMENTS + '][' + NUM_OF_SEGMENTS + '] adjacencyMatrix;' + '\n' +
'	    for (int i = 0; i < NUM_OF_SEGMENTS; i++){' + '\n' +
'	      for (int j = 0; j < NUM_OF_SEGMENTS; j++){' + '\n' +
'	        adjacencyMatrix[i][j] = 0;' + '\n' +
'	      }' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    for (int h = 0; h < NUM_OF_ROWS; h++){' + '\n' +
'	      for (int t = 0; t < NUM_OF_COLUMNS; t++){' + '\n' +
'	        for (int k = 0; k < NUM_OF_ROWS; k++){' + '\n' +
'	          for (int z = 0; z < NUM_OF_COLUMNS; z++) {' + '\n' +
'	            int i = (h * NUM_OF_COLUMNS) + t;' + '\n' +
'	            int j = (k * NUM_OF_COLUMNS) + z;' + '\n' +
'	            if( ( (abs(h - k) <= 1) &&  (abs(t - z) <= 1)) && ((abs(h - k) + abs(t - z) != 0)) ){' + '\n' +
'	              if (mapAvailability[i] && mapAvailability[j] && ADJACENCY_MATRIX[i][j]){' + '\n' +
'	                adjacencyMatrix[i][j] = 1;' + '\n' +
'	              }' + '\n' +
'	              else{' + '\n' +
'	                adjacencyMatrix[i][j] = 99999;' + '\n' +
'	              }' + '\n' +
'	            }' + '\n' +
'	          }' + '\n' +
'	        }' + '\n' +
'	      }' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    /* shortestDistances[i] will hold the shortest distance from src to i */' + '\n' +
'	    int[' + NUM_OF_SEGMENTS + '] shortestDistances;' + '\n' +
'' + '\n' +
'	    /* added[i] will true if vertex i is included in shortest path tree or shortest distance from src to i is finalized */' + '\n' +
'	    boolean[' + NUM_OF_SEGMENTS + '] added;' + '\n' +
'	    /* Initialize added var */' + '\n' +
'	    for(int seg = 0; seg < NUM_OF_SEGMENTS; seg++){' + '\n' +
'	      added[seg] = false;' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    for (int row = 0; row < NUM_OF_ROWS; row++){' + '\n' +
'	      for (int column = 0; column < NUM_OF_COLUMNS; column++){' + '\n' +
'	        int vertexIndex =  row * NUM_OF_COLUMNS + column;' + '\n' +
'	        shortestDistances[vertexIndex] = 999999;' + '\n' +
'	        added[vertexIndex] = false;' + '\n' +
'	      }' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    /* Distance of source vertex from itself is always 0 */' + '\n' +
'	    shortestDistances[startVertex] = 0;' + '\n' +
'' + '\n' +
'	    /* Parent array to store shortest path tree */' + '\n' +
'	    int[' + NUM_OF_SEGMENTS + '] parents;' + '\n' +
'	    /* Initialize parents var */' + '\n' +
'	    for(int seg = 0; seg < NUM_OF_SEGMENTS; seg++){' + '\n' +
'	      parents[seg] = 0;' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    /* The starting vertex does not have a parent */' + '\n' +
'	    parents[startVertex] = -1;' + '\n' +
'' + '\n' +
'	    /* Find shortest path for all vertices */' + '\n' +
'	    for (int k = 1; k < NUM_OF_SEGMENTS; k++){' + '\n' +
'' + '\n' +
'	      /* Pick the minimum distance vertex from the set of vertices not yet processed. nearestVertex is always equal to startNode in first iteration. */' + '\n' +
'	      int nearestVertex = -1;' + '\n' +
'	      int shortestDistance = 999999;' + '\n' +
'	      for (int vertexIndex = 0; vertexIndex < NUM_OF_SEGMENTS; vertexIndex++){' + '\n' +
'	        if (!added[vertexIndex] && shortestDistances[vertexIndex] < shortestDistance){' + '\n' +
'	          nearestVertex = vertexIndex;' + '\n' +
'	          shortestDistance = shortestDistances[vertexIndex];' + '\n' +
'	        }' + '\n' +
'	      }' + '\n' +
'' + '\n' +
'	      /* Mark the picked vertex as processed if there is a link */' + '\n' +
'	      if (nearestVertex != -1){' + '\n' +
'	        added[nearestVertex] = true;' + '\n' +
'' + '\n' +
'	        /* Update dist value of the adjacent vertices of the picked vertex.*/' + '\n' +
'	        for (int vertexIndex = 0; vertexIndex < NUM_OF_SEGMENTS; vertexIndex++){' + '\n' +
'	          int edgeDistance = adjacencyMatrix[nearestVertex][vertexIndex];' + '\n' +
'' + '\n' +
'	          if (edgeDistance > 0 && ((shortestDistance + edgeDistance) < shortestDistances[vertexIndex])){' + '\n' +
'	            parents[vertexIndex] = nearestVertex;' + '\n' +
'	            shortestDistances[vertexIndex] = shortestDistance + edgeDistance;' + '\n' +
'	          }' + '\n' +
'	        }' + '\n' +
'	      }' + '\n' +
'	      else{' + '\n' +
'	        parents[k] = -1;' + '\n' +
'	      }' + '\n' +
'	      /*if (k == destVertex){' + '\n' +
'	        break;' + '\n' +
'	      }*/' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    int[' + MAX_TRACK_LENGTH + '] newSubRoute;' + '\n' +
'	    /* Inizialize newSubRoute var */' + '\n' +
'	    for (int nSR = 0; nSR < MAX_TRACK_LENGTH; nSR++){' + '\n' +
'	      newSubRoute[nSR] = -1;' + '\n' +
'	    }' + '\n' +
'	    newSubRoute[0] = startVertex;' + '\n' +
'	    newSubRoute[shortestDistances[destVertex]] = destVertex;' + '\n' +
'' + '\n' +
'	    int nextVertex = destVertex;' + '\n' +
'' + '\n' +
'	    for(int nSR = shortestDistances[destVertex] - 1; nSR >=0; nSR--){' + '\n' +
'	      if(parents[nextVertex] == -1){' + '\n' +
'	        nextVertex = -1;' + '\n' +
'	        break;' + '\n' +
'	      }' + '\n' +
'	      else{' + '\n' +
'	        if(parents[nextVertex] != startVertex){' + '\n' +
'	          nextVertex = parents[nextVertex];' + '\n' +
'	          newSubRoute[nSR] = nextVertex;' + '\n' +
'	        }' + '\n' +
'	        else{' + '\n' +
'	          break;' + '\n' +
'	        }' + '\n' +
'	      }' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    nextVertex = destVertex;' + '\n' +
'' + '\n' +
'	    for(int parIndex = 0; parIndex < NUM_OF_SEGMENTS; parIndex++){' + '\n' +
'	      if(parents[nextVertex] == -1){' + '\n' +
'	        nextVertex = -1;' + '\n' +
'	        break;' + '\n' +
'	      }' + '\n' +
'	      else{' + '\n' +
'	        if(parents[nextVertex] != startVertex){' + '\n' +
'	          nextVertex = parents[nextVertex];' + '\n' +
'	        }' + '\n' +
'	        else{' + '\n' +
'	          break;' + '\n' +
'	        }' + '\n' +
'	      }' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    /* Copy the old route within the new route */' + '\n' +
'	    for(int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'	    		if(i < trackIndex) {' + '\n' +
'	    		      newRoute[i] = currRoute[i];' + '\n' +
'	    		}' + '\n' +
'	    		else {' + '\n' +
'	    			newRoute[i] = -1;' + '\n' +
'	    		}' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    /* Put the new sub-route within the old one */' + '\n' +
'	    for(int i = 0; i < shortestDistances[destVertex]; i++){' + '\n' +
'	      newRoute[trackIndex + i] = newSubRoute[i + 1];' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    /* Refine the new route in case of double visit to the same segment */' + '\n' +
'	    for (int i = trackIndex; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'	      for (int j = i + 1; j < MAX_TRACK_LENGTH; j++){' + '\n' +
'	        if (newRoute[i] == newRoute[j]){' + '\n' +
'	          /* Move the sub route backward */' + '\n' +
'	          for(int z = i + 1; z < MAX_TRACK_LENGTH - (j - i); z++){' + '\n' +
'	            newRoute[z] = newRoute[z + (j - i)];' + '\n' +
'	          }' + '\n' +
'	          break;' + '\n' +
'	        }' + '\n' +
'	      }' + '\n' +
'	    }' + '\n' +
'' + '\n' +
'	    int nextX = ( (int) nextVertex / NUM_OF_COLUMNS );' + '\n' +
'	    int nextY = nextVertex % NUM_OF_COLUMNS;' + '\n' +
'	    assertion(nextX != -1 && nextY != -1, "Segment not valid, wrong nextX and nextY");' + '\n' +
'	    nextMovement = getNextCardinalMovement(coord, nextX, nextY);' + '\n' +
'	 }' + '\n' +
'	 else{' + '\n' +
'	    /* Put the given fixed-route */' + '\n' +
'	    int routeID = ((source + destination) * (source + destination + 1) / 2) + destination;' + '\n' +
'	    for(int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'	      newRoute[i] = ROUTES_MATRIX[routeID][i];' + '\n' +
'		}' + '\n' +
'' + '\n' +
'	    int nextX = ( (int) newRoute[0] / NUM_OF_COLUMNS );' + '\n' +
'	    int nextY = newRoute[0] % NUM_OF_COLUMNS;' + '\n' +
'	    assertion(nextX != -1 && nextY != -1, "Segment not valid, wrong nextX and nextY");' + '\n' +
'	    nextMovement = getNextCardinalMovement(coord, nextX, nextY);' + '\n' +
'' + '\n' +
'	}' + '\n' +
'' + '\n' +
'   ((Segment)segments[nextMovement]).givePermisionForVehicle(vehicleId, taskIndex, trackIndex, source, destination, newRoute, failingSegments,' + '\n' +
'                                          isLoaded, battery, consumedBattery, movedMaterial, co2Emission) after(1);' + '\n' +
'' + '\n' +
'	}' + '\n' +
'' + '\n' +
'  /* The segment denies the vehicle to access it. According to the policy of adaptation, the vehicle can: wait, overpass, re-route*/' + '\n' +
'	msgsrv segmentNotFree(int vehicleId, int taskIndex, int trackIndex, int source, int destination, int[' + MAX_TRACK_LENGTH + '] currRoute, int[' + MAX_TRACK_LENGTH + ']  failingSegments,' + '\n' +
'                                  boolean isLoaded, double battery, double consumedBattery, int movedMaterial, double co2Emission){' + '\n' +
'' + '\n' +
'    /* Old Choice: Failing segment */' + '\n' +
'    int nextX = currRoute[trackIndex] == -1 ? -1 : ( (int) currRoute[trackIndex] / NUM_OF_COLUMNS );' + '\n' +
'    int nextY = currRoute[trackIndex] == -1 ? -1 : currRoute[trackIndex] % NUM_OF_COLUMNS;' + '\n' +
'    assertion(nextX != -1 && nextY != -1, "Segment not valid, wrong nextX and nextY, segmentNotFree!");' + '\n' +
'    int nextMovement = getNextCardinalMovement(coord, nextX, nextY);' + '\n' +
'' + '\n' +
'    /* Decrease the battery level and increase CO2 emitted' + '\n' +
'     * Consumption and emission values are the lowest ones' + '\n' +
'     */' + '\n' +
'    consumedBattery += (BATTERY_CONSUMPTION[vehicleId] / VEHICLES_SPEED[vehicleId]) * 1;' + '\n' +
'    battery -= (BATTERY_CONSUMPTION[vehicleId] / VEHICLES_SPEED[vehicleId]) * 1;' + '\n' +
'    co2Emission += (CO2_EMISSIONS[vehicleId]   / VEHICLES_SPEED[vehicleId]) * 1;' + '\n' +
'' + '\n' +
'    /* Check the current battery level */' + '\n' +
'	 if(battery < 0){' + '\n' +
'		assertion(false,"The battery is out of charge!");}' + '\n' +
'' + '\n' +
'    int numOfAttempts = getFailingAttemptsNumber(failingSegments, currRoute[trackIndex]);' + '\n' +
'' + '\n' +
'    if(numOfAttempts <= MAX_ATTEMPTS || (POLICY != 1)){' + '\n' +
'      failingSegments[getLength(failingSegments)] = currRoute[trackIndex];' + '\n' +
'' + '\n' +
'      /* Adaptive part */' + '\n' +
'      if (POLICY == 1 || currRoute[trackIndex + 1] == -1){ // WAIT or The next position is the destination PoI' + '\n' +
'        /* 1° Policy: the vehicle wait for a certain amount of time and try again */' + '\n' +
'' + '\n' +
'        /* Decrease the battery level and increase CO2 emitted' + '\n' +
'         * Consumption and emission values are the lowest ones' + '\n' +
'         */' + '\n' +
'        battery -= (BATTERY_CONSUMPTION[vehicleId] / VEHICLES_SPEED[vehicleId]) * (RESENDING_PERIOD - 1);' + '\n' +
'        co2Emission += (CO2_EMISSIONS[vehicleId]   / VEHICLES_SPEED[vehicleId]) * (RESENDING_PERIOD - 1);' + '\n' +
'' + '\n' +
'    		((Segment)sender).givePermisionForVehicle(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                                                  isLoaded, battery, consumedBattery, movedMaterial, co2Emission) after(RESENDING_PERIOD);' + '\n' +
'      }' + '\n' +
'      else if (POLICY == 2){ // try to overpass' + '\n' +
'        self.changeRouteWithPolicy2(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments, isLoaded,' + '\n' +
'                                        battery, consumedBattery, movedMaterial, co2Emission);' + '\n' +
'      }' + '\n' +
'      else if(POLICY == 3){ // DIJKSTRA' + '\n' +
'        // change all the route from here to final destination' + '\n' +
'        self.changeRouteWithPolicy3(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments, isLoaded,' + '\n' +
'                                          battery, consumedBattery, movedMaterial, co2Emission);' + '\n' +
'      }' + '\n' +
'      else if(POLICY == 4){' + '\n' +
'        /* 4° Policy: the vehicle follow the given path, wait and try again */' + '\n' +
'' + '\n' +
'        /* Decrease the battery level and increase CO2 emitted' + '\n' +
'         * Consumption and emission values are the lowest ones' + '\n' +
'         */' + '\n' +
'        battery -= (BATTERY_CONSUMPTION[vehicleId] / VEHICLES_SPEED[vehicleId]) * (RESENDING_PERIOD - 1);' + '\n' +
'        co2Emission += (CO2_EMISSIONS[vehicleId]   / VEHICLES_SPEED[vehicleId]) * (RESENDING_PERIOD - 1);' + '\n' +
'' + '\n' +
'    		((Segment)sender).givePermisionForVehicle(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                                                  isLoaded, battery, consumedBattery, movedMaterial, co2Emission) after(RESENDING_PERIOD);' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'    else { // Too many attempts on the same unavailable segment, reroute with DIJKSTRA' + '\n' +
'      if(currRoute[trackIndex + 1] != -1){' + '\n' +
'        self.changeRouteWithPolicy3(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments, isLoaded,' + '\n' +
'                                          battery, consumedBattery, movedMaterial, co2Emission) after(1);' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'         /* Decrease the battery level and increase CO2 emitted' + '\n' +
'         * Consumption and emission values are the lowest ones' + '\n' +
'         */' + '\n' +
'        battery -= (BATTERY_CONSUMPTION[vehicleId] / VEHICLES_SPEED[vehicleId]) * (RESENDING_PERIOD - 1);' + '\n' +
'        co2Emission += (CO2_EMISSIONS[vehicleId]   / VEHICLES_SPEED[vehicleId]) * (RESENDING_PERIOD - 1);' + '\n' +
'' + '\n' +
'        ((Segment)sender).givePermisionForVehicle(vehicleId, taskIndex, trackIndex, source, destination, currRoute, failingSegments,' + '\n' +
'                                                  isLoaded, battery, consumedBattery, movedMaterial, co2Emission) after(RESENDING_PERIOD);' + '\n' +
'      }' + '\n' +
'	  }' + '\n' +
'	}' + '\n' +
'' + '\n' +
'  /* Policy 2: the segment try to overpass the just met obstacle. Dijkstra from current position to the currRoute[trackIndex + 2]' + '\n' +
'  * e.g. currRoute = [23,24,25,26,36,46,56,-1,-1,...] obstacle found at 25, currPosition: 24' + '\n' +
'  * Dijkstra(24,26): 24,34,35,26  --> newRoute = [23,24,34,35,26,36,46,56,-1,-1,....]' + '\n' +
'  */' + '\n' +
'  msgsrv changeRouteWithPolicy2(int vehicleId, int taskIndex, int trackIndex, int source, int destination, int[' + MAX_TRACK_LENGTH + '] currRoute, int[' + MAX_TRACK_LENGTH + ']  failingSegments, boolean isLoaded,' + '\n' +
'                                    double battery, double consumedBattery, int movedMaterial, double co2Emission){' + '\n' +
'' + '\n' +
'    int startVertex = coord[0] * NUM_OF_COLUMNS + coord[1];' + '\n' +
'    int destVertex = currRoute[trackIndex + 1];' + '\n' +
'' + '\n' +
'    /* Modify the mapAvailability with the current obstacle */' + '\n' +
'    boolean[' + NUM_OF_SEGMENTS + '] mapAvailability;' + '\n' +
'' + '\n' +
'    for (int i = 0; i <NUM_OF_SEGMENTS; i++){' + '\n' +
'      if(i != currRoute[trackIndex] && !isTheSegmentInTheList(i, failingSegments)){' + '\n' +
'        mapAvailability[i] = MAP_AVAILABILITY[((int)i / NUM_OF_COLUMNS)][i % NUM_OF_COLUMNS];' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        mapAvailability[i] = false;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* 2° Policy: try to overpass the segment that is not free (obstacle, busy, ...) */' + '\n' +
'    /* Get the new next position with A* Algorithm and update the current route: from currPosition to nextPosition + 2 */' + '\n' +
'    /*************************************************************/' + '\n' +
'    int[' + NUM_OF_SEGMENTS + '][' + NUM_OF_SEGMENTS + '] adjacencyMatrix;' + '\n' +
'    for (int i = 0; i < NUM_OF_SEGMENTS; i++){' + '\n' +
'      for (int j = 0; j < NUM_OF_SEGMENTS; j++){' + '\n' +
'        adjacencyMatrix[i][j] = 0;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    for (int h = 0; h < NUM_OF_ROWS; h++){' + '\n' +
'      for (int t = 0; t < NUM_OF_COLUMNS; t++){' + '\n' +
'        for (int k = 0; k < NUM_OF_ROWS; k++){' + '\n' +
'          for (int z = 0; z < NUM_OF_COLUMNS; z++) {' + '\n' +
'            int i = (h * NUM_OF_COLUMNS) + t;' + '\n' +
'            int j = (k * NUM_OF_COLUMNS) + z;' + '\n' +
'            if( ( (abs(h - k) <= 1) &&  (abs(t - z) <= 1)) && ((abs(h - k) + abs(t - z) != 0)) ){' + '\n' +
'              if (mapAvailability[i] && mapAvailability[j] && ADJACENCY_MATRIX[i][j]){' + '\n' +
'                adjacencyMatrix[i][j] = 1;' + '\n' +
'              }' + '\n' +
'              else{' + '\n' +
'                adjacencyMatrix[i][j] = 99999;' + '\n' +
'              }' + '\n' +
'            }' + '\n' +
'          }' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* shortestDistances[i] will hold the shortest distance from src to i */' + '\n' +
'    int[' + NUM_OF_SEGMENTS + '] shortestDistances;' + '\n' +
'' + '\n' +
'    /* added[i] will true if vertex i is included in shortest path tree or shortest distance from src to i is finalized */' + '\n' +
'    boolean[' + NUM_OF_SEGMENTS + '] added;' + '\n' +
'    /* Initialize added var */' + '\n' +
'    for(int seg = 0; seg < NUM_OF_SEGMENTS; seg++){' + '\n' +
'      added[seg] = false;' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    for (int row = 0; row < NUM_OF_ROWS; row++){' + '\n' +
'      for (int column = 0; column < NUM_OF_COLUMNS; column++){' + '\n' +
'        int vertexIndex =  row * NUM_OF_COLUMNS + column;' + '\n' +
'        shortestDistances[vertexIndex] = 999999;' + '\n' +
'        added[vertexIndex] = false;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* Distance of source vertex from itself is always 0 */' + '\n' +
'    shortestDistances[startVertex] = 0;' + '\n' +
'' + '\n' +
'    /* Parent array to store shortest path tree */' + '\n' +
'    int[' + NUM_OF_SEGMENTS + '] parents;' + '\n' +
'    /* Initialize parents var */' + '\n' +
'    for(int seg = 0; seg < NUM_OF_SEGMENTS; seg++){' + '\n' +
'      parents[seg] = 0;' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* The starting vertex does not have a parent */' + '\n' +
'    parents[startVertex] = -1;' + '\n' +
'' + '\n' +
'    /* Find shortest path for all vertices */' + '\n' +
'    for (int k = 1; k < NUM_OF_SEGMENTS; k++){' + '\n' +
'' + '\n' +
'      /* Pick the minimum distance vertex from the set of vertices not yet processed. nearestVertex is always equal to startNode in first iteration. */' + '\n' +
'      int nearestVertex = -1;' + '\n' +
'      int shortestDistance = 999999;' + '\n' +
'      for (int vertexIndex = 0; vertexIndex < NUM_OF_SEGMENTS; vertexIndex++){' + '\n' +
'        if (!added[vertexIndex] && shortestDistances[vertexIndex] < shortestDistance){' + '\n' +
'          nearestVertex = vertexIndex;' + '\n' +
'          shortestDistance = shortestDistances[vertexIndex];' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'' + '\n' +
'      /* Mark the picked vertex as processed if there is a link */' + '\n' +
'      if (nearestVertex != -1){' + '\n' +
'        added[nearestVertex] = true;' + '\n' +
'' + '\n' +
'        /* Update dist value of the adjacent vertices of the picked vertex.*/' + '\n' +
'        for (int vertexIndex = 0; vertexIndex < NUM_OF_SEGMENTS; vertexIndex++){' + '\n' +
'          int edgeDistance = adjacencyMatrix[nearestVertex][vertexIndex];' + '\n' +
'' + '\n' +
'          if (edgeDistance > 0 && ((shortestDistance + edgeDistance) < shortestDistances[vertexIndex])){' + '\n' +
'            parents[vertexIndex] = nearestVertex;' + '\n' +
'            shortestDistances[vertexIndex] = shortestDistance + edgeDistance;' + '\n' +
'          }' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        parents[k] = -1;' + '\n' +
'      }' + '\n' +
'      /*if (k == destVertex){' + '\n' +
'        break;' + '\n' +
'      }*/' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    int[' + MAX_TRACK_LENGTH + '] newSubRoute;' + '\n' +
'    /* Inizialize newSubRoute var */' + '\n' +
'    for (int nSR = 0; nSR < MAX_TRACK_LENGTH; nSR++){' + '\n' +
'      newSubRoute[nSR] = -1;' + '\n' +
'    }' + '\n' +
'    newSubRoute[0] = startVertex;' + '\n' +
'    newSubRoute[shortestDistances[destVertex]] = destVertex;' + '\n' +
'' + '\n' +
'    int nextVertex = destVertex;' + '\n' +
'' + '\n' +
'    for(int nSR = shortestDistances[destVertex] - 1; nSR >=0; nSR--){' + '\n' +
'      if(parents[nextVertex] == -1){' + '\n' +
'        nextVertex = -1;' + '\n' +
'        break;' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        if(parents[nextVertex] != startVertex){' + '\n' +
'          nextVertex = parents[nextVertex];' + '\n' +
'          newSubRoute[nSR] = nextVertex;' + '\n' +
'        }' + '\n' +
'        else{' + '\n' +
'          break;' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    nextVertex = destVertex;' + '\n' +
'' + '\n' +
'    for(int parIndex = 0; parIndex < NUM_OF_SEGMENTS; parIndex++){' + '\n' +
'      if(parents[nextVertex] == -1){' + '\n' +
'        nextVertex = -1;' + '\n' +
'        break;' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        if(parents[nextVertex] != startVertex){' + '\n' +
'          nextVertex = parents[nextVertex];' + '\n' +
'        }' + '\n' +
'        else{' + '\n' +
'          break;' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    int[' + MAX_TRACK_LENGTH + '] newRoute;' + '\n' +
'    /* Copy the old route within the new route */' + '\n' +
'    for(int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'      newRoute[i] = currRoute[i];' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* Put the new sub-route within the old one */' + '\n' +
'    for(int i = 0; i < shortestDistances[destVertex]; i++){' + '\n' +
'      newRoute[trackIndex + i] = newSubRoute[i + 1];' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    for(int i = trackIndex + shortestDistances[destVertex]; i < MAX_TRACK_LENGTH  - shortestDistances[destVertex]; i++){' + '\n' +
'      newRoute[i] = currRoute[i - shortestDistances[destVertex] + 2];' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* Refine the new route in case of double visit to the same segment */' + '\n' +
'    for (int i = trackIndex; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'      for (int j = i + 1; j < MAX_TRACK_LENGTH; j++){' + '\n' +
'        if (newRoute[i] == newRoute[j]){' + '\n' +
'          /* Move the sub route backward */' + '\n' +
'          for(int z = i + 1; z < MAX_TRACK_LENGTH - (j - i); z++){' + '\n' +
'            newRoute[z] = newRoute[z + (j - i)];' + '\n' +
'          }' + '\n' +
'          break;' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    int nextX = ( (int) nextVertex / NUM_OF_COLUMNS );' + '\n' +
'    int nextY = nextVertex % NUM_OF_COLUMNS;' + '\n' +
'    assertion(nextX != -1 && nextY != -1, "Segment not valid, wrong nextX and nextY");' + '\n' +
'    int nextMovement = getNextCardinalMovement(coord, nextX, nextY);' + '\n' +
'' + '\n' +
'    ((Segment)segments[nextMovement]).givePermisionForVehicle(vehicleId, taskIndex, trackIndex, source, destination, newRoute, failingSegments,' + '\n' +
'                                              isLoaded, battery, consumedBattery, movedMaterial, co2Emission) after(1);' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  /* Policy 3: the segment try to re-route the enitre path. Dijkstra from current position to the destination' + '\n' +
'  * e.g. currRoute = [23,24,25,26,36,46,56,-1,-1,...] obstacle found at 25, currPosition: 24' + '\n' +
'  * Dijkstra(24,56): 24,34,35,36,46,56  --> newRoute = [23,24,34,35,36,46,56,-1,-1,....]' + '\n' +
'  */' + '\n' +
'  msgsrv changeRouteWithPolicy3(int vehicleId, int taskIndex, int trackIndex, int source, int destination, int[' + MAX_TRACK_LENGTH + '] currRoute, int[' + MAX_TRACK_LENGTH + ']  failingSegments, boolean isLoaded,' + '\n' +
'                                    double battery, double consumedBattery, int movedMaterial, double co2Emission){' + '\n' +
'    /* 3° Policy: change all the route from the current segment to the final destination */' + '\n' +
'' + '\n' +
'    int startVertex = coord[0] * NUM_OF_COLUMNS + coord[1];' + '\n' +
'    int destVertex = (IoPs_LOCATION[destination][0] * NUM_OF_COLUMNS) + IoPs_LOCATION[destination][1];' + '\n' +
'    /*************************************************************/' + '\n' +
'    /* Modify the mapAvailability with the current obstacle */' + '\n' +
'    boolean[' + NUM_OF_SEGMENTS + '] mapAvailability;' + '\n' +
'' + '\n' +
'    for (int i = 0; i <NUM_OF_SEGMENTS; i++){' + '\n' +
'      if(i != currRoute[trackIndex] && !isTheSegmentInTheList(i, failingSegments)){' + '\n' +
'        mapAvailability[i] = MAP_AVAILABILITY[((int)i / NUM_OF_COLUMNS)][i % NUM_OF_COLUMNS];' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        mapAvailability[i] = false;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    int[' + NUM_OF_SEGMENTS + '][' + NUM_OF_SEGMENTS + '] adjacencyMatrix;' + '\n' +
'    for (int i = 0; i < NUM_OF_SEGMENTS; i++){' + '\n' +
'      for (int j = 0; j < NUM_OF_SEGMENTS; j++){' + '\n' +
'        adjacencyMatrix[i][j] = 0;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    for (int h = 0; h < NUM_OF_ROWS; h++){' + '\n' +
'      for (int t = 0; t < NUM_OF_COLUMNS; t++){' + '\n' +
'        for (int k = 0; k < NUM_OF_ROWS; k++){' + '\n' +
'          for (int z = 0; z < NUM_OF_COLUMNS; z++) {' + '\n' +
'            int i = (h * NUM_OF_COLUMNS) + t;' + '\n' +
'            int j = (k * NUM_OF_COLUMNS) + z;' + '\n' +
'            if( ( (abs(h - k) <= 1) &&  (abs(t - z) <= 1)) && ((abs(h - k) + abs(t - z) != 0)) ){' + '\n' +
'              if (mapAvailability[i] && mapAvailability[j] && ADJACENCY_MATRIX[i][j]){' + '\n' +
'                adjacencyMatrix[i][j] = 1;' + '\n' +
'              }' + '\n' +
'              else{' + '\n' +
'                adjacencyMatrix[i][j] = 99999;' + '\n' +
'              }' + '\n' +
'            }' + '\n' +
'          }' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* shortestDistances[i] will hold the shortest distance from src to i */' + '\n' +
'    int[' + NUM_OF_SEGMENTS + '] shortestDistances;' + '\n' +
'' + '\n' +
'    /* added[i] will true if vertex i is included in shortest path tree or shortest distance from src to i is finalized */' + '\n' +
'    boolean[' + NUM_OF_SEGMENTS + '] added;' + '\n' +
'    /* Initialize added var */' + '\n' +
'    for(int seg = 0; seg < NUM_OF_SEGMENTS; seg++){' + '\n' +
'      added[seg] = false;' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    for (int row = 0; row < NUM_OF_ROWS; row++){' + '\n' +
'      for (int column = 0; column < NUM_OF_COLUMNS; column++){' + '\n' +
'        int vertexIndex =  row * NUM_OF_COLUMNS + column;' + '\n' +
'        shortestDistances[vertexIndex] = 999999;' + '\n' +
'        added[vertexIndex] = false;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* Distance of source vertex from itself is always 0 */' + '\n' +
'    shortestDistances[startVertex] = 0;' + '\n' +
'' + '\n' +
'    /* Parent array to store shortest path tree */' + '\n' +
'    int[' + NUM_OF_SEGMENTS + '] parents;' + '\n' +
'    /* Initialize parents var */' + '\n' +
'    for(int seg = 0; seg < NUM_OF_SEGMENTS; seg++){' + '\n' +
'      parents[seg] = 0;' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* The starting vertex does not have a parent */' + '\n' +
'    parents[startVertex] = -1;' + '\n' +
'' + '\n' +
'    /* Find shortest path for all vertices */' + '\n' +
'    for (int k = 1; k < NUM_OF_SEGMENTS; k++){' + '\n' +
'' + '\n' +
'      /* Pick the minimum distance vertex from the set of vertices not yet processed. nearestVertex is always equal to startNode in first iteration. */' + '\n' +
'      int nearestVertex = -1;' + '\n' +
'      int shortestDistance = 999999;' + '\n' +
'      for (int vertexIndex = 0; vertexIndex < NUM_OF_SEGMENTS; vertexIndex++){' + '\n' +
'        if (!added[vertexIndex] && shortestDistances[vertexIndex] < shortestDistance){' + '\n' +
'          nearestVertex = vertexIndex;' + '\n' +
'          shortestDistance = shortestDistances[vertexIndex];' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'' + '\n' +
'      /* Mark the picked vertex as processed if there is a link */' + '\n' +
'      if (nearestVertex != -1){' + '\n' +
'        added[nearestVertex] = true;' + '\n' +
'' + '\n' +
'        /* Update dist value of the adjacent vertices of the picked vertex.*/' + '\n' +
'        for (int vertexIndex = 0; vertexIndex < NUM_OF_SEGMENTS; vertexIndex++){' + '\n' +
'          int edgeDistance = adjacencyMatrix[nearestVertex][vertexIndex];' + '\n' +
'' + '\n' +
'          if (edgeDistance > 0 && ((shortestDistance + edgeDistance) < shortestDistances[vertexIndex])){' + '\n' +
'            parents[vertexIndex] = nearestVertex;' + '\n' +
'            shortestDistances[vertexIndex] = shortestDistance + edgeDistance;' + '\n' +
'          }' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        parents[k] = -1;' + '\n' +
'      }' + '\n' +
'      /*if (k == destVertex){' + '\n' +
'        break;' + '\n' +
'      }*/' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    int[' + MAX_TRACK_LENGTH + '] newSubRoute;' + '\n' +
'    /* Inizialize newSubRoute var */' + '\n' +
'    for (int nSR = 0; nSR < MAX_TRACK_LENGTH; nSR++){' + '\n' +
'      newSubRoute[nSR] = -1;' + '\n' +
'    }' + '\n' +
'    newSubRoute[0] = startVertex;' + '\n' +
'    newSubRoute[shortestDistances[destVertex]] = destVertex;' + '\n' +
'' + '\n' +
'    int nextVertex = destVertex;' + '\n' +
'' + '\n' +
'    for(int nSR = shortestDistances[destVertex] - 1; nSR >=0; nSR--){' + '\n' +
'      if(parents[nextVertex] == -1){' + '\n' +
'        nextVertex = -1;' + '\n' +
'        break;' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        if(parents[nextVertex] != startVertex){' + '\n' +
'          nextVertex = parents[nextVertex];' + '\n' +
'          newSubRoute[nSR] = nextVertex;' + '\n' +
'        }' + '\n' +
'        else{' + '\n' +
'          break;' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    nextVertex = destVertex;' + '\n' +
'' + '\n' +
'    for(int parIndex = 0; parIndex < NUM_OF_SEGMENTS; parIndex++){' + '\n' +
'      if(parents[nextVertex] == -1){' + '\n' +
'        nextVertex = -1;' + '\n' +
'        break;' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        if(parents[nextVertex] != startVertex){' + '\n' +
'          nextVertex = parents[nextVertex];' + '\n' +
'        }' + '\n' +
'        else{' + '\n' +
'          break;' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    int[' + MAX_TRACK_LENGTH + '] newRoute;' + '\n' +
'    /* Copy the old route within the new route */' + '\n' +
'    for(int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'    		if(i < trackIndex) {' + '\n' +
'    		      newRoute[i] = currRoute[i];' + '\n' +
'    		}' + '\n' +
'    		else {' + '\n' +
'    			newRoute[i] = -1;' + '\n' +
'    		}' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* Put the new sub-route within the old one */' + '\n' +
'    for(int i = 0; i < shortestDistances[destVertex]; i++){' + '\n' +
'      newRoute[trackIndex + i] = newSubRoute[i + 1];' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    /* Refine the new route in case of double visit to the same segment */' + '\n' +
'    for (int i = trackIndex; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'      for (int j = i + 1; j < MAX_TRACK_LENGTH; j++){' + '\n' +
'        if (newRoute[i] == newRoute[j]){' + '\n' +
'          /* Move the sub route backward */' + '\n' +
'          for(int z = i + 1; z < MAX_TRACK_LENGTH - (j - i); z++){' + '\n' +
'            newRoute[z] = newRoute[z + (j - i)];' + '\n' +
'          }' + '\n' +
'          break;' + '\n' +
'        }' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'' + '\n' +
'    int nextX = ( (int) nextVertex / NUM_OF_COLUMNS );' + '\n' +
'    int nextY = nextVertex % NUM_OF_COLUMNS;' + '\n' +
'    assertion(nextX != -1 && nextY != -1, "Segment not valid, wrong nextX and nextY");' + '\n' +
'    int nextMovement = getNextCardinalMovement(coord, nextX, nextY);' + '\n' +
'' + '\n' +
'    ((Segment)segments[nextMovement]).givePermisionForVehicle(vehicleId, taskIndex, trackIndex, source, destination, newRoute, failingSegments,' + '\n' +
'                                              isLoaded, battery, consumedBattery, movedMaterial, co2Emission) after(1);' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  /* Re-route using Dipole flow field algorithm */' + '\n' +
'  msgsrv changeRouteWithPolicy4(){}' + '\n' +
'' + '\n' +
'  /* METHODS FOR REBEC */' + '\n' +
'  int abs(int a){' + '\n' +
'    if(a >= 0){' + '\n' +
'      return a;' + '\n' +
'    }' + '\n' +
'    else {' + '\n' +
'      return (a * -1);' + '\n' +
'    }' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  /* Extract the next cardinal movement' + '\n' +
'  [0] = N; // NORTH' + '\n' +
'  [1] = NE;// NORTH-EAST' + '\n' +
'  [2] = E; // EAST' + '\n' +
'  [3] = ES;// EAST-SOUTH' + '\n' +
'  [4] = S; // SOUTH' + '\n' +
'  [5] = SW;// SOUTH-WEST' + '\n' +
'  [6] = W; // WEST' + '\n' +
'  [7] = WN;// WEST-NORTH' + '\n' +
'  */' + '\n' +
'  int  getNextCardinalMovement(int[2] location, int nX, int nY){' + '\n' +
'    if(nX == (location[0]-1) && nY == location[1]){ // NORTH' + '\n' +
'      return 0;}' + '\n' +
'    else if(nX == (location[0]-1) && nY == (location[1]+1)){ // NORTH-EAST' + '\n' +
'      return 1;}' + '\n' +
'    else if(nX == location[0] && nY == (location[1]+1)){ // EAST' + '\n' +
'      return 2;}' + '\n' +
'    else if(nX == (location[0]+1) && nY == (location[1]+1)){ // EAST-SOUTH' + '\n' +
'      return 3;}' + '\n' +
'    else if(nX == (location[0]+1) && nY == location[1]){ // SOUTH' + '\n' +
'      return 4;}' + '\n' +
'    else if(nX == (location[0]+1) && nY == (location[1]-1)){ // SOUTH-WEST' + '\n' +
'      return 5;}' + '\n' +
'    else if(nX == location[0] && nY == (location[1]-1)){ // WEST' + '\n' +
'      return 6;}' + '\n' +
'    else if(nX == (location[0]-1) && nY == (location[1]-1)){ // WEST-NORTH' + '\n' +
'      return 7;}' + '\n' +
'    else{' + '\n' +
'      assertion(false, "Next segment is not valid!");}' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  boolean isTheSegmentInTheList(int segmentId, int[' + MAX_TRACK_LENGTH + '] listOfSegments){' + '\n' +
'    for (int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'      if(listOfSegments[i] == segmentId){' + '\n' +
'        return true;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'    return false;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  int getLength(int[' + MAX_TRACK_LENGTH + '] listOfSegments){' + '\n' +
'    for (int i = 0; i < MAX_TRACK_LENGTH; i++){' + '\n' +
'      if(listOfSegments[i] == -1){' + '\n' +
'        return i;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'    return MAX_TRACK_LENGTH;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  boolean isTheSegmentAParkingStation(int[2] location){' + '\n' +
'    for (int i = 0; i < NUM_OF_PARKING_STATIONS; i++)' + '\n' +
'      if(PARKING_STATION_POSITIONS[i][0] == location[0] && PARKING_STATION_POSITIONS[i][1] == location[1])' + '\n' +
'        return true;' + '\n' +
'' + '\n' +
'    return false;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  boolean isTheSegmentAChargingStation(int[2] location){' + '\n' +
'    for (int i = 0; i < NUM_OF_CHARGING_STATIONS; i++)' + '\n' +
'      if(CHARGING_STATION_POSITIONS[i][0] == location[0] && CHARGING_STATION_POSITIONS[i][1] == location[1])' + '\n' +
'        return true;' + '\n' +
'' + '\n' +
'    return false;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  boolean isTheSegmentALoadUnloadLocation(int[2] location){' + '\n' +
'    for (int i = 0; i < NUM_OF_LOAD_UNLOAD_STATIONS; i++)' + '\n' +
'      if(LOAD_UNLOAD_POSITIONS[i][0] == location[0] && LOAD_UNLOAD_POSITIONS[i][1] == location[1])' + '\n' +
'        return true;' + '\n' +
'' + '\n' +
'    return false;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  boolean isTheTimeInAnObstacleWindow(int currTime){' + '\n' +
'    for (int i = 0; i < OBSTACLE_OCCURRENCES; i++)' + '\n' +
'      if(currTime >= CHANGES_TIME[i][0] && currTime <= CHANGES_TIME[i][1])' + '\n' +
'        return true;' + '\n' +
'    return false;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  int getObstacleWindow(int currTime){' + '\n' +
'    for (int i = 0; i < OBSTACLE_OCCURRENCES; i++)' + '\n' +
'      if(currTime >= CHANGES_TIME[i][0] && currTime <= CHANGES_TIME[i][1])' + '\n' +
'        return i;' + '\n' +
'    return -1;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  boolean isTheSegmentInTheObstacleList(int segmentId, int obstacleWindow){' + '\n' +
'    for(int i = 0; i < OBSTACLE_NUMBER; i++)' + '\n' +
'      if(CHANGES_ENV[obstacleWindow][i] == segmentId)' + '\n' +
'        return true;' + '\n' +
'    return false;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'  boolean isTheSegmentAvailableNow(int segmentId, int currTime){' + '\n' +
'    boolean isObstacleTime = isTheTimeInAnObstacleWindow(currTime);' + '\n' +
'    if(isObstacleTime){' + '\n' +
'      boolean isSegmentAvailable = isTheSegmentInTheObstacleList(segmentId, getObstacleWindow(currTime));' + '\n' +
'      if(isSegmentAvailable){' + '\n' +
'        return false;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'    return true;' + '\n' +
'  }                    ' + '\n' +
'' + '\n' +
'  int getFailingAttemptsNumber(int[' + MAX_TRACK_LENGTH + '] listOfSegments, int segment){' + '\n' +
'    int attempts = 0;' + '\n' +
'    int index = getLength(listOfSegments) - 1;' + '\n' +
'    for (int i = index; i >= 0; i--){' + '\n' +
'      if(listOfSegments[i] == segment){' + '\n' +
'        attempts++;' + '\n' +
'      }' + '\n' +
'      else{' + '\n' +
'        break;' + '\n' +
'      }' + '\n' +
'    }' + '\n' +
'    return attempts;' + '\n' +
'  }' + '\n' +
'' + '\n' +
'	/* END METHODS */' + '\n' +
'' + '\n' +
'}' + '\n' +
'' + '\n' +
'/*********************************************************/' + '\n' +
'main{' + '\n' + MAIN + '\n' +
'}' + '\n')


# In[93]:


# Create the model specification into TRebeca file
def createModelFile(fileName, model):
    rebecaModelFile = open((fileName + '.rebeca'), 'w')
    rebecaModelFile.write(model)
    print('Model Created!')
    rebecaModelFile.close()


# In[94]:


createModelFile(modelFileName, modelString)


# In[ ]:




