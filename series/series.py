
def fib(num):
    if num == 0:
      return 0
    elif num == 1:
      return 1
    elif num == 2:
      return 1
    return fib(num - 1) + fib(num - 2)

# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843
def lucas(num):
    if num == 0:
      return 2
    elif num == 1:
      return 1
    return lucas(num - 1) + lucas(num - 2)


def sum_series(num, num1 = 0, num2 = 1):

    if num1 == 0 and num2 ==1:
        return fib(num)
    elif num1 == 2 and num2 == 1:
        return lucas(num)
    else:
        return 'invalid'


print(sum_series(6, 2, 1))



