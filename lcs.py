""" 
Динамическое программирование. Наибольшая общая подпоследовательность. 
(Longest Common Subsequence - LCS)
"""


first_word = 'blue'
second_word = 'clues'

def lcs(first_word, second_word):
    matrix = [[0 for i in range(len(second_word) + 1)] for j in range(len(first_word) + 1)]

    for i in range(1, len(first_word) + 1):
        for j in range(1, len(second_word) + 1):
            if first_word[i-1] == second_word[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
                #matrix[i][j] = 0
    return matrix


print(lcs(first_word, second_word))
