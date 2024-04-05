def square(item_list):
    squares = []
    for l in item_list:
        squares.append( l**2 )
    return squares
my_list = [17,15,89]
my_result = square( my_list)
print(my_result)