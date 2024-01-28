# 419. Battleship in a board
class Solution:
  def countBattleships(self, board: List[List[str]]) -> int:
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                if (i == 0 or board[i-1][j] == ".") and (j == 0 or board[i][j-1] == "."):
                    count += 1
    return count
