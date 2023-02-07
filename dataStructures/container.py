import random


#### DETTE ER CONATINERE #####
def NewContainer(id, length, cargo): #skal man ta inn en weight her også?
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
    #return container[2] + container[3]
    container[4] = getWeigtContainer(container) + getCargoContainer(container)
    return container[4]

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
    
# def getContainerTotalWeight(container):
#     return getWeigtContainer(container) + getCargoContainer(container)


def randomContainers(containers):
    for i in range (0,5):
        container = [0,0,0,0,0]
        id = random.randint(0,10000000)
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
            getTotalWeightContainer(container)
        addContainer(container)
    return containers

### PRINT CONTAINERS ###

# #Lage det om til filformat
def fileFormatContainer(container):
     # id,lengde,egenvekt,loadvekt,totalvekt
    return str(container[0])+" "+str(container[1])+" "+str(container[2])+" "+str(container[3])+" "+str(getTotalWeightContainer(container))

#skrive til fil
def writeContainersToFile(containers):
    try:
        with open("dataStructures/load.csv", "w") as fp:
            for container in containers:
                formatedContainer = fileFormatContainer(container)
                fp.write("%s\n" % formatedContainer)
            fp.close()
    except:
        print("Could not write to file")

def readContainersFromFile(containers):
#     with open("dataStructures/load.cvs", "r") as fp:
#         for container in 
    try:
        # fil = open("dataStructures/load.csv", "r") ### NOE SKURRER
        # fil.close()
        with open("dataStructures/load.csv", "r") as fp:
            container = fp.read()
            list = [container.splitlines()]
            for line in range(0, len(list)-1):
                containers.append(line) 
            fp.close()
    except:
        print("Could not read file")


### DETT ER SHIPS #####

def NewShip(length, width, height):
    return [length, width, height, containers]

#gettere
def getLengthShip(ship):
    return ship[0]

def getWidthShip(ship):
    return ship[1]

def getHeightShip(ship):
    return ship[2]

def getShipContainers(ship):
    return ship[3]

#settere
def setLengthShip(ship, length):
    ship[0] = length

def setWidthShip(ship, width):
    ship[1] = width

def setHeightShip(ship, height):
    ship[2] = height

def numberOfContainersShips(ship):
    return len(getShipContainers(ship))

def getRandomContainer(ship, i):
    return containers[i]

def insertContainerOnShip(ship, container, i):
    containers.insert(i, container)

def appendContainerOnShip(ship, container):
    containers.append(container)

def loadContainerOnShip(ship, newContainer):
    newContainerWeight = getTotalWeightContainer(newContainer)
    loaded = False
    i = 0
    while i < numberOfContainersShips(ship):
        container = getRandomContainer(ship, i)
        containerWeight = getTotalWeightContainer(container)
        if containerWeight <= newContainerWeight:
            insertContainerOnShip(ship, newContainer, i)
            loaded = True
            break
        i = i + 1
    if not loaded:
        appendContainerOnShip(ship, newContainer)

def appendContainerOnShip(ship, container):
    containers.append(container)

def removeContainerFromShip(ship):
    if numberOfContainersShips() != 0:
        containers.pop()
    return containers

def getLastContainerOnShip(ship):
    if numberOfContainersShips != 0:
        return containers[-1]
    return None

def sortContainersWeight(containers):
    containers.sort(key = lambda x: x[4])
    return containers

#pile 
# while containersOnland =! 0 
#  [floor[row[kolonne]]]
# for floor in range (0,17):
#    for row in range (0,21):
#        for kolonne in range (0,22):
#             if getLength(container) == 4:
#             if kolonne == 21:
#                  sjekke neste container 
#            
#             kolonne += 2





### PRINT SHIPS ###

# def fileFormatShip(ship):
#      # id,lengde,egenvekt,loadvekt,totalvekt
#     containerWeight = getTotalWeightContainer(ship[3])
#     return containerWeight

# def writeShipsToFile(ship):
#     try:
#         with open("dataStructures/loadShip.tsv", "w") as fp:
#             for container in ship:
#                 formatedShip = fileFormatShip(container)
#                 fp.write("%s\n" % formatedShip)

#         fp.close()
#     except:
#         print("Could not write to file")

# ship = NewShip(23, 22, 18)
# writeShipsToFile(ship)


#Dette er en test 

#ship = NewShip(23, 22, 18)
# c1 = NewContainer(1000, 20, 5)
# c2 = NewContainer(1010, 40, 9)
# c3 = NewContainer(1100, 20, 10)
# c4 = NewContainer(1001, 40, 20)

# loadContainerOnShip(ship, c1)
# loadContainerOnShip(ship, c2)
# loadContainerOnShip(ship, c3)
# loadContainerOnShip(ship, c4)

#print("------")
#print(ship)

randomContainers(containers)
sortContainersWeight(containers)
for el in containers:
     print(fileFormatContainer(el))
writeContainersToFile(containers)
print("----")
readContainersFromFile(containers)
print(containers)

