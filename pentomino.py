import random


pentominoes = [
    [[0, 1, 1],
     [1, 1, 0],
     [0, 1, 0]], #F

    [[1, 1, 1, 1, 1]], #I


    [[1, 1, 1, 1],
     [1, 0, 0, 0]], #L

    [[1, 1, 1, 1],
     [0, 0, 1, 0]], #Y


    [[0, 1],
     [0, 1],
     [1, 1],
     [1, 0]], #N

    [[1, 0, 1],
     [1, 1, 1]], #U


    [[1, 1, 1],
     [0, 0, 1],
     [0, 0, 1]], #V


    [[1, 1, 0],
     [0, 1, 1],
     [0, 0, 1]], #W


    [[1, 1, 0],
     [0, 1, 0],
     [0, 1, 1]], #Z

    [[1, 1, 1], #T
     [0, 1, 0],
     [0, 1, 0]],

    [[1, 1], #P
     [1, 1],
     [0, 1]],

    [[0, 1, 0],
     [1, 1, 1],
     [0, 1, 0]], #X

]

def place_pentomino(matrix, pentomino, x, y):
    for i in range(len(pentomino)):
        for j in range(len(pentomino[i])):
            if pentomino[i][j] == 1:
                matrix[x + i][y + j] = 1

def display_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=' ')
        print()

def generate_pentomino_placements():
    matrix = [[0] * 10 for _ in range(6)]
    placements = [[] for _ in range(len(pentominoes))]

    for pentomino_index, pentomino in enumerate(pentominoes):
        for _ in range(10):
            i = random.randint(0, 6 - len(pentomino))
            j = random.randint(0, 10 - len(pentomino[0]))
            temp_matrix = [row[:] for row in matrix]
            place_pentomino(temp_matrix, pentomino, i, j)
            placements[pentomino_index].append(temp_matrix)
            # display_matrix(temp_matrix)
            # print()

    return placements

p = generate_pentomino_placements()
with open('pentonimos.dat', 'w') as file:
    file.write('P = '+ str(p))
    print('file saved')