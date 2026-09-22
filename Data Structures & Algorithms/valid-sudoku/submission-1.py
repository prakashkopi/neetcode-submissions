class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use 3 hashsets to detect duplicates in the row, col and square
        rows= defaultdict(set)
        cols= defaultdict(set)
        squares= defaultdict(set)

        # key: rowNum 0 --> set of unique values in that row
        # key: colNum 0 --> set of unique values in that row 
        # key: square (0,0) --> set of unique values in that square
            # we can use integer division to determine the indices

        # O(1) time and space because we have at most 9^2

        for r in range(9):
            for c in range(9): 
                # ignore empty values in the board
                if board[r][c] != ".":
                    # check for duplicates
                    currentValue= board[r][c]
                    currentRow= rows[r]
                    currentCol= cols[c]
                    currentSquare= squares[(r//3, c//3)]

                    if (currentValue in currentRow or currentValue in currentCol or currentValue in currentSquare): 
                        return False

                    # add values of each row, col, and square to each hashmap so we can detect duplicates
                    rows[r].add(board[r][c]) 
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        
        return True 