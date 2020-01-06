nums = [0,0,1,1,1,2,2,3,3,4]
currentP = 0
maxValue = 3
count = 0
for i in range(len(nums)):
    if nums[i] > maxValue:
        nums[currentP] = nums[i]
        maxValue = nums[i]
        currentP = currentP + 1
        count = count + 1
        print(nums)
        print(nums[i], i)
        print("CurrentP ", currentP)
    else:
        print("Else ", nums[i])
print(nums)
print(count)
     
for i in range(10-1):
    for j in range(i+1, 10):
        print(j,end = '')
    print()
