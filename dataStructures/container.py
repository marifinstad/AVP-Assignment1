
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

### DETT ER SHIPS #####