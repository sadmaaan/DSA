def numWaterBottles(numBottles, numExchange):
    drink = numBottles
    extras = 0
    
    while numBottles >= numExchange:
        extras = numBottles % numExchange
        numBottles //= numExchange
        drink += numBottles
        numBottles += extras
        
    return drink

print(numWaterBottles(15, 4))