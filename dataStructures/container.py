import random
import csv

#TASK 1
def NewContainer(id, length, cargo): 
    #Cargo is the amount of material
    #The list with containers will be [id, length, width, cargo]
    if cargo < 0 or cargo > 23:
        return print("cannot load container due to over/under weight")
    if length == 20:
        return [id, 20, 2, cargo]
    elif length == 40:
        return [id, 40, 4, cargo]
    else:
        return ("could not obtain container")

#Container is now a list with info about a container
#Gets the ID number to a container
def getIdContainer(container):
    return container[0]
#Gets the length to a container
def getLengthContainer(container):
    return container[1]
#Gets the weight to a container
def getWeigtContainer(container):
    return container[2]
#gets all the cargo from the ship 
def getCargoContainer(container):
    return container[3]
#Gets the total weight to a container:
def getTotalWeightContainer(container):
    container[4] = getWeigtContainer(container) + getCargoContainer(container)
    return container[4]

#set the id for a container
def setIdContainer(container, id):
    container[0] = id
#set length of container
def setLengthContainer(container, length):
    container[1] = length
    #set weight for container
def setWeigthContainer(container, weight):
    container[2] = weight
#set cargo for container
def setCargoContainer(container, cargo):
    container[3] = cargo

#END OF TASK 1  
#TEST 1
# c1 = [0,0,0,0,0]
# c2 = [0,0,0,0,0]
# c3 = NewContainer(0000,40,20)
# setIdContainer(c1,1)
# setIdContainer(c2,2)
# setLengthContainer(c2,40)
# setLengthContainer(c1,40)
# setCargoContainer(c1,4)
# setCargoContainer(c2,10)
# task1 = [c1,c2]
# for q in task1:
#     setWeigthContainer(q,4)
#     getIdContainer(q)
#     getCargoContainer(q)
#     getWeigtContainer(q)
#     getLengthContainer(q)
#     getTotalWeightContainer(q)
# print(task1,c3)


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
# containertest2= NewContainer(1234,40,2)
# print(containers)
# if checkID(containertest2[0]) == False: 
#     addContainer(containertest2)
#     print(containers)
#     if findContainer(containertest2) == True:
#         removeContainer(containertest2)
#         print(containers)

#TASK 3
def randomContainers(containers):
    for i in range (0,50):
        id = i 
         #This gives us an increasing index
        container = [0,0,0,0,0]
        #id = random.randint(0,100000)
        if checkID(id) == False:
            setIdContainer(container, id)
            cargo = random.randint(0,23)
            setCargoContainer(container,cargo)
#The code below generates a 20ft or 40ft container. We assume that we only get 40ft containers for the rest of the code
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
# randomContainers(containers)
# print(containers)

#TASK 4
#Lage det om til filformat
def fileFormatContainer(container):
     # id, length, unloaded weight, loadedweight ,total weight
    return str(container[0])+","+str(container[1])+","+str(container[2])+","+str(container[3])+","+str(getTotalWeightContainer(container))

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
            empty = []
            container = csv.reader(fp)
            for row in container: 
                list = [eval(i) for i in row]
                empty.append(list)
            for el in empty:
                containers.append(el)
            fp.close()
    except:
        print("Could not read file")

#END OF TASK 4

#TEST TASK 4

# randomContainers(containers)
# writeContainersToFile(containers)
# readContainersFromFile(containers)
# print(containers)



#TASK 5 AND 7 AND 8

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


#Helpfunctions

#inserts the conatiner into the i index in the list and the dict
def insertContainerOnShip(ship, container, i):
    ship[3].append(container)

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
        if getWeightArea(ship[5+i]) < lettest:
            lettest = getWeightArea(ship[5+i])
            areanr = 5 + i
    return areanr


#finds the lightest stack
def getLightestStack(area):
    stacknr = 0
    lightest = 1000000000000
    for i in range(len(area)):
        weight = getWeightStack(area[i])
        if weight < lightest and len(area[i]) <= 18:
            stacknr = i
            lightest = weight
    return stacknr #denne returner en indeks i som gjør at vi i et area vet at den letteste stacken er f.eks FrontLeft[i]
    #This returns an index i that will 

def loadContainerToShip(ship,container):
    #newWeight = container[4]
    lightestArea = getLightestArea(ship)
    #print(ship[lightestArea])
    lightestStack = getLightestStack(ship[lightestArea])
    #print(str(lightestArea)+ ", "+ str(lightestStack))
    #print(str(getWeightStack(ship[lightestArea][lightestStack]))+ " STACKWEIGHT \n")
    ship[lightestArea][lightestStack].append(container)
    ship[lightestArea][lightestStack].sort(key = lambda x: x[4], reverse = True) #THIS IS TASK 8
    ship[3].append(container)
    addContainerToDict(ship,container)



#finds the lighets area
def getHeaviestArea(ship):
    areanr = 0
    lettest = 0
    for i in range(6):
        if getWeightArea(ship[5+i]) > lettest:
            lettest = getWeightArea(ship[5+i])
            areanr = 5 + i
    return areanr


#finds the lightest stack
def getHeaviestStack(area):
    stacknr = 0
    lightest = 0
    for i in range(len(area)):
        weight = getWeightStack(area[i])
        if weight > lightest and len(area[i]) <= 18:
            stacknr = i
            lightest = weight
    return stacknr #denne returner en indeks i som gjør at vi i et area vet at den letteste stacken er f.eks FrontLeft[i]

def unloadContainers(ship):
    while len(ship[3]) != 0:
        heaviestArea = getHeaviestArea(ship)
        heaviestStack = getHeaviestStack(ship[heaviestArea])
        container = ship[heaviestArea][heaviestStack].pop()
        removedContainers.append(container)
        removeContainerFromDict(ship,container)
        ship[3].remove(container)

removedContainers = []

#### TEST 5
# skip5 = NewShip(24,22,18)
# randomContainers(containers)
# while True:
#     for cont in containers:
#         loadContainerToShip(skip5,cont)
#     for i in range (5):
#         print(skip5[5+i])
#     unloadContainers(skip5)
#     for i in range (5):
#             print(skip5[5+i])
#     break

# TASK 6 #

def fileFormatShip(container):
#[length, width, height, [], dict(), frontLeft, frontRight, midLeft, midRight, backLeft, backRight
    return str(container[0]) + ',' + str(container[1]) + ',' + str(container[2]) + ',' + str(container[3]) + ',' + str(container[4])  

def writeShipToFile(ship):
    try:
       with open("dataStructures/loadShip.tsv", "w") as fp:
            for container in ship[3]:
                formatedShip = fileFormatShip(container)
                fp.write("%s\n" % formatedShip)
            fp.close()
    except:
         print("Could not write to file")

def loadShipFromFile(ship):
    try:
        with open("dataStructures/loadShip.tsv", "r") as fp:
            empty = []
            container = csv.reader(fp)
            for row in container:
                list = [eval(i) for i in row]
                empty.append(list)
            container = fp.read()
            for el in empty:
                loadContainerToShip(ship,el)
            fp.close()
    except:
        print("Could not read file")

###TEST TASK 6###
# skip6 = NewShip(24,22,18)
# randomContainers(containers)
# while True:
#     for container in containers:
#         loadContainerToShip(skip6, container)
#     break
# writeShipToFile(skip6)
# loadShipFromFile(skip6)
# print(skip6)


#TASK 9
def getWeightofShip(ship):
    weight = 0
    for i in range (5):
        weight += getWeightArea(ship[5+i])
    print("The total weight of the ship is: " + str(weight))
    return weight

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
        weight = getWeightArea(ship[5+i])
        if i == 0 or i == 1: 
            part1 += weight
        if i == 2 or i == 3: 
            part2 += weight
        if i == 4 or i == 5: 
            part3 += weight
    return part1,part2,part3

def getStabilitySide(ship):
    weight1, weight2 = getWeightsOfSideShip(ship)
    percentage = abs(weight2 - weight1)/min(weight2,weight1) * 100
    if percentage <= 10:
        print("The differenece bewteen the sides are: " + str(percentage))
        return True
    else:
        print("The difference between sides are above the limit, it is "+ str(percentage))
        return False

def getStabilitySection(ship):
    part1,part2,part3 = getWeightsOfSections(ship)
    el = [part1,part2,part3]
    percentage1 = abs(el[0] - el[1])/min(el[0],el[1]) * 100
    percentage2 = abs(el[2] - el[1])/min(el[2],el[1]) * 100
    percentage3 = abs(el[0] - el[2])/min(el[0],el[2]) * 100
    percentages = [percentage1,percentage2,percentage3]
    okey = False
    for el in percentages:
        if el < 10: 
            okey = True
        else: 
            print("Stability between sides are not good")
            return False
    print("Stability between sections are good, they are: "+ str(percentages))
    return okey

def checkStability(ship):
    stabil = True
    if getStabilitySection(ship) == False:
        stabil = False
    if getStabilitySide(ship) == False:
        stabil = False
    print("Ship is stable status: "+ str(stabil))
    return stabil

     

#TEST TASK 9
# skip9 = NewShip(24,22,18)
# randomContainers(containers)
# while True:
#     for cont in containers:
#         loadContainerToShip(skip9,cont)
#     break
# print("           /\          ")
# print("          /  \         ")
# print("_______________________")
# print("|section 1:|section 2: ")
# print("|       "+ str(getWeightArea(skip9[5]))+ "|        "+str(getWeightArea(skip9[6]))+ "|")
# print("_______________________")
# print("|section 3:|section 4: ")
# print("|       "+ str(getWeightArea(skip9[7]))+ "|        "+str(getWeightArea(skip9[8]))+ "|")
# print("_______________________")
# print("|section 5:|section 6: ")
# print("|       "+ str(getWeightArea(skip9[9]))+ "|        " +str(getWeightArea(skip9[10]))+ "|")
# print("_______________________")
# for i in range (6):
#     print("Weight of section "+ str(i)+ " is : " + str(getWeightArea(skip9[5+i])))
# checkStability(skip9)

### PRINT SHIPS ###

#TASK 11
def loadTime(containers):
    return print("It takes "+str(len(containers)*4)+" minutes to load the container to the ship")
    
#TEST 11
# randomContainers(containers)
# loadTime(containers)

