ps = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ']] 


def openRowFinder(column):
  for i in range (0,6):
    if ps[5][column] == ' ':
      availableRow = 5
      return availableRow
      break
    if ps[0][column] != ' ':
      print('Invalid move: Column is Full')
      break
    if  column < 0 or column > 7:
      print("Invalid move: Column doesn't Exist")
      break
    if ps[i+1][column] != ' ':
      availableRow = i
      return availableRow
      break
    else:
      pass
    
    
def dropPiece(piece, column):
  row = openRowFinder(column)
  global ps
  ps[row][column] = piece
  board = f'''
  1   2   3   4   5   6   7
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
| {ps[0][0]} | {ps[0][1]} | {ps[0][2]} | {ps[0][3]} | {ps[0][4]} | {ps[0][5]} | {ps[0][6]} |   6
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
| {ps[1][0]} | {ps[1][1]} | {ps[1][2]} | {ps[1][3]} | {ps[1][4]} | {ps[1][5]} | {ps[1][6]} |   5
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
| {ps[2][0]} | {ps[2][1]} | {ps[2][2]} | {ps[2][3]} | {ps[2][4]} | {ps[2][5]} | {ps[2][6]} |   4
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
| {ps[3][0]} | {ps[3][1]} | {ps[3][2]} | {ps[3][3]} | {ps[3][4]} | {ps[3][5]} | {ps[3][6]} |   3
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
| {ps[4][0]} | {ps[4][1]} | {ps[4][2]} | {ps[4][3]} | {ps[4][4]} | {ps[4][5]} | {ps[4][6]} |   2
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
| {ps[5][0]} | {ps[5][1]} | {ps[5][2]} | {ps[5][3]} | {ps[5][4]} | {ps[5][5]} | {ps[5][6]} |   1
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
'''
  print(board)
