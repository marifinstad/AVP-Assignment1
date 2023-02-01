import random
import numpy as np

#### DETTE ER CONATINERE #####
def NewContainer(id, length, cargo):
    #cargo er mengen av materialet den har med
    #listen med containere blir  [id, length, wighth, cargo]
    if cargo < 0 or cargo > 23: 
        return print("cannot load container due to over/under weight")
    if length == 20: 
        return [id, 20, 2, cargo]
    elif length == 40: 
        return [id, 40, 4, cargo]
    else: 
        return ("could not obtain container")

#Conatiner er nå en liste med info om en container
#få tak i ID nummeret til en container
def getIdContainer(container):
    return container[0]
#få tak i LENGEN til en container
def getLengthContainer(container):
    return container[1]
#få tak i VEKTEN til en container
def getWeigtContainer(container):
    return container[2]
#få tak i LASTEN til en container
def getCargoContainer(container):
    return container[3]
#få tak i TOTALVEKT til container:
def getTotalWeightContainer(container):
    return getWeigtContainer(container) + getCargoContainer(container)

#sette ID
def setIdContainer(container, id):
    container[0] = id
#sette lengde
def setLengthContainer(container, length):
    container[1] = length
    #sette vekt
def setWeigthContainer(container, weight):
    container[2] = weight
#sette cargo
def setCargoContainer(container, cargo):
    container[3] = cargo


containers = []

def addContainer(container):
    containers.append(container)

def removeContainer(container):
    if len(containers) != 0:
        containers.remove(container)
    else:
        return "No containers available"

def findContainer(container):
    if container in containers:
        return True
    else:
        return False

def checkID(id):
    for i in containers:
        if i[0] == id:
            return True
    else: 
        return False

def randomContainers(conatiners):
    for i in range (0,20):
        container = [0,0,0,0]
        id = random.randint(0,10000)
        if checkID(id) == False:
            setIdContainer(container, id)
            cargo = random.randint(0,23)
            setCargoContainer(container,cargo)
            weight = random.randrange(2,5,2)
            setWeigthContainer(container,weight)
            if weight == 2:
                length = 20
            else:
                length = 40
            setLengthContainer(container,length)
        addContainer(container)
    return containers


#Lage det om til filformat
def fileFormatContainer(container):
    # id,lengde,egenvekt,loadvekt,totalvekt
    return str(container[0])+","+str(container[1])+","+str(container[2])+","+container[3]+","+str(getTotalWeightContainer(container))



### DETT ER SHIPS #####

