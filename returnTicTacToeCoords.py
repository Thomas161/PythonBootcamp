# Print coordinates for tic tac toe board

def get_row_col(coordinates):
    col = coordinates[0]
    row = int(coordinates[1])
    
    if col == "A":
        col = 0
    if col == "B":
        col = 1
    if col == "C":
        col = 2
    if row == 1:
        row = int(row-1)
    if row == 2:
        row = int(row-1)
    if row == 3:
        row = int(row-1)
#     print(row,col)
    return row,col

get_row_col("A1")
