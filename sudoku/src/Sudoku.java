public class Sudoku {
    private static final int BOARD_SIZE = 9;
    private static final int EMPTY = 0;
    private int[][] board;

    public Sudoku(int[][] board) {
        this.board = new int[BOARD_SIZE][BOARD_SIZE];
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                this.board[i][j] = board[i][j];
            }
        }
    }

    public boolean solve() {
        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE; col++) {
                if (board[row][col] == EMPTY) {
                    for (int num = 1; num <= BOARD_SIZE; num++) {
                        if (isValid(row, col, num)) {
                            board[row][col] = num;

                            if (solve()) {
                                return true;
                            } else {
                                board[row][col] = EMPTY;
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isValid(int row, int col, int num) {
        // check row
        for (int i = 0; i < BOARD_SIZE; i++) {
            if (board[row][i] == num) {
                return false;
            }
        }

        // check column
        for (int i = 0; i < BOARD_SIZE; i++) {
            if (board[i][col] == num) {
                return false;
            }
        }

        // check square
        int boxRow = row - row % 3;
        int boxCol = col - col % 3;
        for (int i = boxRow; i < boxRow + 3; i++) {
            for (int j = boxCol; j < boxCol + 3; j++) {
                if (board[i][j] == num) {
                    return false;
                }
            }
        }

        return true;
    }

    public void print() {
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] board = {
                {1, 0, 9, 0, 0, 2, 6, 4, 0},
                {0, 0, 5, 0, 0, 3, 0, 1, 9},
                {4, 0, 8, 0, 0, 0, 2, 0, 0},
                {0, 0, 7, 8, 0, 0, 1, 0, 5},
                {0, 8, 0, 0, 6, 0, 4, 0, 0},
                {6, 1, 4, 0, 3, 0, 8, 0, 0},
                {7, 0, 3, 2, 0, 5, 0, 8, 0},
                {0, 0, 0, 6, 0, 8, 0, 0, 0},
                {0, 2, 6, 0, 0, 9, 5, 7, 1}};
        Sudoku s = new Sudoku(board);
        s.solve();
        s.print();
    }
}