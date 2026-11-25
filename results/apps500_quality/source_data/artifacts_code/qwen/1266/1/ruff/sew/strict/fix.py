def  is_king_in_check(king_x, king_y, pieces):
    for  piece_type, x, y in  pieces:
        if piece_type == 'Q' or piece_type == 'R':
            if x == king_x or y == king_y:
                return  True
        elif piece_type == 'B':
            if abs(x-king_x)==abs(y-king_y):
                return True
    return False

def  main():
    import sys
    input=sys.stdin.read
    data=input().split()

    n=int(data[0])
    king_x, king_y=map(int, data[1:3])

    pieces=list()
    for  i in  range(n):
        piece_type, x = data[6 + 3 * i], int(data[7 + 3 * i])
        y = int(data[3 * i + 8])
        pieces.append((piece_type, x, y))

    if not is_king_in_check(king_x, king_y, pieces):
        print("NO")
    else:
        print("YES")

if  __name__=="__main__":
    main()
