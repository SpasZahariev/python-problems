



# function that says id smallString is contained in bigString?


def preProcessSmallString(smallString: str):

    prefixLen = 0
    properPrefixes = [None] * len(smallString) 
    properPrefixes[0] = 0 # this is always going to be 0

    # AABAACAA
    index = 1
    while(index < len(smallString)):
        if(smallString[index] == smallString[prefixLen]):
            prefixLen += 1
            properPrefixes[index] =  prefixLen
            index +=1
        else:
            if (prefixLen > 0):
                prefixLen = properPrefixes[prefixLen - 1] # we are going back to the position the prev is pointing to
            else:
                properPrefixes[index] = 0
                index += 1
    
    return properPrefixes

def kmpSearch(bigString: str, smallString: str) -> bool:

    properPrefixes = preProcessSmallString(smallString)

    smallStringIndex = 0
    bigStringIndex = 0

    while bigStringIndex < len(bigString):
        if (smallStringIndex == len(smallString)):
            return True 

        if (bigString[bigStringIndex] == smallString[smallStringIndex]):
            smallStringIndex +=1
            bigStringIndex +=1
        else:
            print("failed to match at: " +  str(bigStringIndex))
            print("goin back to: " + str(properPrefixes[smallStringIndex - 1]))
            smallStringIndex = properPrefixes[smallStringIndex - 1]
            if smallStringIndex == 0:
                bigStringIndex +=1
            
    if (smallStringIndex == len(smallString)):
        return True
    return False 

smallString = "aaacaaab"
bigString = "aaacaaacaaab"
print("Does " + bigString + " contain " + smallString + " : " + str(kmpSearch(bigString, smallString)))
