# two sum
twoSum=[2, 11, 15, -2]
target=9


# Return indices of two numbers such that they add up to specific target 
def calcTwoSum(arr: [int], targetNum: int)->[int]:
    hashTracker: dict = {

    }

    for i in range(len(arr)):
        inverse = targetNum - arr[i]
        print(inverse)
        if inverse in hashTracker.keys():  
            print(hashTracker)
            return [hashTracker[inverse],i]
        hashTracker[arr[i]]=i

    return []

#print(calcTwoSum(twoSum,target))

threeSum=[-1, 0, 1, 2, -1, -4]
threeSumTarget=0

def calcThreeSum(arr: [int], targetNum: int)->[ [int] ]:
    rArrays: [[int]] = []

    hashTracker: dict = {

    }

    i = 0 
    j = len(arr)-1

    while i < j:
        print("checking")
        check1 = targetNum - arr[i]
        check2 = targetNum - arr[j]
        print(f"check1: {check1}, check2: {check2}")
        if check1 in hashTracker.keys():
            print("check 1 triggered!")
            print(f"{check1} target num:: {arr[j]}")
            if (arr[j] in hashTracker[check1].keys()):
                rArrays.append(check1, arr[i], arr[j])
            elif hashTracker[check1] is None:
                hashTracker[check1]={}
            else:
                hashTracker[check1][arr[j]]=j

        if check2 in hashTracker.keys():
            print("check 1 triggered!")
            print(f"{check2} target num:: {arr[i]}")
            if (arr[i] in hashTracker[check2].keys()):
                rArrays.append(check2, arr[i], arr[j])
            elif hashTracker[check2] is None:
                hashTracker[check2]={}
            else:
                hashTracker[check2][arr[i]]=i
        if arr[i] not in hashTracker.keys():
            hashTracker[arr[i]]={}
        if arr[j] not in hashTracker.keys():
            hashTracker[arr[j]]={}
        print(hashTracker)
        i+=1
        j-=1
    return rArrays

print(calcThreeSum(threeSum, threeSumTarget))
