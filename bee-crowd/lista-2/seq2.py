sizeOfLine, limit = map(int, input().split())

nums = []
first = 0

i = 0

while i < limit - sizeOfLine:
    for j in range(1, sizeOfLine + 1):
        nums.append(i + 1)
        div = nums[first]
        nums[first] = str(nums[first])
        first += 1
        i += 1

    first = 0
    nums = " ".join(nums)
    print(nums)
    nums = []

rest = limit % sizeOfLine

if rest == 0:
    for x in range(limit - sizeOfLine, limit):
        nums.append(x + 1)
        nums[first] = str(nums[first])
        first += 1
    nums = " ".join(nums)
    print(nums)

if rest != 0:
    for x in range(div, limit):
        nums.append(x + 1)
        nums[first] = str(nums[first])
        first += 1
    nums = " ".join(nums)
    print(nums)
