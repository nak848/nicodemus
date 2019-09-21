#   File: MagicSquare.py
#   Description: This is a program that generates completed magic squares from any given odd input
#   Student's Name: Nicolas Kim
#   Student's UT EID: nak848
#   Course Name: CS 313E
#   Unique Number: 50205
#   Date Created: 8/30/2019
#   Date Last Modified: 9/6/2019

def main():

    n = int(input('Please enter a positive odd number: '))
    n_odd_check = int(n/2)
    while n <= 0 or (n/2) == n_odd_check:
        n = int(input('Invalid entry. Please enter a positive odd number: '))
        n_odd_check = int(n / 2)

    magic_square = make_square(n)

    print_square(magic_square)

    check_square(magic_square)

def make_square(n):
    number_order = make_numbers(n)

    base_lists = make_lists(n)

    magic_square = assign_position(number_order, base_lists, n)

    return magic_square

def print_square(magic_square):
    x = 0
    y = 0
    n = len(magic_square)
    for i in range(n):
        for a in range(n):
            print(format(magic_square[i][a], '4d'), end = "")
            if a == n - 1:
                print()

def check_square(magic_square):
    n = len(magic_square)
    tick = check_square_2(magic_square, n)
    return tick

def make_numbers(num):
    magic_square_list = []
    counter = 0
    for x in range(1, (num**2 + 1)):
        magic_square_list.append(x)


    return(magic_square_list)

def make_lists(list_num):
    square = []
    counter = 0
    for x in range(list_num):
        square.append([])
    while counter < list_num:
        for i in range(list_num):
            square[i].append(0)
        counter = counter +1
    return(square)

def assign_position(order, place, n):
    x = n-1
    y = n//2
    for i in order:
        if i == 1:
            place[x][y] = 1
        elif place[x][y] == 0:
            place[x][y] = i
        elif place[x][y] != 0:
            y = y - 1
            x = x - 2
            if x >= n:
                x = 0
            if y >= n:
                y = 0
            place[x][y] = i

        x = x + 1
        y = y + 1
        if x >= n:
            x = 0
        if y >= n:
            y = 0




    return place

def check_square_2(magic_square, n):
    tick = 0
    cannonical = int(n * (n**2 + 1)/2)
    tick = check_rows(magic_square, n) + tick
    tick = check_columns(magic_square, n) + tick
    tick = check_diagonals(magic_square, n) + tick
    if tick == 0:
        print('This is a magic square and the canonical sum is', cannonical)
        tick = True
    else:
        print('This is not a magic square')
        tick = False
    return tick

def check_rows(magic_square, n):
    x = 0
    y = 0
    z = 0
    tick = 0
    for i in range(n):
        for g in range(n):
            z = z + magic_square[x][y]
            x = x + 1
        if z != (n * ((n ** 2 + 1) / 2)):
            tick = tick + 1
        x = 0
        y = y + 1
        z = 0
        return tick

def check_columns(magic_square, n):
    x = 0
    y = 0
    z = 0
    tick = 0
    for i in range(n):
        for g in range(n):
            z = z + magic_square[x][y]
            y = y + 1
        if z != (n * ((n ** 2 + 1) / 2)):
            tick = tick + 1
        y = 0
        x = x + 1
        z = 0
        return tick

def check_diagonals(magic_square, n):
    x = n - 1
    y = 0
    z = 0
    tick = 0
    for i in range(n):
        for g in range(n):
            z = z + magic_square[x][y]
            y = y + 1
            x = x - 1
        if z != (n * ((n ** 2 + 1) / 2)):
            tick = tick + 1
        y = n-1
        x = 0
        z = 0
        for g in range(n):
            z = z + magic_square[x][y]
            x = x + 1
            y = y - 1
        if z != (n * ((n ** 2 + 1) / 2)):
            tick = tick + 1
        return tick

main()