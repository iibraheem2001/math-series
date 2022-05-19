

def fib(n):


    a = 0
    b = 1


    # print(a)
    # print(b)
    final = 0
    for i in range(2,n):

        final = a + b
        a = b
        b = final

    return final
print(fib(10))

# def lucas(n):
#
#
#     a = 2
#     b = 1
#
#     print(a)
#     print(b)
#
#     for i in range(3,n):
#
#         c = a + b
#         a = b
#         b = c
#         print(c)
#
# lucas(10)