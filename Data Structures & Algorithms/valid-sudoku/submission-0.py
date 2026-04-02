class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # we can use a hashset for every row and column to check for duplicates
        # and this is efficient cuz adding elements to or checking duplicates is O(1)

        # rule 3 is a bit more difficult its the 3x3 sub-boxes part
        # but basically we use integer division to simplify each row/column to a 3x3
        # aka 0-2, 4-6, 7-9

        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # rows is the hashmap, and r is the current row
                # and same for columns
                if (board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in squares[(r // 3 , c // 3)]):
                    return False

                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[( r // 3 , c // 3)].add(board[r][c])
        
        return True

        