#   File: WordSearch.py
#   Description: This is a program that solves a wordsearch
#   Student's Name: Nicolas Kim
#   Student's UT EID: nak848
#   Course Name: CS 313E
#   Unique Number: 50205
#   Date Created: 9/15/2019
#   Date Last Modified: 9/16/2019

def main():
    # Create the block of chars, positions, and the word list
    lists = create_char_block_and_words()
    char_block_str_rows = lists[0]
    char_block_str_cols = lists[1]
    word_list = lists[2]
    # Search by Word
    found_row_list = []
    found_col_list = []
    found_se_list = []
    found_sw_list = []
    for i in word_list:
        row_find = search_row(i, char_block_str_rows)
        if row_find is not None:
            found_row_list.append(row_find)
        elif row_find is None:
            col_find = search_column(i, char_block_str_cols)
            if col_find is not None:
                found_col_list.append(col_find)
            elif col_find is None:
                se_find = search_se(i, char_block_str_rows)
                if se_find is not None:
                    found_se_list.append(se_find)
                elif se_find is None:
                    sw_find = search_sw(i, char_block_str_rows)
                    if sw_find is not None:
                        found_sw_list.append(sw_find)
    whole_list = found_col_list + found_row_list + found_se_list + found_sw_list
    whole_list.sort()
    new_file = open('found.txt', 'w')
    for item in whole_list:
        word = ''.join(item[0])
        new_file.write('{} {} {}\n'.format(word, item[1], item[2], "4d").expandtabs(10))
    new_file.close()


# need to swap the x and y for col list


def create_char_block_and_words():
    # opening the file, attaching a readline, and reading the first line
    file = open('hidden.txt', 'r')
    file_line = file.readline()
    first_line = file_line.split()
    file_line = file.readline()
    counter = 0
    for i in first_line:
        first_line[counter] = int(i)
        counter += 1
    # m is the lines (rows)
    m = first_line[0]
    # n is the characters in the rows
    n = first_line[1]
    # Create the char block strings row
    char_block_str_row = []
    for i in range(m):
        file_line = file.readline()
        line = file_line.split()
        char_block_str_row.append(line)

    char_block_str_col = []
    for a in range(n):
        col_list = []
        for i in range(n):
            col_list.append(char_block_str_row[i][a])
        char_block_str_col.append(col_list)

    # Create the char block positional
    #    char_block_pos = []
    #    x = 0
    #    for i in range(m):
    #        y = 0
    #        char_block_pos.append([])
    #        for a in range(n):
    #            char_block_pos[x].append((x, y), )
    #            y += 1
    #        x += 1
    # C

    # create the Word List
    file_line = file.readline()
    k = int(file.readline())
    word_list = []
    for i in range(k):
        file_line = file.readline()
        word = list(file_line)
        word = word[:-1]
        word_list.append(word)

    return [char_block_str_row, char_block_str_col, word_list]


def search_row(word_char_list, char_block_str):
    for i in char_block_str:
        if word_char_list[0] in i:
            indicies = [check for check, x in enumerate(i) if x == word_char_list[0]]
            check = 1
            for a in indicies:
                right = a + 1
                left = a - 1
                try:
                    if word_char_list[1] == i[right]:
                        for rest_of_word in word_char_list[2:]:
                            right += 1
                            if rest_of_word == i[right]:
                                check = True
                            else:
                                check = False
                                break
                except IndexError:
                    check = False
                if check is True:
                    return word_char_list, char_block_str.index(i) + 1, a + 1
                try:
                    if word_char_list[1] == i[left]:
                        for rest_of_word in word_char_list[2:]:
                            left -= 1
                            if rest_of_word == i[left]:
                                check = True
                            else:
                                check = False
                                break
                        if check == True:
                            return word_char_list, char_block_str.index(i) + 1, a + 1
                except IndexError:
                    check = False


def search_column(word_char_list, char_block_str):
    for i in char_block_str:
        if word_char_list[0] in i:
            indices = [check for check, x in enumerate(i) if x == word_char_list[0]]
            check = 0
            for a in indices:
                down = a + 1
                up = a - 1
                try:
                    if word_char_list[1] == i[down]:
                        for rest_of_word in word_char_list[2:]:
                            down += 1
                            if rest_of_word == i[down]:
                                check = True
                            else:
                                check = False
                                break
                except IndexError:
                    check = False
                if check is True:
                    return word_char_list, a + 1, char_block_str.index(i) + 1
                try:
                    if word_char_list[1] == i[up]:
                        for rest_of_word in word_char_list[2:]:
                            up -= 1
                            if rest_of_word == i[up]:
                                check = True
                            else:
                                check = False
                                break
                except IndexError:
                    check = False
                if check is True:
                    return word_char_list, a + 1, char_block_str.index(i) + 1


def search_se(word_char_list, char_block_str):
    for i in char_block_str:
        if word_char_list[0] in i:
            indicies = [check for check, x in enumerate(i) if x == word_char_list[0]]
            check = 1
            for a in indicies:
                right = a + 1
                down = char_block_str.index(i) + 1
                try:
                    if word_char_list[1] == char_block_str[down][right]:
                        for rest_of_word in word_char_list[2:]:
                            right += 1
                            down += 1
                            if rest_of_word == char_block_str[down][right]:
                                check = True
                            else:
                                check = False
                                break
                except IndexError:
                    check = False
                if check is True:
                    return word_char_list, char_block_str.index(i) + 1, a + 1
                try:
                    left = a - 1
                    up = char_block_str.index(i) - 1
                    if word_char_list[1] == char_block_str[up][left]:
                        for rest_of_word in word_char_list[2:]:
                            left -= 1
                            up -= 1
                            if rest_of_word == char_block_str[up][left]:
                                check = True
                            else:
                                check = False
                                break
                        if check == True:
                            return word_char_list, char_block_str.index(i) + 1, a + 1
                except IndexError:
                    check = False


def search_sw(word_char_list, char_block_str):
    for i in char_block_str:
        if word_char_list[0] in i:
            indices = [check for check, x in enumerate(i) if x == word_char_list[0]]
            check = 1
            for a in indices:
                left = a - 1
                down = char_block_str.index(i) + 1
                try:
                    if word_char_list[1] == char_block_str[down][left]:
                        for rest_of_word in word_char_list[2:]:
                            left -= 1
                            down += 1
                            if rest_of_word == char_block_str[down][left]:
                                check = True
                            else:
                                check = False
                                break
                except IndexError:
                    check = False
                if check is True:
                    return word_char_list, char_block_str.index(i) + 1, a + 1
                try:
                    right = a + 1
                    up = char_block_str.index(i) - 1
                    if word_char_list[1] == char_block_str[up][right]:
                        for rest_of_word in word_char_list[2:]:
                            right += 1
                            up -= 1
                            if rest_of_word == char_block_str[up][right]:
                                check = True
                            else:
                                check = False
                                break
                        if check is True:
                            return word_char_list, char_block_str.index(i) + 1, a + 1
                except IndexError:
                    check = False


if __name__ == "__main__":
    main()
