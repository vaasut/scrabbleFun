import random, copy

def createScrabbleBag():
    ones = "KJXQZ"
    twos = "?BCMPFHVWY"
    threes= "G"
    fours = "LSUD"
    sixes = "NRT"
    eights = "O"
    nines = "AI"
    twelves = "E"
    scrabbleBag = ones + twos*2 + threes*3 + fours*4 + sixes*6 + eights*8 + nines*9 + twelves*12
    scrabbleBag = list(scrabbleBag)
    scrabbleBag.sort()
    return scrabbleBag

def removeTiles(tiles,scrabbleBag):
    #will error if tiles are not in bag.
    for letter in tiles:
        scrabbleBag.remove(letter)
    return scrabbleBag

def drawNTiles(n,scrabbleBag):
    #randomly draw n tiles from bag. does not change bag composition.
    random.shuffle(scrabbleBag)
    draw = scrabbleBag[0:n]
    return draw

def wordInRack(word,rack):
    #check if word in rack. blanks are ? symbol.
    rackCopy = copy.deepcopy(rack) #don't modify the rack
    missing = 0
    for letter in word:
        if letter in rackCopy:
            rackCopy.remove(letter)
        else:
            missing += 1
    for i in range(2):
        if "?" in rackCopy:
            rackCopy.remove("?")
            missing -= 1
    if missing <= 0:
        return True
    return False
        

def simulateDraw(successDraws,scrabbleBag,iterations):
    """simulates iterations nnumber of draws from scrabble bag
    if any of the success draws are drawn, it counts as success"""
    successCount = 0.0
    for i in range(iterations):
        success = False
        rack = drawNTiles(7,scrabbleBag)
        for word in successDraws:
            if wordInRack(word,rack): 
                success = True # don't double count if two of the successes are drawn together
        if success:
            successCount += 1
    return successCount / iterations


if __name__ == "__main__":
    scrabbleBag = createScrabbleBag()
    tilesPreviouslyDrawn = "HELLO" #use capital letters and ? for blanks
    scrabbleBag = removeTiles(tilesPreviouslyDrawn,scrabbleBag)
    probability = simulateDraw(["FINDING", "CHANCE", "ALL", "DRAW"],scrabbleBag,1000000)
    print(probability)



