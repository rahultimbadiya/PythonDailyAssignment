def Factorial(num):
    sum = 0
    if num == 1:
        return 1
    else:
        sum = num * Factorial(num-1)
        return (sum)

print(Factorial(4))