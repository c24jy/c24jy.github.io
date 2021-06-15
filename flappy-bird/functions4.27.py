# def twice(x):
#     return x * 2
#     # or x + x
#
# x = "hello"
# y=twice(x)
#
# print(y)

# new = []
#
# def twice(nums):
#     for num in nums:
#         new.append(2 * num)
#
#     return new



# def even(nums):
#     new = []
#     for num in nums:
#         if (num%2 == 0):
#             new.append(num)
#     return new
#
# nums = [1, 3, 4, 8, 6, 13]
# print(even(nums))

def onscreenpipes(pipes):
    new = []
    for pipe in pipes:
        if pipe>0:
            new.append(pipe)
    return new

pipes = [-1, 3, -6, 2, 3]
print(onscreenpipes(pipes))

