class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        matrix = [["#" for _ in range(3)] for _ in range(3)]

        turn = "x"

        for i, j in moves:
            matrix[i][j] = turn
            turn = "o" if turn == "x" else "x"

        for row in range(3):
            if matrix[row][0] != "#" and matrix[row][0] == matrix[row][1] == matrix[row][2]:
                return "A" if matrix[row][0] == "x" else "B"

        for col in range(3):
            if matrix[0][col] != "#" and matrix[0][col] == matrix[1][col] == matrix[2][col]:
                return "A" if matrix[0][col] == "x" else "B"

        if matrix[0][0] != "#" and matrix[0][0] == matrix[1][1] == matrix[2][2]:
            return "A" if matrix[0][0] == "x" else "B"

        if matrix[0][2] != "#" and matrix[0][2] == matrix[1][1] == matrix[2][0]:
            return "A" if matrix[0][2] == "x" else "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"