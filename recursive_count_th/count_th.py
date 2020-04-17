'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    if('th' not in word):
        count = 0
    else:
        count = 1
        index_point = word.index('th') + 2
        count += count_th(word[index_point:])

    return count
