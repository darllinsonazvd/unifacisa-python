nums = input().split(" ")

num1, num2 = int(nums[0]), int(nums[1])

if num1 > num2:
    if num1 % num2 == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
elif num1 < num2:
    if num2 % num1 == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
elif num1 == num2:
    print("Sao Multiplos")
