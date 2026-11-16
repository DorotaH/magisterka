def generate_matrix(n):
        if n <= 0:
            return  [] 
        matrix=[row[:] for row in [[0]*n]*n]        
        row_st, row_ed=0, n-1        
        col_st=0
        col_ed, current=n-1, 1        
        while (True):
            if  current>n*n:
                break
            for  c in  range (col_st, col_ed+1):
                matrix[row_st][c] = current
                current=current+1
            row_st=row_st+1
            for  r in  range (row_st, row_ed+1):
                matrix[r][col_ed] = current
                current=current+1
            col_ed=col_ed-1
            for  c in  range (col_ed, col_st - 1, -1):
                matrix[row_ed][c] = current
                current=current+1
            row_ed=row_ed-1
            for  r in  range (row_ed, row_st - 1, -1):
                matrix[r][col_st] = current
                current=current+1
            col_st=col_st+1
        return  matrix
