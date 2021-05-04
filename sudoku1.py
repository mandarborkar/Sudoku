sudokufile = open("/Users/mborkar/PycharmProjects/sudoku/sudokufile.txt", "r")
sudokustr = sudokufile.read()
sudoku = []
sudokuarr = []
sudokuarr = sudokustr.split('\n')
print (sudokuarr)
for i in range (0,len(sudokuarr)):
    sudoku.append (sudokuarr[i].split(','))
print (sudoku)
print (len(sudoku))