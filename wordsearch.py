#############################################################
# FILE: wordsearch.py
# WRITER: Amir Rosengarten, amir.rosen15, 207942285
# EXERCISE: intro2cs2 ex5 2022
# DESCRIPTION:A program that finds words within a matrix of letters (bulk).
#############################################################

import sys


def read_wordlist(filename):

    """
    The function opens the file whose name is given as a parameter, and
     reads the words inside it.
    :param filename: A name of a file which contains the word list and is
     represented as a string.
    :return: The function returns a list of words read from the file,
     in order.
    """

    words = []
    f_words = open(filename)
    for line in f_words:
        words.append(line.strip())
    f_words.close()
    return words


def read_matrix(filename):

    """
    The function gets the name of a file that contains the letter matrix
     and is represented as a string.
    :param filename: The filename.
    :return: The function returns a two-dimensional list of the matrix
     letters.
    """

    f_matrix = open(filename)
    matrix_lst = []
    for line in f_matrix:
        letters_lst = line.strip().split(",")
        matrix_lst.append(letters_lst)
    f_matrix.close()
    return matrix_lst


def reverse_matrix(matrix_lst):

    """
    The function gets a two-dimensional list of the matrix letters.
    :param matrix_lst: List of the matrix letters.
    :return: The function returns a two-dimensional list of the matrix
     letters, so that each internal list returns in reverse order.
    """
    reversed_mat = []
    for row in matrix_lst:
        reversed_mat.append(row[:])
    for i in range(len(reversed_mat)):
        reversed_mat[i].reverse()
    return reversed_mat


def transpose_matrix(matrix_lst):

    """
    The function gets a two-dimensional list of the matrix letters.
    :param matrix_lst: List of the matrix letters.
    :return: The function returns a two-dimensional list of the matrix
     letters so that the matrix that returns as output is the transpose
     matrix of the original.
    """

    rows = len(matrix_lst)
    columns = len(matrix_lst[0])
    transpose = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix_lst[i][j])
        transpose.append(row)
    return transpose


def up_right_diagonal(matrix_lst):

    """
    The function gets a two-dimensional list of the matrix letters.
    :param matrix_lst: List of the matrix letters.
    :return: The function returns a two-dimensional list of letters
     arranged on the diagonals of the original matrix, from left to right
      in the top direction.
    """

    lenght_col = len(matrix_lst[0])
    lenght_row = len(matrix_lst)
    forward_diag = [[] for _ in range(lenght_row + lenght_col - 1)]
    for i in range(lenght_col):
        for j in range(lenght_row):
            forward_diag[i + j].append(matrix_lst[j][i])
    return forward_diag


def down_right_diagonal(matrix_lst):

    """
    The function gets a two-dimensional list of the matrix letters.
    :param matrix_lst: List of the matrix letters.
    :return: The function returns a two-dimensional list of letters
    arranged on the diagonals of the original matrix, from left to right
    in the downward direction.
    """

    lenght_col = len(matrix_lst[0])
    lenght_row = len(matrix_lst)
    back_diag = [[] for _ in range(lenght_row + lenght_col - 1)]
    min_back_diag = -lenght_row + 1
    for i in range(lenght_col):
        for j in range(lenght_row):
            back_diag[i - j - min_back_diag].append(matrix_lst[j][i])
    return back_diag


def search_words_and_count(words, matrix_lst, good_words_lst):

    """
    The function gets the word list, the letter matrix, and an empty list.
    :param words: Word list.
    :param matrix_lst: Letter matrix.
    :param good_words_lst: An empty list.
    :return: The function returns a dictionary that contains the words
     found in each search, and the amount of each word found in that
     search.
    """

    count = 0
    for word in words:
        word_count = 0
        for line in matrix_lst:
            for i in range(len(line)):
                for j in range(len(word)):
                    if i + j < len(line):
                        if word[j] == line[i + j]:
                            count += 1
                if count == len(word):
                    word_count += 1
                count = 0
            count = 0
        if word_count > 0:
            good_words_lst.append((word, word_count))
    new_dict = dict(good_words_lst)
    return new_dict


def update_dict(current_dict, final_dict):

    """
    The function gets 2 dictionaries.
    :param current_dict: Current dictionary.
    :param final_dict: Updated dictionary.
    :return: The function returns the updated dictionary, which contains
     the words found and the number of times they appeared.
    """

    # The function goes over the key values, and if there are identical
    # keys, then it adds the amount of each value to the updated
    # dictionary.
    for key in current_dict.keys():
        if key in final_dict:
            final_dict[key] += current_dict[key]
        else:
            final_dict.update({key: current_dict[key]})
    return final_dict


def dictionary_to_list(f_dict):

    """
    The function gets a dictionary.
    :param f_dict: A dictionary.
    :return: The function converts the dictionary to a list of tuples.
    """

    final_lst = [(word, count) for word, count in f_dict.items()]
    return final_lst


def right_search(matrix_lst, words):
    # r

    """
    The function gets the letter matrix, and the word list.
    :param matrix_lst: Letter matrix.
    :param words: Word list.
    :return: The function returns a dictionary of all the words found in
     the right direction, and the amount of their occurrence.
    """

    good_words_lst = []
    # Call to a function search_words_and_count
    return search_words_and_count(words, matrix_lst, good_words_lst)


def left_search(matrix_lst, words):
    # l

    """
        The function gets the letter matrix, and the word list.
        :param matrix_lst: Letter matrix.
        :param words: Word list.
        :return: The function returns a dictionary of all the words found
         in the left direction, and the amount of their occurrence.
        """

    good_words_lst = []
    # Call to a function reverse_matrix
    matrix_reverse = reverse_matrix(matrix_lst)
    # Call to a function search_words_and_count
    return search_words_and_count(words, matrix_reverse, good_words_lst)


def up_search(matrix_lst, words):
    # u

    """
        The function gets the letter matrix, and the word list.
        :param matrix_lst: Letter matrix.
        :param words: Word list.
        :return: The function returns a dictionary of all the words found
         in the top direction, and the amount of their occurrence.
        """

    # Call to a function matrix_transpose
    matrix_transpose = transpose_matrix(matrix_lst)
    # Call to a function reverse_matrix
    matrix_reverse = reverse_matrix(matrix_transpose)
    good_words_lst = []
    # Call to a function search_words_and_count
    return search_words_and_count(words, matrix_reverse, good_words_lst)


def down_search(matrix_lst, words):
    # d

    """
        The function gets the letter matrix, and the word list.
        :param matrix_lst: Letter matrix.
        :param words: Word list.
        :return: The function returns a dictionary of all the words found
         in the down direction, and the amount of their occurrence.
        """

    # Call to a function matrix_transpose
    matrix_transpose = transpose_matrix(matrix_lst)
    good_words_lst = []
    # Call to a function search_words_and_count
    return search_words_and_count(words, matrix_transpose, good_words_lst)


def up_right_search(matrix_lst, words):
    # w

    """
        The function gets the letter matrix, and the word list.
        :param matrix_lst: Letter matrix.
        :param words: Word list.
        :return: The function returns a dictionary of all the words found
         in the up and right direction (diagonal ascends to the right),
          and the amount of their occurrence.
        """

    good_words_lst = []
    # Call to a function matrix_diagonal
    matrix_diagonal = up_right_diagonal(matrix_lst)
    # Call to a function search_words_and_count
    return search_words_and_count(words, matrix_diagonal, good_words_lst)


def down_left_search(matrix_lst, words):
    # z

    """
        The function gets the letter matrix, and the word list.
        :param matrix_lst: Letter matrix.
        :param words: Word list.
        :return: The function returns a dictionary of all the words found
         in the down and left direction (diagonal descends to the left),
          and the amount of their occurrence.
        """

    good_words_lst = []
    # Call to a function matrix_diagonal
    matrix_diagonal = up_right_diagonal(matrix_lst)
    # Call to a function reverse_matrix
    matrix_reverse = reverse_matrix(matrix_diagonal)
    # Call to a function search_words_and_count
    return search_words_and_count(words, matrix_reverse, good_words_lst)


def down_right_search(matrix_lst, words):
    # y

    """
        The function gets the letter matrix, and the word list.
        :param matrix_lst: Letter matrix.
        :param words: Word list.
        :return: The function returns a dictionary of all the words found
         in the down and right direction (diagonal descends to the right),
          and the amount of their occurrence.
        """

    good_words_lst = []
    # Call to a function matrix_diagonal
    matrix_diagonal = down_right_diagonal(matrix_lst)
    # Call to a function search_words_and_count
    return search_words_and_count(words, matrix_diagonal, good_words_lst)


def up_left_search(matrix_lst, words):
    # x

    """
        The function gets the letter matrix, and the word list.
        :param matrix_lst: Letter matrix.
        :param words: Word list.
        :return: The function returns a dictionary of all the words found
         in the up and left direction (diagonal ascends left),
         and the amount of their occurrence.
        """

    good_words_lst = []
    # Call to a function matrix_diagonal
    matrix_diagonal = down_right_diagonal(matrix_lst)
    # Call to a function reverse_matrix
    matrix_reverse = reverse_matrix(matrix_diagonal)
    # Call to a function search_words_and_count
    return search_words_and_count(words, matrix_reverse, good_words_lst)


def finale_directions(directions):

    """
    The function gets the list of directions and checks if there are
     double directions in the same string of directions. If so, the
      function removes the double directions, and finally returns the
       shortlist.
    :param directions: The directions
    """

    direction_lst = []
    for letter in directions:
        if letter not in direction_lst:
            direction_lst.append(letter)
    return ''.join(direction_lst)


def find_words(word_list, matrix, directions):

    """
    The function gets a list of words, a matrix of letters, a string of
     letters that represent the directions for searching the matrix.
    :param word_list: List of words.
    :param matrix: Matrix of letters.
    :param directions: String of letters that represent the directions for
     searching the matrix.
    :return: The function returns a list of tuples. Every tuple contain
    contains the words found in the matrix, and the number of times that
     word was found in the matrix.
    """

    # Final dict
    sum_up_dict = {}
    # Call to the function finale_directions.
    min_directions = finale_directions(directions)
    # In the following lines the function checks which letters are in the
    # directions. For each letter that is in the directions the function
    # calls the appropriate function in terms of search, and in addition,
    # it updates the main dictionary.
    for letter in min_directions:
        if letter == 'u':
            dict_u = up_search(matrix, word_list)
            sum_up_dict = update_dict(dict_u, sum_up_dict)
        elif letter == 'd':
            dict_d = down_search(matrix, word_list)
            sum_up_dict = update_dict(dict_d, sum_up_dict)
        elif letter == 'r':
            dict_r = right_search(matrix, word_list)
            sum_up_dict = update_dict(dict_r, sum_up_dict)
        elif letter == 'l':
            dict_l = left_search(matrix, word_list)
            sum_up_dict = update_dict(dict_l, sum_up_dict)
        elif letter == 'w':
            dict_w = up_right_search(matrix, word_list)
            sum_up_dict = update_dict(dict_w, sum_up_dict)
        elif letter == 'x':
            dict_x = up_left_search(matrix, word_list)
            sum_up_dict = update_dict(dict_x, sum_up_dict)
        elif letter == 'y':
            dict_y = down_right_search(matrix, word_list)
            sum_up_dict = update_dict(dict_y, sum_up_dict)
        elif letter == 'z':
            dict_z = down_left_search(matrix, word_list)
            sum_up_dict = update_dict(dict_z, sum_up_dict)
    # Call to a function dictionary_to_list
    sum_up_lst = dictionary_to_list(sum_up_dict)
    return sum_up_lst


def write_output(results, filename):

    """
    The function produces the file whose name is given as a parameter,
    and will write into it the search results of the words in the letter
    matrix.
    :param results: The search results of the letter matrix.
    :param filename: The file name.
    :return: The file of the results.
    """

    with open(filename, 'w') as final_file:
        for i in results:
            result = str(i[0]) + ',' + str(i[1])
            final_file.write(result + '\n')
        final_file.close()
    return final_file


def main():

    """
    The main function that makes calls to all the other functions.
    """

    # In the following lines the function checks the correctness of the
    # input. If the input is incorrect, the function returns a message due
    # to an error.
    if len(sys.argv) != 5:
        print('Number of parameters is invalid')
        return
    if not sys.argv[1] and not sys.argv[2]:
        print('Word list does not exist')
        return
    if not sys.argv[1]:
        print('Word list does not exist')
        return
    if not sys.argv[2]:
        print('Matrix does not exist')
        return
    for letter in sys.argv[4]:
        if letter not in 'udrlwxyz':
            print('The directions in not valid')
            return
    # Call to all other functions, in order to realize the bulk.
    word_lst = read_wordlist(sys.argv[1])
    mat = read_matrix(sys.argv[2])
    if word_lst == [] or mat == []:
        write_output([], sys.argv[3])
        exit()
    result = find_words(word_lst, mat, sys.argv[4])
    write_output(result, filename=sys.argv[3])


if __name__ == '__main__':
    main()
