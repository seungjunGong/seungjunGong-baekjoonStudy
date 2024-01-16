from collections import deque

def find_block(graph, v, n, move_to):    
    queue = deque([v])
    block = [v]
    
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        
        for i, j in move_to:
            xi, yj = x + i, y + j
            if -1 < xi < n and -1 < yj < n and graph[xi][yj]:
                block.append((xi, yj))
                queue.append((xi, yj))
    return block

def make_blocks(board, n):
    move_to = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    blocks = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                blocks.append(find_block(board, (i, j), n, move_to))
    return blocks

def make_box(block):
    x, y = zip(*block)
    col, row = max(x) - min(x) + 1, max(y) - min(y) + 1
    box = [[0] * row for _ in range(col)]
    
    for i, j in block:
        i, j = i - min(x), j - min(y)
        box[i][j] = 1
    return box

def rotate_block(block):
    cnt = 0
    rotate_block = [[0]*len(block) for _ in range(len(block[0]))]
    
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j]:
                cnt += 1
            rotate_block[j][len(block)-1-i] = block[i][j]
    return rotate_block, cnt

def match_blank(blank, blocks):
    for i, block in enumerate(blocks):
        block = make_box(block)
        for _ in range(4):
            block, cnt = rotate_block(block)   # 블록 회전
            if blank == block:
                del blocks[i]
                return cnt
    return 0

def solution(game_board, table):
    answer = 0
    n = len(table)  
    
    blocks = make_blocks(table, n)  # 블록 찾기
    # 빈칸 찾기(빈칸: 1, 블록: 0 변환)
    board = list(map(lambda x: list(map(lambda y: 1 - y, x)), game_board))
    blanks = make_blocks(board, n)

    # 빈칸-블록 매치(박스 만들기 매칭)
    for blank in blanks:
        blank = make_box(blank)
        answer += match_blank(blank, blocks)
                
    return answer