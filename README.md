<h1>Recursive Python Solver</h1>

<p>This is a code fully written in python that utilizes recursive functions to solve a Sudoku Puzzle. The idea behind using recursion for this, is that it generates a tree of multiple solution paths from an initial "0", and returns back to the initial "0" if that path does not lead to an overall solution.</p>

<p>This Sudoku solver is divided into 4 functions</p>
<ul>
  <li><strong>def print_board(board):</strong><br/><span>&nbsp;&nbsp;&nbsp;&nbsp;Prints the entire board</span></li>
  <li><strong>def find_zero(board):</strong><br/><span>&nbsp;&nbsp;&nbsp;&nbsp;Finds the position of the first "0" value.</span></li>
  <li><strong>def is_valid(board, row, col, value):</strong><br/><span>&nbsp;&nbsp;&nbsp;&nbsp;Determines whether an added value is valid.</span></li>
  <li><strong>def solve(board):</strong><br/><span>&nbsp;&nbsp;&nbsp;&nbsp;Recursive function that explores the paths made by hypothetical solutions.</span></li>
</ul>
