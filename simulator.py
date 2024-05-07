import random
import time

blobNames = ["Tubby", "Goob", "Blubster", "Jerry", "Fatty", "Jiggler", "Wobbly", "Gelatina", "Squishy", "Droopy", "Loopster", "Higgly",
             "Bobbly", "Bouncy", "Tiggly", "Flabbo", "Figgly", "Ziggly", "Noodler", "Hobbly", "Yooby", "Slippery", "Gordo", "Pabbly",
             "Bobo", "Dobo", "Flubby", "Jubby", "Weebly", "Zeebly", "Quibley", "Jibley", "Bibley", "Nubley", "Wubley", "Yubbzy"]

doveFamilies = ["Finklebuster", "Wigglewomper", "Squashmeister", "Goodington", "Blueguy", "Softie", "Niceface", "Gentleson", "Sharington", "Yagoobian"]
hawkFamilies = ["Hawkerson", "Talonizer", "Antagonator", "Ripner", "Clawson", "Slashner", "Fightington", "Jerkfield", "McBully", "Killinator"]

def setTextColorBlue():
    print("\033[34m", end="")

def setTextColorRed():
    print("\033[91m", end="")

def setTextColorYellow():
    print("\033[33m", end="")

def setTextColorGreen():
    print("\033[32m", end="")

def setTextColorCyan():
    print("\033[36m", end="")

def setTextColorWhite():
    print("\033[0m", end="")

def printLivingBlobs(messageString, showRewards=False):
    setTextColorGreen()
    time.sleep(TEXT_WAIT)
    print(messageString)
    setTextColorWhite()

    for blobNum in range(len(livingBlobs)):
        currBlob = livingBlobs[blobNum]
        if currBlob.getBlobType() == "D": setTextColorBlue()
        if currBlob.getBlobType() == "H": setTextColorRed()
        time.sleep(TEXT_WAIT)
        print(f"   Blob name: {currBlob.getBlobFullName()}    Blob type: {currBlob.getBlobType()}    Generation: {currBlob.getBlobGeneration()}")
        if showRewards:
            time.sleep(TEXT_WAIT)
            print(f"                    Blob reward: {livingBlobs[blobNum].getBlobReward()}")
        setTextColorWhite()


class Blob:
    def __init__(self, blobType, firstName, lastName, generation=1):
        self.blobType = blobType
        self.firstName = firstName
        self.lastName = lastName
        self.generation = generation
        self.predatorLevel = 0
        self.reward = 1

    def getBlobType(self):
        return self.blobType
    
    def getBlobFirstName(self):
        return self.firstName
    
    def getBlobLastName(self):
        return self.lastName
    
    def getBlobFullName(self):
        return self.firstName + " " + self.lastName
    
    def getBlobGeneration(self):
        return self.generation
    
    def getPredatorLevel(self):
        return self.predatorLevel
    
    def getBlobReward(self):
        return self.reward
    
    def setBlobReward(self, newReward):
        self.reward = newReward

    def predatorLevelUp(self):
        self.predatorLevel += 1

    def printPredatorLevel(self):
        blobTypeText = "Hawk"
        if (self.blobType == "D"): blobTypeText = "Dove"
        return "(Lv. " + str(self.predatorLevel) + " " + blobTypeText + ")"


def computeFoodRewards(blob1, blob2):
    if blob1.getBlobType() == "D" and blob2.getBlobType() == "D": return 1, 1
    elif blob1.getBlobType() == "H" and blob2.getBlobType() == "H": return 0, 0
    elif blob1.getBlobType() == "D" and blob2.getBlobType() == "H":
        blob2.predatorLevelUp()
        return .5, 1.5
    elif blob1.getBlobType() == "H" and blob2.getBlobType() == "D":
        blob1.predatorLevelUp()
        return 1.5, .5

def computeBlobFate(blob):
    survives = False
    reproduces = False

    if blob.getBlobReward() < 1:
        survivalChance = blob.getBlobReward()
        if random.random() < survivalChance: survives = True
    else:
        survives = True
        babyChance = blob.getBlobReward() - 1
        if random.random() < babyChance: reproduces = True

    return survives, reproduces



# -------------------------------   MAIN CODE   --------------------------------------

setTextColorCyan()
print("WELCOME TO BLOB SIMULATOR!")

setTextColorYellow()
NUM_DAYS = int(input("How many days to simulate?   >>> "))

setTextColorBlue()
START_DOVES = int(input("How many doves/blue blobs [0, 10]?   >>> "))

setTextColorRed()
START_HAWKS = int(input("How many hawks/red blobs [0, 10]?   >>> "))

setTextColorGreen()
NUM_FOOD_PAIRS = int(input("How many available pairs of food?   >>> "))

setTextColorCyan()
text_speed = .01 * int(input("Enter text speed [0 = slowest, 100 = instant]   >>> "))
TEXT_WAIT = 1 - text_speed

# Initialize blobs
livingBlobs = []

for blueNum in range(START_DOVES):
    doveFirstName = blobNames[random.randint(0, len(blobNames) - 1)]
    doveLastName = doveFamilies.pop(random.randint(0, len(doveFamilies) - 1))
    newDove = Blob("D", doveFirstName, doveLastName)
    livingBlobs.append(newDove)

for redNum in range(START_HAWKS):
    hawkFirstName = blobNames[random.randint(0, len(blobNames) - 1)]
    hawkLastName = hawkFamilies.pop(random.randint(0, len(hawkFamilies) - 1))
    newHawk = Blob("H", hawkFirstName, hawkLastName)
    livingBlobs.append(newHawk)

# Run simulation
for dayNum in range(NUM_DAYS):

    setTextColorYellow()
    time.sleep(TEXT_WAIT * 5)
    print(f"STARTING DAY {dayNum + 1} OF {NUM_DAYS} ({NUM_FOOD_PAIRS} food pairs)")
    setTextColorWhite()

    printLivingBlobs("Start of day:")

    availableFoodPairs = [0] * NUM_FOOD_PAIRS

    completedFoodPairs = []
    # Assign blobs to food pairs for the round
    while len(livingBlobs) > 0 and len(availableFoodPairs) > 0:

        chosenBlobNum = random.randint(0, len(livingBlobs) - 1)
        chosenBlob = livingBlobs.pop(chosenBlobNum)

        foodPairNum = random.randint(0, len(availableFoodPairs) - 1)
        if availableFoodPairs[foodPairNum] == 0: availableFoodPairs[foodPairNum] = [chosenBlob]
        else:
            availableFoodPairs[foodPairNum].append(chosenBlob)
            completedPair = availableFoodPairs.pop(foodPairNum)
            completedFoodPairs.append(completedPair)

    # Any blobs that didn't get assigned a food pair will starve
    for blobThatWillStarve in range(len(livingBlobs)):
        livingBlobs[blobThatWillStarve].setBlobReward(0)

    # Get reward for blobs that have food to themselves
    for pairNum in range(len(availableFoodPairs)):
        if availableFoodPairs[pairNum] != 0:
            luckyBlob = availableFoodPairs[pairNum][0]
            time.sleep(TEXT_WAIT)
            print(f"{luckyBlob.getBlobFullName()} gets all the food to themselves!")
            luckyBlob.setBlobReward(2)
            livingBlobs.append(luckyBlob)

    # Get rewards for each blob that is partnered with another blob
    for pairNum in range(len(completedFoodPairs)):
        blobOne = completedFoodPairs[pairNum][0]
        blobTwo = completedFoodPairs[pairNum][1]
        time.sleep(TEXT_WAIT)
        print(f"{blobOne.getBlobFullName()} {blobOne.printPredatorLevel()} vs. {blobTwo.getBlobFullName()} {blobTwo.printPredatorLevel()}")
        rewardOne, rewardTwo = computeFoodRewards(blobOne, blobTwo)
        blobOne.setBlobReward(rewardOne)
        blobTwo.setBlobReward(rewardTwo)
        livingBlobs.append(blobOne)
        livingBlobs.append(blobTwo)

    printLivingBlobs("After lunch... Blob rewards:", True)

    newLivingBlobs = []
    # Now that rewards have been obtained, use them to determine the fate of each blob
    for blobNum in range(len(livingBlobs)):
        currentBlob = livingBlobs[blobNum]
        survives, reproduces = computeBlobFate(livingBlobs[blobNum])

        if survives:
            newLivingBlobs.append(currentBlob)
        else:
            time.sleep(TEXT_WAIT)
            print(f"{currentBlob.getBlobFullName()} (reward of {currentBlob.getBlobReward()}) dies...")

        if reproduces:
            babyName = blobNames[random.randint(0, len(blobNames) - 1)]
            time.sleep(TEXT_WAIT)
            print(f"{currentBlob.getBlobFullName()} births {babyName} {currentBlob.getBlobLastName()}")
            babyBlob = Blob(currentBlob.getBlobType(), babyName, currentBlob.getBlobLastName(), currentBlob.getBlobGeneration() + 1)
            newLivingBlobs.append(babyBlob)

    # Print out remaining blobs after the round
    livingBlobs = newLivingBlobs
    printLivingBlobs("End of day:")
