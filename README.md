# NQueenProblem
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

Using backtracking algorithm, The idea is to place queens one by one in different rows, starting from the first row. When we place a queen in a row, we check for clashes with queens that we already assigned for other rows. In the current row, if we find a coloumn for which there is no clash, we mark this row and column as part of the solution. If we do not find such a coloumn due to clashes then we backtrack and return false.

1) Start in the first row

2) If all queens are placed
    return true
    
3) Try all coloumn in the current row. 
   Do following for every tried coloumn.
   
    a) If the queen can be placed safely in this coloumn 
       then mark this [row, column] as part of the 
       solution and recursively check if placing
       queen here leads to a solution.
       
    b) If placing the queen in [row, column] leads to
       a solution then return true.
       
    c) If placing queen doesn't lead to a solution then
       unmark this [row, column] (Backtrack) and go to 
       step (a) to try other rows.
       
4) If all coloumn have been tried and nothing worked,
   return false to trigger backtracking.
