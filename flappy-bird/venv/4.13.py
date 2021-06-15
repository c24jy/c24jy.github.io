# def get_double_of_all(input):
#     new_list = []
#     for num in input:
#         new_list.append(num * 2)
#     return new_list
#
# x = [1, 2, 3, 4, 5]
# double_of_x = get_double_of_all(x)
#
# print(double_of_x)

def square_everything(input):
    square_list = []
    for num in input:
        if num * num < 5:
            square_list.append(num ** 2)
    return square_list

x = [0, 1, 2, 7]
square_of_x = square_everything(x)

print(square_of_x)

#same thing as

def square_everything(x):
    newlist = []
    for num in x:
            if num * num < 5:
                newlist.append(num ** 2)
    return newlist

j = square_everything([0, 1, 2, 7])
print(j)