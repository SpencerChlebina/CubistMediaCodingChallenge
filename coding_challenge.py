#!/usr/bin/env python

evilList = "1 2 2 2 3 5 10"
goodList = "1 2 3 3 4 10"

def goodVevil(evilCount, goodCount):
    
    evilScore = sum(map(int, evilCount.split()))
    goodScore = sum(map(int, goodCount.split()))

    if evilScore > goodScore:
        return "Battle Result: Evil eradicates all trace of Good"
    elif goodScore > evilScore:
        return "Battle Result: Good triumphs over Evil"
    else:
        return "Battle Result: No victor on this battle field"

print(goodVevil("1 2 2 2 3 5 10", "1 2 3 3 4 10"))
    

