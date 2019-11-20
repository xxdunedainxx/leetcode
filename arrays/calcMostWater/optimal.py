container = [1,8,6,2,5,4,8,3,7]

def calculateMostWater(cont : [int])->int:
    largestVolume: int = 0
    i = 0
    j = (len(container)-1)

    while j != i:
        height=min(cont[i], cont[j])
        width= j - i

        if (height * width) > largestVolume:
            largestVolume= (height * width)

        if i > j:
            j-=1
        else:
            i+=1
    return largestVolume