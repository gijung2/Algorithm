#위의숫자에서 겹치는 안겹치는지 확인
#조건을 두개 성립해야됨 한줄에 겹치는 숫자가 없으면서 동시에 3*3배열에서 겹치는게 없어야됨.

T = int(input())


def check(board):

    for r in range(9):
        if len(set(board[r])) !=9:
            return 0

    for c in range(9):
        col = [board[r][c] for r in range(9)]
        if len(set(col)) != 9:
            return 0

    
    for sr in range(0,9,3):
        for sc in range(0,9,3):
            box= []
            
            for r in range(sr, sr+3):
                for c in range(sc, sc+3):
                    box.append(board[r][c])
                    
            if len(set(box)) !=9:
                return 0
            
    return 1

for tc in range(1,T+1):
    board = [list(map(int,input().split())) for x in range(9)]
    result = check(board)
    print("#{} {}".format(tc,result))