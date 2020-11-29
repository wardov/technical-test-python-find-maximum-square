'''
I will add a feature in a perspective to read the file containing the plateau
and to convert it to a matrix of lists so as to work with it by this code
M is defined as a matrix input of lists
'''


def findMaxSubSquare(M):
    R = len(M)  # number of rows in M[][]
    C = len(M[0])  # number of columns in M[][]

    S = [[0 for k in range(C)] for l in range(R)]
    # here we have set the first row and column of S[][]

    # Construct other entries
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                              S[i-1][j-1]) + 1
            else:
                S[i][j] = 0

    # Find the maximum entry and
    # indices of maximum entry in S[][]
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print(M[i][j], end=" ")
        print("")


# a simple test of the program
M1 = [[0, 1, 1, 0, 1],
      [1, 1, 0, 1, 0],
      [0, 1, 1, 1, 0],
      [1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0]]

M = [[0, 1, 1, 0, 1],
     [1, 1, 1, 1, 1],
     [0, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [0, 1, 1, 1, 0]]


findMaxSubSquare(M)
