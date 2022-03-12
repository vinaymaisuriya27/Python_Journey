def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

if __name__ == '__main__':
    num = 5
    print(factorial(num))