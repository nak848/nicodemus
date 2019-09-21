#     File: Intervals.py
#   Description: A code that takes a file of integer intervals and sorts/combines them if they overlap
#   Student's Name: Nicolas Kim
#   Student's UT EID: nak848
#   Course Name: CS 313E
#   Unique Number: 50205
#   Date Created: 9/9/2019
#   Date Last Modified: 9/9/2019


def main():
    file = open("intervals.txt", "r")

    interval_list = sorted(create_list(file))
    combine_intervals(interval_list)
    print('Non-intersecting Intervals:')
    for i in range(len(interval_list)):
        print(interval_list[i])
    print('Non-intersecting Intervals in order of size:')
    new_list = order_by_size(interval_list)
    for i in range(len(new_list)):
        print(new_list[i])


def create_list(file):
    file_line = file.readlines()
    interval_list = []
    temp_list = []
    for x in file_line:
        line_string = x
        del temp_list
        temp_list = []
        for num in line_string.split():
            try:
                temp_list.append(int(num))
            except ValueError:
                pass
        temp_tuple = tuple(temp_list)
        interval_list.append(temp_tuple)
        del temp_tuple

    return interval_list

def combine_intervals(interval_list):
    spot = 0
    counter = len(interval_list)
    y = 0
    z = 0
    for i in range(counter):
        try:
            if interval_list[spot][1] >= interval_list[spot + 1][0]:
                if interval_list[spot][1] >= interval_list[spot + 1][1]:
                    first_num = interval_list[spot][0]
                    second_num = interval_list[spot][1]
                    interval_list.insert(spot , (first_num, second_num))
                    del interval_list[spot + 1]
                    del interval_list[spot + 1]
                else:
                    first_num = interval_list[spot][0]
                    second_num = interval_list[spot + 1][1]
                    interval_list.insert(spot , (first_num, second_num))
                    del interval_list[spot + 1]
                    del interval_list[spot + 1]
            else:
                spot = spot + 1
        except IndexError:
            break

def order_by_size(interval_list):
    place_list = []
    for i in range(len(interval_list)):
        place_list.append(int(abs(abs(interval_list[i][1]) - abs(interval_list[i][0]))))
    new_list = [interval_list for place_list, interval_list in sorted(zip(place_list, interval_list))]
    return new_list

if __name__ == "__main__":
    main()