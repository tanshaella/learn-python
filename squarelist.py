# Implement the following function:
# def_square_list(lst)
# The function is given a list of numbers lst, and squares its 
# elements.

# Implement the following functions:
# a. def_create_sqr_list(lst)
# will create and return a new list containing the square of the 
# corresponding elements in lst.
# b. def_sqr_list_in_place(lst)
# will square, in-place, each element in lst.

# def sqr_list_in_place(lst):
#     for elem in lst:
#         elem = elem*elem

# NOT WORKING ^

def sqr_list_in_place(lst):
    for i in range(len(lst):
            lst[i]=lst[i]*lst[i]
