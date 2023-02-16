import random

#TASK 1
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

#END OF TASK 1

#TEST 1



#TASK 2

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

#END OF TASK 2
#TEST TASK 2


#TASK 3
def randomContainers(containers):
    for i in range (0,50):
        container = [0,0,0,0,0]
        id = i
        if checkID(id) == False:
            setIdContainer(container, id)
            cargo = random.randint(0,23)
            setCargoContainer(container,cargo)
            #weight = random.randrange(2,5,2)
            #setWeigthContainer(container,weight)
            #if weight == 2:
            #    length = 20
            #else:
            #    length = 40
            length = 40
            weight = 4
            setLengthContainer(container,length)
            setWeigthContainer(container,weight)
            getTotalWeightContainer(container)
        addContainer(container)
    return containers
#END OF TASK 3

#TEST TASK 3

#print("----")
#randomContainers(containers)
#print(containers)

#TASK 4
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
    try:
        with open("dataStructures/load.csv", "r") as fp:
            container = fp.read()
            list = [container.splitlines()]
            for line in range(0, len(list)-1):
                containers.append(line)
            fp.close()
    except:
        print("Could not read file")
#END OF TASK 4

#TEST TASK 4

#writeContainersToFile(containers)
#readContainersFromFile(containers)


#TASK 5 AND 7
### DETT ER SHIPS #####

#implement of a new ship
def NewShip(length, width, height):
    frontLeft = [] #ship[5]
    frontRight = [] #ship[6]
    midLeft = [] #ship[7]
    midRight = [] #ship[8]
    backLeft = [] #ship[9]
    backRight = [] #ship[10]
    for i in range(5):
        x = []
        y = []
        z = []
        a = []
        b = []
        c = []
        frontLeft.append(x)
        frontRight.append(y)
        midLeft.append(z)
        midRight.append(a)
        backLeft.append(b)
        backRight.append(c)
    return [length, width, height, [], dict(), frontLeft, frontRight, midLeft, midRight, backLeft, backRight]

#gettere for ship
def getLengthShip(ship):
    return ship[0]

def getWidthShip(ship):
    return ship[1]

def getHeightShip(ship):
    return ship[2]

def getShipContainers(ship):
    return ship[3]

def getRandomContainer(ship, i):
    containers = getShipContainers(ship)
    return containers[i]

def getDictFromShip(ship):
    return ship[4]

def getFrontLeft(ship):
    return ship[5]

def getFrontRight(ship):
    return ship[6]

def getMidLeft(ship):
    return ship[7]

def getMidRight(ship):
    return ship[8]

def getBackLeft(ship):
    return ship[9]

def getBackRight(ship):
    return ship[10]

#settere
def setLengthShip(ship, length):
    ship[0] = length

def setWidthShip(ship, width):
    ship[1] = width

def setHeightShip(ship, height):
    ship[2] = height

def numberOfContainersShips(ship):
    return len(getShipContainers(ship))


#støttefunksjoner til dictionary

#inserts the conatiner into the i index in the list and the dict
def insertContainerOnShip(ship, container, i):
    #containers = getShipContainers(ship)
    #containers.insert(i,container)
    ship[3].append(container)
    addContainerToDict(ship,container)


def appendContainerOnShip(ship, container):
   cont = getShipContainers(ship)
   cont.append(container)
   addContainerToDict(ship,container)

def lookForContainer(ship,id):
    dict = getDictFromShip(ship)
    return dict.get(id,None)

def addContainerToDict(ship,container):
    dict = getDictFromShip(ship)
    id = getIdContainer(container)
    dict[id] = container

def removeContainerFromDict(ship,container):
    dict = getDictFromShip(ship)
    id = getIdContainer(container)
    del dict[id]

#get Weight of stack
def getWeightStack(stack):
    weight = 0
    for container in stack:
        weight += getTotalWeightContainer(container)
    return weight

#gets the weight of the area
def getWeightArea(area): #area = ship[6]
    weight = 0
    for stack in area:
        weight += getWeightStack(stack)
    return weight


#finds the lighets area
def getLightestArea(ship):
    areanr = 0
    lettest = 10000000000000000
    for i in range(6):
        #print(getWeightArea(ship[5+i]))
        if getWeightArea(ship[5+i]) < lettest:
            lettest = getWeightArea(ship[5+i])
            areanr = 5 + i
    #print(lettest)
    #print(areanr)
    return areanr


#finds the lightest stack
def getLightestStack(area):
    stacknr = 0
    lightest = 1000000000000
    for i in range(len(area)):
        weight = getWeightStack(area[i])
        #print(str(weight)+  " DETTE ER EN STACKWEIGHT")
        if weight < lightest and len(area[i]) <= 18:
            stacknr = i
            #print("this is area i")
            #print(area[i])
            lightest = weight
    #print(lightest)
    #print(stacknr) 
    return stacknr #denne returner en indeks i som gjør at vi i et area vet at den letteste stacken er f.eks FrontLeft[i]


# lightestArea = getLightestArea(ship)
# lightestStack = getLightestStack(lightestArea)
# ship[lightestArea][lightestStack].append(container)


def loadContainerToShip(ship,container):
    newWeight = container[4]
    lightestArea = getLightestArea(ship)
    #print(ship[lightestArea])
    lightestStack = getLightestStack(ship[lightestArea])
    #print(str(lightestArea)+ ", "+ str(lightestStack))
    #print(str(getWeightStack(ship[lightestArea][lightestStack]))+ " STACKWEIGHT \n")
    loaded = False
    if not loaded:
        ship[lightestArea][lightestStack].append(container)
        ship[lightestArea][lightestStack].sort(key = lambda x: x[4], reverse = True)
        ship[3].append(container)
        addContainerToDict(ship,container)

removedContainers = []
#finds the lighets area
def getHeaviestArea(ship):
    areanr = 0
    lettest = 0
    for i in range(6):
        #print(getWeightArea(ship[5+i]))
        if getWeightArea(ship[5+i]) > lettest:
            lettest = getWeightArea(ship[5+i])
            areanr = 5 + i
    #print(lettest)
    #print(areanr)
    return areanr


#finds the lightest stack
def getHeaviestStack(area):
    stacknr = 0
    lightest = 0
    for i in range(len(area)):
        weight = getWeightStack(area[i])
        #print(str(weight)+  " DETTE ER EN STACKWEIGHT")
        if weight > lightest and len(area[i]) <= 18:
            stacknr = i
            #print("this is area i")
            #print(area[i])
            lightest = weight
    #print(lightest)
    #print(stacknr) 
    return stacknr #denne returner en indeks i som gjør at vi i et area vet at den letteste stacken er f.eks FrontLeft[i]

def unloadContainers(ship):
    while len(ship[3]) != 0:
        heaviestArea = getHeaviestArea(ship)
        #print(ship[lightestArea])
        heaviestStack = getHeaviestStack(ship[heaviestArea])
        container = ship[heaviestArea][heaviestStack].pop()
        removedContainers.append(container)
        ship[3].remove(container)
#### TEST 5
skip5 = NewShip(24,22,18)
randomContainers(containers)
while True:
    for cont in containers:
        loadContainerToShip(skip5,cont)
    # # for i in range (5):
    # #         print(skip5[5+i])

    #unloadContainers(skip5)
    print("hei")
    break



# #checks if ship empty
# def isEmptyShip(ship):
#     return numberOfContainersShips(ship) == 0

#add container to list on ship
# def addContainerToShip(ship,container):
#     cont = getShipContainers(ship)
#     cont.append(container)
#     addContainerToDict(ship, container)

# #add containers list to ship
# def addContainersToShip(ship, cont):
#     while len(cont) != 0:
#         container = cont.pop()
#         addContainerToShip(ship, container)

#deletes container from list on ship
# def removeContainerFromShip(ship): #denne sletter den øverste containeren
#     if numberOfContainersShips(ship) != 0:
#         cont = getShipContainers(ship)
#         container = cont.pop()
#         removeContainerFromDict(ship,container)
#     return

#gets the container at the top of the list
# def getLastContainerOnShip(ship):
#     if numberOfContainersShips != 0:
#         return containers[-1]
#     return None

# def removeLighterContainers(ship, weight):
#     removedContainers = []
#     while not isEmptyShip(ship):
#         container = getLastContainerOnShip(ship)
#         totalWeight = getTotalWeightContainer(container)
#         if totalWeight >= weight:
#             break
#         removeContainer(ship)
#         removedContainers.append(container)
#     return removedContainers



#TASK 9
def getWeightofShip(ship):
    weight = 0
    for i in range (5):
        weight += getWeightArea(ship[5+i])
    return print("Total weight of ship is: " + str(weight))

def getWeightsOfSideShip(ship):
    weight1 = 0
    weight2 = 0
    for i in range(6):
        if (i+5)%2 != 0:
            weight1 += getWeightArea(ship[5+i])
        if (i+5)%2 == 0:
            weight2 += getWeightArea(ship[5+i])
    return weight1, weight2

def getWeightsOfSections(ship):
    part1 = 0
    part2 = 0
    part3 = 0
    for i in range(6):
        weight += getWeightArea(ship[5+i])
        if i == 0 or i == 1: 
            part1 += weight
        if i == 2 or i == 3: 
            part2 += weight
        if i == 4 or i == 5: 
            part3 += weight
    return part1,part2,part3

def getStabilitySide(ship):
    print("The total weight of the ship is: " + str(getWeightofShip(ship)))
    weight1, weight2 = getWeightsOfSideShip(ship)
    percentage = abs(weight2 - weight1)/max(weight2,weight1) * 100
    if percentage <= 5:
        return print("The differenece bewteen the sides are: " + str(percentage))
    else:
        return print("The difference between sides are above the limit, it is "+ str(percentage))

def getStabilitySection(ship):
    part1,part2,part3 = getWeightsOfSections(ship)
    percentage = abs(weight2 - weight1)/max(weight2,weight1) * 100

#TEST TASK 9
print(getWeightArea(skip5[5]))
print(getWeightArea(skip5[6]))
print(getWeightArea(skip5[7]))
print(getWeightArea(skip5[8]))
print(getWeightArea(skip5[9]))
print(getWeightArea(skip5[10]))
getWeightofShip(skip5)
getStabilitySide(skip5)
### PRINT SHIPS ###

def fileFormatShip(ship):
#      # id,lengde,egenvekt,loadvekt,totalvekt
#[length, width, height, [], dict(), frontLeft, frontRight, midLeft, midRight, backLeft, backRight]
    return str(ship[0]) + ' ' + str(ship[1]) + ' ' + str(ship[2]) + ' ' + str(ship[3]) + ' ' + str(ship[4]) + ' ' + str(ship[5]) + ' ' + str(ship[6]) + ' ' + str(ship[7]) + ' ' + str(ship[8]) + ' ' + str(ship[9])+ ' ' + str(ship[10])

def writeShipToFile(ship):
    try:
       with open("dataStructures/loadShip.tsv", "w") as fp:
            for container in ship:
                formatedShip = fileFormatShip(container)
                fp.write("%s\n" % formatedShip)
            fp.close()
    except:
         print("Could not write to file")

def readShipFromFile(ship):
    try:
        with open("dataStructures/loadShip.tsv", "r") as fp:
            ship = fp.read()
            list = [ship.splitlines()]
            for line in range(0, len(list)-1):
                ship.append(line)
            fp.close()
    except:
        print("Could not read file")

###TEST TASK 6###
skip5 = NewShip(24,22,18)
randomContainers(containers)
#print('hei')
# while True:
#     for cont in containers:
#         loadContainerToShip(skip5,cont)
#     break
print(skip5)
writeShipToFile(skip5)




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

# randomContainers(containers)
# sortContainersWeight(containers)
# for el in containers:
#      print(fileFormatContainer(el))
# writeContainersToFile(containers)
# print("----")
# readContainersFromFile(containers)
# print(containers)

