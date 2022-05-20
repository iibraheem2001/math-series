
def fib(num):
    """
    fib is short for fibonacci
    the function below goes through the process of computing the sequence
    the first 8 fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21
    """
    if num == 0:
      return 0
    elif num == 1:
      return 1
    elif num == 2:
      return 1
    return fib(num - 1) + fib(num - 2)

# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843
def lucas(num):
    """
    the lucas sequence is very similar to the fibonacci sequence.
    the difference is the starting points.
    the lucas series starts with the following numbers: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843

    """
    if num == 0:
      return 2
    elif num == 1:
      return 1
    return lucas(num - 1) + lucas(num - 2)


def sum_series(num, num1 = 0, num2 = 1):
    """
    the sum_series is a function that looks at the argument passed to it and decides if it will return
    the nth number in the fibonacci series, the lucas series or other series based on values of num1 and num2 arguments.
    """

    if num1 == 0 and num2 ==1:
        return fib(num)
    elif num1 == 2 and num2 == 1:
        return lucas(num)
    else:
        if num == 0:
            return num1
        elif num == 1:
            return num2
        return sum_series(num - 1, num1, num2) + sum_series(num - 2, num1, num2)




