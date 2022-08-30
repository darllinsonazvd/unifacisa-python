num1 = int(input())
minor = 0

for i in range(1, 100):
    nums = int(input())
    if nums > minor:
        major = nums
        position = i + 1
        minor = nums

print(major)
print(position)
