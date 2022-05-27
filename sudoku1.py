
# read file
sudokufile = open("/Users/mborkar/PycharmProjects/sudoku/sudokufile.txt", "r")
sudokustr = sudokufile.read()

sudokuarr = []
sudokuarr = sudokustr.split('\n')
print (sudokuarr)

# populate mainsoduku
sudoku = []
for i in range (0,len(sudokuarr)):
    sudoku.append (sudokuarr[i].split(','))
print (sudoku)
print (len(sudoku))

#populate soduku notes
snotes = []
for i in range (0,len (sudoku[0])):
    snotes.append([])
    for j in range (0, len(sudoku)):
        if sudoku[i][j] != 'x':
            # print (sudoku[i][j])
            snotes[i].append ([int(sudoku[i][j])])
        else:
            snotes[i].append ([1,2,3,4])
print (snotes)

#process notes based on mainsoduku # row
for i in range (0,len (sudoku[0])):
    for j in range (0, len(sudoku)):
        # print (snotes[i][j])
        if len (snotes[i][j]) == 1:
            currcell=snotes[i][j][0]
            # print(currcell)
            for k in range (0,len(sudoku)):
                if j != k :
                    #print(snotes[i][k])
                    try:
                        snotes[i][k].remove(currcell)
                    except ValueError: continue;
        print(snotes)

#process notes based on mainsoduku #column
for i in range (0,len (sudoku[0])):
    for j in range (0, len(sudoku)):
        # print (snotes[i][j])
        if len (snotes[j][i]) == 1:
            currcell=snotes[j][i][0]
            # print(currcell)
            for k in range (0,len(sudoku)):
                if i != k :
                    #print(snotes[i][k])
                    try:
                        snotes[k][i].remove(currcell)
                    except ValueError: continue;
        print(snotes)